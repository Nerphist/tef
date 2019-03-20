import json
import logging
import os
from collections import namedtuple

import requests

from rozklad_api.models import Lesson
from test_kpi.settings import BASE_DIR


def sync_with_kpi_rozklad():
    with open(os.path.join(BASE_DIR, 'rozklad_api/json_groups.json')) as f:
        f.seek(0)
        data = json.load(f)
    for group_id in data:
        sync_group(str(group_id))


def sync_group(group_id):
    try:
        response = request(group_id=group_id)
        result = json.loads(response, object_hook=lambda d: namedtuple('entity', d.keys())(*d.values())).data
    except Exception as e:
        logging.error('Error while parsing the result of the request')
        result = {}
    got_list, group_name = parse_lessons(result)
    db_entity_list = list(Lesson.objects.all().using('rozklad').filter(group_name=group_name))
    current_list = [i.as_json() for i in db_entity_list]
    for lesson_dict in got_list:
        if lesson_dict not in current_list:
            lesson = Lesson(
                id=lesson_dict.get('id'),
                lesson_name=lesson_dict.get('lesson_name'),
                teacher=lesson_dict.get('teacher'),
                day_number=lesson_dict.get('day_number'),
                lesson_number=lesson_dict.get('lesson_number'),
                lesson_week=lesson_dict.get('lesson_week'),
                lesson_room=lesson_dict.get('lesson_room'),
                lesson_type=lesson_dict.get('lesson_type'),
                group_name=group_name,
            )
            lesson.save(using='rozklad')
            print('INSERT')
    print(group_name)
    print(group_id)


def request(group_id='4355'):
    url = 'http://api.rozklad.org.ua/v2/groups/%s/lessons' % group_id
    try:
        response = requests.get(url).content.decode()
    except Exception as e:
        logging.error('Error while making request to the api.rozklad.org.ua')
        logging.error('Reason: ' + str(e))
        response = ''
    return response


def parse_lessons(result_dict):
    print('AAAAAAAAA')
    lesson_list = []
    group_name = None
    for lesson in result_dict:
        try:
            teacher = lesson.teachers[0].teacher_short_name
        except Exception as e:
            teacher = None
        try:
            lesson_room = lesson.rooms[0].room_name
        except Exception as e:
            lesson_room = None
        if not group_name:
            group_name = get_group_from_local_json(lesson.group_id)
        parsed_lesson = dict(
            id=int(lesson.lesson_id),
            lesson_name=lesson.lesson_name,
            teacher=teacher,
            day_number=int(lesson.day_number),
            lesson_number=int(lesson.lesson_number),
            lesson_week=int(lesson.lesson_week),
            lesson_room=lesson_room,
            lesson_type=lesson.lesson_type if lesson.lesson_type else None,
            group_name=group_name,
        )
        lesson_list.append(parsed_lesson)
    return lesson_list, group_name


def get_group_from_local_json(group_id):
    with open(os.path.join(BASE_DIR, 'rozklad_api/json_groups.json')) as f:
        f.seek(0)
        data = json.load(f)

    group_name = data[group_id]
    return group_name


def update_group_in_local_json(group_id, group_name):
    with open(os.path.join(BASE_DIR, 'rozklad_api/json_groups.json'), 'r+') as f:
        f.seek(0)
        data = json.load(f)
        if str(group_id) in data:
            return 'the group already exists'
        data.update({str(group_id): group_name})
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
    sync_group(group_id)
    return 'the group was successfully added'

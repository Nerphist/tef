import json
import os

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rozklad_api.models import Lesson
from rozklad_api.serializers import LessonSerializer
from rozklad_api.service import update_group_in_local_json
from test_kpi.settings import BASE_DIR


class GetLessonsView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        group_name = self.kwargs.get('group_name')
        print(group_name)

        lessons = list(map(lambda x: x.as_json(), Lesson.objects.all().using('rozklad').filter(group_name=group_name)))

        return lessons

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)

        def filter_for_day(week, day):
            return list(filter(lambda x: x.get('lesson_week') == week and x.get('day_number') == day, queryset))

        final_dict = {
            '1 week': {
                '1 day': filter_for_day(1, 1),
                '2 day': filter_for_day(1, 2),
                '3 day': filter_for_day(1, 3),
                '4 day': filter_for_day(1, 4),
                '5 day': filter_for_day(1, 5),
                '6 day': filter_for_day(1, 6),
            },
            '2 week': {
                '1 day': filter_for_day(2, 1),
                '2 day': filter_for_day(2, 2),
                '3 day': filter_for_day(2, 3),
                '4 day': filter_for_day(2, 4),
                '5 day': filter_for_day(2, 5),
                '6 day': filter_for_day(2, 6),
            }
        }

        print(queryset)

        return Response(final_dict)


@api_view(['GET', 'POST'])
def get_create_groups(request, **kwargs):
    if request.method == 'GET':
        with open(os.path.join(BASE_DIR, 'rozklad_api/json_groups.json')) as f:
            f.seek(0)
            data = json.load(f)
            print(data)
        return Response(data=data, status=200)
    else:
        post = json.loads(request.body.decode())
        group_name = post.get('group_name')
        group_id = str(post.get('group_id'))
        print(group_id)
        print(group_name)
        if not group_id or not group_name:
            return Response(data={'result': 'Not all necessary parameters were provided'}, status=404)
        try:
            response = requests.get('http://api.rozklad.org.ua/v2/groups/%s/lessons' % group_id).content.decode()
        except Exception as e:
            return Response(data={'result': 'Error while getting schedule from api.rozklad.org.ua'}, status=404)
        try:
            result_dict = json.loads(response)
            message = result_dict.get('message')
            data = result_dict.get('data')
            if message == 'Ok' and len(data) > 0:
                result = update_group_in_local_json(group_id, group_name)
                return Response(data={'result': result}, status=200)
            else:
                return Response(data={'result': 'group with this id doesn\'t exist'}, status=404)
        except Exception as e:
            print(e)
            return Response(data={'result': 'Received inappropriate result from api.rozklad.org.ua'}, status=404)

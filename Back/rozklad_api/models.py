from django.db import models


# Create your models here.


class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    lesson_name = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255, null=True)
    day_number = models.IntegerField()
    lesson_number = models.IntegerField()
    lesson_week = models.IntegerField()
    lesson_room = models.CharField(max_length=255, null=True)
    lesson_type = models.CharField(max_length=255, null=True)
    group_name = models.CharField(max_length=255)

    def as_json(self):
        return dict(
            id=self.id,
            lesson_name=self.lesson_name,
            teacher=self.teacher,
            day_number=self.day_number,
            lesson_number=self.lesson_number,
            lesson_week=self.lesson_week,
            lesson_room=self.lesson_room,
            lesson_type=self.lesson_type,
            group_name=self.group_name,
        )

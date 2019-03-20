from rest_framework.serializers import ModelSerializer

from rozklad_api.models import Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

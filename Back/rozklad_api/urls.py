from django.conf.urls import url

from rozklad_api.views import GetLessonsView, get_create_groups

app_name = 'rozklad_api'

urlpatterns = [
    url(r'^groups/$', view=get_create_groups, name='groups-list-get-create'),
    url(r'^(?P<group_name>\S{3,7})/$', view=GetLessonsView.as_view(), name='lessons-list-get'),
    # url(r'^groups/name=(?P<group_name>[A-Z]{2,3}-[0-9]{1,5}[a-z]{,3}),id=(?P<group_id>[0-9]{1,5})/$',
    #     view=create_group,
    #     name='create-group'),
]

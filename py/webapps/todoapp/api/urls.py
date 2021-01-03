from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    #path('', views.apiOverview, name="api-overview"),
    path('task/<str:pk>', views.TaskDetail.as_view()),
    path('tasks', views.TasksList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

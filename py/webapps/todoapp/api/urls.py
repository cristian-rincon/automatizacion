from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [path('api/', views.apiOverview, name="api-overview"),
               path('api/task/<str:pk>', views.TaskDetail.as_view()),
               path('api/tasks', views.TasksList.as_view()),
               ]


urlpatterns = format_suffix_patterns(urlpatterns)

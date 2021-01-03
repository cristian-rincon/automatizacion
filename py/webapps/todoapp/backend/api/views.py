from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import TaskSerializer
from .models import Task

"""
API Overview
"""


class TasksList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    List all tasks, or create a new one.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        """
        Get all tasks.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create new task.
        """
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve, update or delete a task instance.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        """
        Get task by a given id.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update task.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete task.
        """
        return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List (GET)': '/tasks/',
        'Detail View (GET)': '/task/<str:pk>/',
        'Create (POST)': '/tasks/',
        'Update': '/task/<str:pk>/',
        'Delete': '/task/<str:pk>/',
    }
    return Response(api_urls)

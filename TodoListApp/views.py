from rest_framework import generics
from .models import TodoListModel
from .serializers import TodoTaskSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoTaskSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoTaskSerializer

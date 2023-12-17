from rest_framework import serializers
from .models import TodoListModel


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListModel
        fields = '__all__'
        read_only_fields = ('timestamp',)

from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'tree', 'content','created_at', 'updated_at']
        extra_kwargs = {
            'user': {'write_only': True},
            'tree': {'write_only': True},
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }

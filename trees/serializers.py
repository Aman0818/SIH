from rest_framework import serializers
from .models import Tree
from utils.utils import generate_presigned_url

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['common_name', 'botanical_name', 'habitant', 'region', 'type', 'image_link', 'video_link', 'information', 'medical_use']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('image_link'):
            representation['image_link'] = generate_presigned_url(representation['image_link'].replace('https://ayushvatika.s3.amazonaws.com/', ''))

        if representation.get('video_link'):
            representation['video_link'] = generate_presigned_url(representation['video_link'].replace('https://ayushvatika.s3.amazonaws.com/', ''))

        return representation

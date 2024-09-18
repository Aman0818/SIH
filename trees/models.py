from django.db import models
import os
def tree_image_file_path(instance, filename):

    extension = filename.split('.')[-1]
    filename = f"{instance.common_name.lower().replace(' ', '_')}_image.{extension}"
    return os.path.join('tree_images/', filename)

def tree_audio_file_path(instance, filename):

    extension = filename.split('.')[-1]
    filename = f"{instance.common_name.lower().replace(' ', '_')}_audio.{extension}"
    return os.path.join('tree_audio/', filename)

class Tree(models.Model):

    common_name = models.CharField(max_length=255, unique=True)  
    botanical_name = models.CharField(max_length=255, blank=True, null=True)
    habitant = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    medical_use = models.TextField(blank=True, null=True)
    image_link = models.ImageField(upload_to=tree_image_file_path, blank=True, null=True)
    audio_link = models.FileField(upload_to=tree_audio_file_path, blank=True, null=True)

    def __str__(self):
        return self.common_name

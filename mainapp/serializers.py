
from django.db import models
from rest_framework import serializers
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Movies


# Create your models here.
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

class Movieserializer(serializers.ModelSerializer):
    movie_image_url = serializers.SerializerMethodField()
    movie_video_url = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = '__all__'  # keeps original fields
        # OR list all fields if you want to avoid sending raw CloudinaryField

    def get_movie_image_url(self, obj):
        if obj.movie_image:
            # ensure HTTPS and no extra prefix
            return str(obj.movie_image).replace("http://", "https://")
        return ""

    def get_movie_video_url(self, obj):
        if obj.movie_video:
            return str(obj.movie_video).replace("http://", "https://")
        return ""


class Movieupdateserializer(serializers.ModelSerializer):
    movie_no = serializers.IntegerField(required=False)
    movie_name = serializers.CharField(required=False)
    movie_desc = serializers.CharField(required=False)
    movie_rating = serializers.FloatField(required=False)

    class Meta:
        model = Movies
        fields = ['movie_no', 'movie_name', 'movie_desc', 'movie_rating']

    
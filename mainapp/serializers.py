from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Movies

# Create your models here.
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


# Serializers for Movies
class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"


class Movieupdateserializer(serializers.ModelSerializer):
    movie_no = serializers.IntegerField(required=False)
    movie_name = serializers.CharField(required=False)
    movie_desc = serializers.CharField(required=False)
    movie_rating = serializers.FloatField(required=False)

    class Meta:
        model = Movies
        fields = ['movie_no', 'movie_name', 'movie_desc', 'movie_rating']

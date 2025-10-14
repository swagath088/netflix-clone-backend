from django.shortcuts import render
from . serializers import Userserializer,Movieserializer,Movieupdateserializer
from rest_framework import status
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from django.contrib.auth import authenticate
from django.db.models import Q
import re
from django.conf import settings
from django.http import FileResponse
from rest_framework.authtoken.models import Token

from .models import Movies
# Create your views here.
class register(APIView):
    def post(self,request):
        obj=Userserializer(data=request.data)
        if obj.is_valid()==True:
            res=obj.save()
            res.password=make_password(res.password)
            res.save()
            token=Token.objects.create(user=res)
            return Response(status=HTTP_201_CREATED)
        else:
            return Response( obj.errors,status=HTTP_400_BAD_REQUEST)
class Add(APIView):
    def post(self,request):
       obj= Movieserializer(data=request.data)
       if obj.is_valid():
           obj.save()
           return Response(status=HTTP_201_CREATED)
       else:
           return Response(obj.errors,status=HTTP_400_BAD_REQUEST)

class show(APIView):
    def get(self,request):
        obj=Movies.objects.all()
        serializer_obj=Movieserializer(obj,many=True)
        return Response(serializer_obj.data,status=HTTP_200_OK)
    
class StreamVideo(APIView):
    def get(self, request, filename):
        # path of the video inside media/videos/
        file_path = os.path.join(settings.MEDIA_ROOT, "videos", filename)

        # open file and return it in chunks
        return FileResponse(open(file_path, 'rb'), content_type='video/mp4')

class get(APIView):
    def get(self, request, pk):
        movies = Movies.objects.filter(
            Q(movie_no__iexact=pk) | Q(movie_name__icontains=pk)
        )

        if not movies.exists():
            return Response({'error': 'Movie not found'}, status=HTTP_400_BAD_REQUEST)

        serializer = Movieserializer(movies, many=True)
        return Response(serializer.data)

class DeleteMovie(APIView):
    def delete(self, request, pk):
        try:
            movie = Movies.objects.get(movie_no=pk)

            # Delete image file
            if movie.movie_image:
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT, movie.movie_image.name))
                except:
                    pass

            # Delete video file
            if movie.movie_video:
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT, movie.movie_video.name))
                except:
                    pass

            movie.delete()
            return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class put(APIView):
    def put(self,request,pk):
        try:
            obj=Movies.objects.get(movie_no=pk)
            res=Movieupdateserializer(obj,data=request.data,partial=True)
            if res.is_valid():
                res.save()
                return Response(status=HTTP_200_OK)
            else:
                return Response(res.errors,status=HTTP_400_BAD_REQUEST)
        except Movies.DoesNotExist:
            return Response({'movie':'not found'},status=HTTP_400_BAD_REQUEST)
        
class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username,
                "is_superuser": user.is_superuser
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class get_one_movie(APIView):
    def get(self, request):
        try:
            movie = Movies.objects.get(movie_no=1)  # or Movies.objects.first()
            serializer = Movieserializer(movie)
            return Response(serializer.data, status=HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response({"error": "Movie not found"}, status=HTTP_400_BAD_REQUEST)
        
from django.contrib.auth.models import User
from django.http import HttpResponse

# TEMPORARY: Creates a new superuser
def make_superuser(request):
    username = 'swagath'  # change if you want a different username
    password = 'NewStrongPassword123'  # change to your desired password
    email = 'swagath@example.com'  # your email

    # Delete old user if exists
    User.objects.filter(username=username).delete()

    # Create superuser
    User.objects.create_superuser(username=username, email=email, password=password)

    return HttpResponse(f"Superuser '{username}' created successfully ✅")



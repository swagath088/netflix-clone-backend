# Django imports
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.conf import settings
from django.http import FileResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
import re

# REST framework imports
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny

# Local imports
from .models import Movies
from .serializers import Userserializer, Movieserializer, Movieupdateserializer

# Cloudinary imports
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import exceptions as cloudinary_exceptions

# Python standard library
import traceback

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

@method_decorator(csrf_exempt, name='dispatch')
class UploadMedia(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            image_file = request.FILES.get("movie_image")
            video_file = request.FILES.get("movie_video")

            if not image_file and not video_file:
                return Response({"error": "No files uploaded"}, status=400)

            # Upload image
            image_url = None
            if image_file:
                resp = cloudinary.uploader.upload(image_file, resource_type="image")
                image_url = resp.get("secure_url")

            # Upload video
            video_url = None
            if video_file:
                resp = cloudinary.uploader.upload(
                    video_file,
                    resource_type="video",
                    timeout=300  # allow big videos
                )
                video_url = resp.get("secure_url")

            return Response({"image_url": image_url, "video_url": video_url}, status=201)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class AddMovie(APIView):
    def post(self, request):
        try:
            movie_name = request.data.get("movie_name")
            movie_desc = request.data.get("movie_desc")
            movie_rating = int(request.data.get("movie_rating", 0))
            movie_image = request.data.get("movie_image")
            movie_video = request.data.get("movie_video")

            if not movie_name or not movie_image or not movie_video:
                return Response({"error": "Required fields missing"}, status=400)

            movie = Movies.objects.create(
                movie_name=movie_name,
                movie_desc=movie_desc,
                movie_rating=movie_rating,
                movie_image=movie_image,
                movie_video=movie_video
            )

            return Response({"message": "Movie added successfully!"}, status=201)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=500)

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

@method_decorator(csrf_exempt, name='dispatch')
class DeleteMovie(APIView):
    def delete(self, request, pk):
        try:
            movie = Movies.objects.get(movie_no=pk)
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

class get(APIView):
    def get(self, request, pk):
        """
        Search by movie_no (if numeric) or movie_name (partial, case-insensitive)
        """
        try:
            movies = Movies.objects.filter(
                Q(movie_no=pk) | Q(movie_name__icontains=pk)
            )

            if not movies.exists():
                return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = Movieserializer(movies, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

cloudinary.config( 
  cloud_name = "dcguhkbhj", 
  api_key = "292771931593114", 
  api_secret = "zHqTM-v2a7ilpXr-2CZBlbsC6wg"
)

class SearchMovie(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        if name:
            movies = Movies.objects.filter(movie_name__icontains=name)
            serializer = Movieserializer(movies, many=True)
            return Response(serializer.data)
        return Response([], status=404)

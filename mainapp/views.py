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
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from .models import Movies

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from .models import Movies

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from mainapp.models import Movies
import os


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from .models import Movies

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from .models import Movies

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
import os
from django.conf import settings

# views.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
import os
from django.conf import settings

@method_decorator(csrf_exempt, name='dispatch')  # ✅ important for frontend DELETE
class DeleteMovie(APIView):
    def delete(self, request, pk):
        try:
            movie = Movies.objects.get(movie_no=pk)

            # Delete image
            if movie.movie_image and movie.movie_image.name:
                image_path = os.path.join(settings.MEDIA_ROOT, movie.movie_image.name)
                if os.path.exists(image_path):
                    os.remove(image_path)

            # Delete video
            if movie.movie_video and movie.movie_video.name:
                video_path = os.path.join(settings.MEDIA_ROOT, movie.movie_video.name)
                if os.path.exists(video_path):
                    os.remove(video_path)

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
        






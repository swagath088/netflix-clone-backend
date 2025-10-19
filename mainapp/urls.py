from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import SearchMovie

urlpatterns=[
    path('', views.show.as_view(), name='show_all'),
    path('register/',views.register.as_view()),
    path('login/', views.Login.as_view()),
    path('add/', views.AddMovie.as_view(), name='add'),
    path('show/',views.show.as_view()),
    path('video/<str:filename>/', views.StreamVideo.as_view()),
    path('UploadMedia/', views.UploadMedia.as_view(), name='upload_media'),
    path('get/<str:pk>/', views.get.as_view(), name='get-movie'),
    path('put/<int:pk>/', views.put.as_view(), name='update-movie'),
    path('delete/<int:pk>/', views.DeleteMovie.as_view(), name='delete-movie'),
    path('search/', SearchMovie.as_view(), name='search-movie'),



]
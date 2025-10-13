from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import make_superuser 
urlpatterns=[
    path('', views.show.as_view(), name='show_all'),
    path('make_superuser/', make_superuser),
    path('register/',views.register.as_view()),
    path('login/', views.Login.as_view()),
    path('Add/',views.Add.as_view()),
    path('show/',views.show.as_view()),
    path('video/<str:filename>/', views.StreamVideo.as_view()),
    path('get/<str:pk>',views.get.as_view()),
    path('put/<int:pk>',views.put.as_view()),
    path('delete/<int:pk>',views.delete.as_view())

]
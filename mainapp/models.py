from django.db import models
class Movies(models.Model):
    movie_no=models.IntegerField(primary_key=True)
    movie_name=models.CharField(max_length=100)
    movie_desc=models.CharField(max_length=100)
    movie_rating=models.IntegerField()
    movie_image=models.ImageField(upload_to='images/')
    movie_video=models.FileField(upload_to='videos/')

    
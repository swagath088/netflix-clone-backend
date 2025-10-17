from django.db import models
from cloudinary.models import CloudinaryField  # for Cloudinary uploads

class Movies(models.Model):
    movie_no = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_desc = models.TextField()
    movie_rating = models.IntegerField()
    movie_image = CloudinaryField('image')
    movie_video = CloudinaryField('video')

    def __str__(self):
        return self.movie_name

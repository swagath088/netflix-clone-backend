from django.db import models

class Movies(models.Model):
    movie_no = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_desc = models.TextField()  # longer descriptions
    movie_rating = models.IntegerField()
    movie_image = models.ImageField(upload_to='movies/images/')
    movie_video = models.FileField(upload_to='movies/videos/')

    def __str__(self):
        return self.movie_name

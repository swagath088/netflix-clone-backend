from django.db import models

class Movies(models.Model):
    movie_no = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_desc = models.TextField()
    movie_rating = models.IntegerField()
    
    # ✅ Change these to URLField
    movie_image = models.URLField(max_length=500, blank=True, null=True)
    movie_video = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.movie_name

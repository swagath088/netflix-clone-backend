from django.contrib import admin
from .models import Movies
from django.utils.html import format_html

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('movie_no', 'movie_name', 'movie_rating', 'image_preview', 'video_preview')
    readonly_fields = ('image_preview', 'video_preview')

    def image_preview(self, obj):
        if obj.movie_image:
            return format_html('<img src="{}" width="100" />', obj.movie_image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

    def video_preview(self, obj):
        if obj.movie_video:
            return format_html(
                '<video width="200" controls><source src="{}" type="video/mp4"></video>', 
                obj.movie_video.url
            )
        return "-"
    video_preview.short_description = 'Video Preview'

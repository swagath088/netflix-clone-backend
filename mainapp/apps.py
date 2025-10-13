from django.apps import AppConfig

class MainappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mainapp"

    def ready(self):
        # Only import here to avoid circular imports
        from .models import Movies
        from django.db.utils import OperationalError, ProgrammingError

        # Safe check in case DB isn't ready
        try:
            if not Movies.objects.filter(movie_no=1).exists():
                Movies.objects.create(
                    movie_no=1,
                    movie_name="Test Movie",
                    movie_desc="Description",
                    movie_rating=5,
                    movie_image="images/test.jpg",  # make sure file exists in media/
                    movie_video="videos/test.mp4"   # make sure file exists in media/
                )
        except (OperationalError, ProgrammingError):
            # Happens if tables are not migrated yet
            pass

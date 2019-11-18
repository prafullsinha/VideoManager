from django.db import models


# Create your models here.
class VideoModel(models.Model):
    title = models.CharField(max_length=25, primary_key=True)
    categories = models.CharField(max_length=15, blank=True)
    tags = models.CharField(max_length=20, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    duration = models.FloatField(blank=True)
    description = models.CharField(max_length=30, blank=True)
    thumbnail = models.FileField(upload_to='images/', blank=True, verbose_name="")
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Track(models.Model):
  #id field will server as primary key for the track
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  url = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)
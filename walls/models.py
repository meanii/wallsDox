from django.utils.timezone import now
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
class Wallpaper(models.Model):
  title = models.CharField(max_length=20)
  description  = models.TextField(max_length=200, blank=True)
  image = CloudinaryField('image')
  post_date = models.DateTimeField(default=now, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, related_name="tags")
  
  def __str__(self):
    return self.title
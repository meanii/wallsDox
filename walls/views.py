from django.shortcuts import render
from .models import Wallpaper, Tag


def home_view(request, *args, **kwargs):
  tags = Tag.objects.all()
  wallpapers = Wallpaper.objects.all()
  
  context = {
    'wallpapers': wallpapers,
    'tags': tags
  }
  return render(request, 'home.html', context)

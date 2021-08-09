from django.shortcuts import render
from reddit import getReddit

# Create your views here.

def home_view(request, *args, **kwargs):
  
  img_list = getReddit('wallpaper', limit=10)
  tags_list = [
    'r/wallpapers',
    'r/anime',
    'google pixle',
    'android 12',
    'stock walls',
    'oxgen os walls'
    ]
  context = {
    'wallpapers': img_list,
    'tags': tags_list
  }
  return render(request, 'home.html', context)

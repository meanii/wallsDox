from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Wallpaper, Tag


def home_view(request, *args, **kwargs):  
  print(request)
  if request.method == 'POST' and request.FILES:
    print('ypp')
    title = request.POST.get('title')
    description = request.POST.get('description')
    tags = request.POST.get('tags')
    image = request.FILES.get('image')
    user = request.user 

    instance = Wallpaper.objects.create(
      title=title,
      description=description,
      image=image,
      user=user
    )
    print(instance)
    tags = tags.split(',')
    print('tags', tags)
    for tag in tags:
      tagin = Tag.objects.filter(name__exact=title)
      print('tagin', tagin)
      if len(tagin) != 0:
        for _ in tagin:
          print('_', _)
          instance.tags.add(_)
      else:
        instance.tags.create(name=tag)
    return redirect('/')

  tags = Tag.objects.all()
  wallpapers = Wallpaper.objects.all()
  
  context = {
    'wallpapers': wallpapers,
    'tags': tags
  }
  return render(request, 'home.html', context)

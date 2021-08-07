from django.shortcuts import render
from reddit import getReddit
from .forms import ImageForm
# Create your views here.

def result_views(request, *args, **kwargs):
  search = None
  error = False 
  img_list = []
  
  if request.method == "POST":
    search = dict(request.POST).get('search')
    print(search)
    if isinstance(search, list):
      search = search[0]
  
  try:
    img_list = getReddit(search, limit=80)
  except KeyError:
    error = True
  
  if len(img_list) == 0:
    error = True
    
  content = {
    'reddit': img_list,
    'searched': search,
    'error': error
  }
  
  return render(request, 'results.html', content)

def home_view(request, *args, **kwargs):
  """print(request)
  if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
  else:
      form = ImageForm()
      """
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

from django.shortcuts import render
from reddit import getReddit

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
    
  content = {
    'reddit': img_list,
    'searched': search,
    'error': error
  }
  
  return render(request, 'results.html', content)

def home_view(request, *args, **kwargs):
  img_list = getReddit('wallpaper', limit=20)
  return render(request, 'home.html', {'reddit': img_list})
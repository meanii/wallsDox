from django.shortcuts import render
from reddit import getReddit
# Create your views here.
def result_views(request, *args, **kwargs):
  if request.method == "POST":
    search = dict(request.POST).get('search')
    print(search)
    if isinstance(search, list):
      search = search[0]
      
  img_list = getReddit(search, limit=80)
  return render(request, 'results.html', {'reddit': img_list})

def home_view(request, *args, **kwargs):
  img_list = getReddit('wallpaper', limit=20)
  return render(request, 'home.html', {'reddit': img_list})
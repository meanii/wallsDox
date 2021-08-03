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

def search_view(request, *args, **kwargs):
  return render(request, 'search.html', {})
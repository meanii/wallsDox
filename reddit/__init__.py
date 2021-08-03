import colorama
import json
import requests
from fake_useragent import UserAgent

def get_pictures_from_subreddit(data, subreddit):
    images_list = []
    for i in range(len(data)):
        current_post = data[i]['data']
        image_url = current_post['url']
        if '.png' in image_url:
            extension = '.png'
        elif '.jpg' in image_url or '.jpeg' in image_url:
            extension = '.jpeg'
        elif 'imgur' in image_url:
            image_url += '.jpeg'
            extension = '.jpeg'
        else:
            continue
        images_list.append(image_url)
    return images_list


def getReddit(search: str, limit: int = 30) -> list:
  colorama.init()
  ua = UserAgent()
  
  url = f'https://www.reddit.com/r/{search}/top/.json?sort=top&t=week&limit={str(limit)}'
  response = requests.get(url, headers={'User-agent': ua.random})
  if not response.ok:
    print("Error check the name of the subreddit", response.status_code)
  print(response.json())
  print(url)
  data = response.json()['data']['children']
  image_list = get_pictures_from_subreddit(data, search)
  return image_list
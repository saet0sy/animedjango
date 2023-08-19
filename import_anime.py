import os
import json
from django.core.wsgi import get_wsgi_application
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animewebapi.settings")
application = get_wsgi_application()

from anime.models import Anime

with open('anime_data.json', 'r') as json_file:
    anime_data = json.load(json_file)

for data in anime_data:
    release_year = int(data['release_year'])  # Преобразование строки в целое число
    
    anime = Anime(
        title=data['title'],
        description=data['description'],
        release_year=release_year,
        cover_image_url=data['cover_image_url']
    )
    anime.save()

print("Anime imported successfully.")

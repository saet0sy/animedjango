import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animewebapi.settings")
application = get_wsgi_application()

from anime.models import Anime, Genre, AnimeGenre

with open('anime_data.json', 'r', encoding='utf-8') as json_file:
    anime_data = json.load(json_file)

for data in anime_data:
    release_year = int(data['release_year'])  # Преобразование строки в целое число
    
    anime = Anime(
        title=data['title'],
        description=data['description'],
        release_year=release_year,
        cover_image_url=data['cover_image_url'],
        trailer_url=data.get('trailer_url', '')  # Добавляем ссылку на трейлер или пустую строку, если нет трейлера
    )
    anime.save()
    
    # Добавляем жанры для аниме
    for genre_name in data.get('genres', []):
        genre, _ = Genre.objects.get_or_create(name=genre_name)
        AnimeGenre.objects.create(anime=anime, genre=genre)

print("Anime imported successfully.")

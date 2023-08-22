from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Anime, Genre, Review, Rating
from .serializers import UserSerializer, AnimeSerializer, GenreSerializer, ReviewSerializer, RatingSerializer
from rest_framework import filters

from django.shortcuts import render

def anime_list(request):
    anime_list = Anime.objects.all()
    return render(request, 'anime_list.html', {'anime_list': anime_list})

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_year', 'title']  # Поля для сортировки

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre_id = self.request.query_params.get('genre_id')
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)
        return queryset


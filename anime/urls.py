from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AnimeViewSet, GenreViewSet, ReviewViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'anime', AnimeViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('anime/', AnimeViewSet.as_view({'get': 'list'}), name='anime-list'),
    
]
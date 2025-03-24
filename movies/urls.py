from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<uuid:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-vies'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]

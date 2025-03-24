from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<str:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]

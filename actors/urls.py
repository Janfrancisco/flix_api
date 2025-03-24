from django.urls import include, path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<str:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]

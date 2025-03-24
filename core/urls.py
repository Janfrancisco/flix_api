
from django.contrib import admin
from django.urls import include, path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView



#def hello_view(request):
#    return JsonResponse(
#        {'message': 'Hello, World!'}
#    )

urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    
]

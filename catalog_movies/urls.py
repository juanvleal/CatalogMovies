from django.contrib import admin
from django.urls import include, path

from movies.views import MoviesDetailListView, MoviesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('movies/', MoviesListView.as_view()),
    path('details/<int:movieId>/', MoviesDetailListView.as_view()),
]

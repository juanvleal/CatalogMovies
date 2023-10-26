from django.contrib import admin
from django.urls import include, path
from movies.views import MoviesDetailListView, MoviesListView, MoviesListViewPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', MoviesListView.as_view()),
    path('movies/', MoviesListView.as_view()),
    path('movies/<int:page>/', MoviesListViewPage.as_view()),
    path('details/<int:movieId>/', MoviesDetailListView.as_view(), name='movie_detail'),
]

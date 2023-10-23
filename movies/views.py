from django.views.generic import TemplateView
from movies.services.movies import Movies
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class MoviesListView(TemplateView):
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_movies = Movies().get_movies
        context.update({"movies":get_movies})
        return context
    
class MoviesDetailListView(TemplateView):
    template_name = "home/details.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_details_movie = Movies().get_details_movie(context['movieId'])
        context.update({"details_movie":get_details_movie})
        return context
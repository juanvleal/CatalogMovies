from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from movies.models import Comment
from movies.forms import CommentForm
from movies.services.movies import Movies
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class MoviesListView(TemplateView):
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_movies = Movies().get_movies(1)
        context.update({"movies":get_movies})
        return context
    
class MoviesListViewPage(TemplateView):
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_movies = Movies().get_movies(context['page'])
        context.update({"movies":get_movies})
        return context
    
@method_decorator(login_required, name='post')
class MoviesDetailListView(TemplateView):
    template_name = "home/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = context['movieId']

        get_details_movie = Movies().get_details_movie(movie_id)
        get_details_movie['release_date'] = datetime.strptime(get_details_movie['release_date'], "%Y-%m-%d").date()
        get_similar_movies = Movies().get_similar_movies(movie_id)
        get_comments = Comment.objects.filter(movieId=movie_id)
        
        context.update({
            "details_movie":get_details_movie,
            "similar_movies":get_similar_movies,
            "comments":get_comments,
            "comment_form":CommentForm()
        })
        return context
    
    def post(self, request, *args, **kwargs):
        movie_id = kwargs.get('movieId')
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movieId = movie_id
            comment.save()
            # Redirecionar para a mesma página após a postagem bem-sucedida
            return redirect(reverse('movie_detail', kwargs={'movieId': movie_id}) + '#comment')
        
        return self.get(request, *args, **kwargs)
    

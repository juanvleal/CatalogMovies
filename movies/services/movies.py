import requests
from decouple import config


class Movies:
    def _init_(self, *args, **kwargs):
        pass

    def get_headers(self):
        return {
            "accept": "application/json",
            "Authorization": config("TMDBToken"),
        }

    def get_movies(self, page):
        url = f"https://api.themoviedb.org/3/movie/popular?language=pt-BR&page={page}&include_adult=false"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if(response.status_code == 200):
            return response.json()
        else:
            return "erro"
        
    def get_details_movie(self, movieId):
        url = f"https://api.themoviedb.org/3/movie/{movieId}?language=pt-BR"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if(response.status_code == 200):
            return response.json()
        else:
            return "erro"
        
    def get_similar_movies(self, movieId):
        url = f"https://api.themoviedb.org/3/movie/{movieId}/similar?language=pt-BR"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if(response.status_code == 200):
            return response.json()
        else:
            return "erro"


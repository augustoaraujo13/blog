from django.views.generic import DetailView, ListView
from .models import Post

#Classe que cria uma lista de post
class PostListView(ListView):
    model = Post

#Classe que mostra um post.
class PostDetailView(DetailView):
    model = Post

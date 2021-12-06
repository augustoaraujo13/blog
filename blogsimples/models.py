from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    #Titulo do post.
    title = models.CharField(max_length=255)
    #Inserir uma imagem ao post
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    #Caminho da url do post.
    slug = models.SlugField(max_length=255, unique=True)
    #Cria um campo para associar o post a um autor.
    author = models.ForeignKey(User, on_delete= models.CASCADE)    
    #Corpo da postagem.
    body = models.TextField()
    #Adiciona automaticamente data e hora ao post, quando postado.
    created = models.DateTimeField(auto_now_add=True)
    #Quando haver atualização no post será mostrada.
    update = models.DateTimeField(auto_now=True)

#Metodo que mostra o titulo
    def __str__(self) -> str:
        return self.title

#Metodo que direnciona para uma url
    def get_absolute_url(self):
        return reverse("blogsimples:detail", kwargs={"slug": self.slug})
    
#Class que ordena a postagem para mais recente.
    class Meta:
        ordering = ("-created",)
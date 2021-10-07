from django.contrib import admin
from .models import Post
# Register your models here.

#Cria uma nova tabela, com isso permite a criação de posts
admin.site.register(Post)

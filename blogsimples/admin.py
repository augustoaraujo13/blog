from django.contrib import admin
from .models import Post
# Register your models here.

#Cria uma nova tabela, com isso permite a criação de posts
@admin.register(Post)

#Classe que cria um mim resumo sobre os posts
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    #Poupula o campo slug com o titulo automaticamente.
    prepopulated_fields = {"slug": ("title",)}

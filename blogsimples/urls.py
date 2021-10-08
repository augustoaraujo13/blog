from django.urls import path
from . import views

app_name = "blogsimples"

urlpatterns = [
    path("", views.PostListView.as_view(),name="List"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]
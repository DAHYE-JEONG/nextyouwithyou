from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create_post, name="create_post"),
    path('edit/<int:post_id>/', views.edit_post, name="edit_post"),
    path('delete/<int:post_id>/', views.delete_post, name="delete_post"),
    path('<int:post_id>/create/comment/', views.create_comment, name="create_comment"),
    path('<int:post_id>/delete/comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
]
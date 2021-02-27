from django.urls import path
from diary import views

app_name = 'diary'
urlpatterns = [
  path('', views.index, name='index'),
  path('createDiary/', views.createDiary, name='createDiary'),
  path('detail/<int:diary_id>/', views.detail, name='detail'),
  path('<int:diary_id>/delete', views.delete, name='delete'),
]


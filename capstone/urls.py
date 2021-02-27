"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from capstone.views import HomeView, UserCreateView, UserCreateDoneTV
import event.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/register/', UserCreateView.as_view(), name='register'), 
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('photo/', include('photo.urls')),
    path('blog/', include('blog.urls', namespace='post')),
    path('event/calendar', event.views.calendar_view, name="calendar"),
    path('event/new/', event.views.event, name="new"),
    path('event/edit/<int:event_id>', event.views.event, name="edit"),
    path('posts/', include('posts.urls')),
    path('todo/', include('todo.urls')),
    path('diary/', include('diary.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


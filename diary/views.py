from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CreateDiary
from django.urls import reverse
from .models import Diary

def index(request):
  diarys = Diary.objects.all()
  return render(request, 'diary/index.html', {'diarys': diarys})

def createDiary(request):
    if request.method == 'POST':
        form = CreateDiary(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('diary:index')
        else:
            return redirect('home')
    else:
        form = CreateDiary()
        return render(request, 'diary/createDiary.html', {'form': form})

def detail(request, diary_id):
  diary_detail = get_object_or_404(Diary, pk=diary_id)
  return render(request, 'diary/detail.html', {'diary_detail': diary_detail})

def delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return HttpResponseRedirect(reverse('diary:index'))  
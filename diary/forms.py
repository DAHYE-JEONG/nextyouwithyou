from django import forms
from .models import Diary
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CreateDiary(forms.ModelForm):
    class Meta:
      model = Diary
      fields = ['title', 'author', 'body']

      widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
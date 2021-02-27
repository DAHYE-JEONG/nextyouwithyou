from django import forms
from .models import Question
from .models import Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
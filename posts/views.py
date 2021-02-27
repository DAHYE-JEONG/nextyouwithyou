from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm
from .models import Question
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm


# Create your views here.
def index(request):
    posts = Question.objects.all()
    
    form = CommentForm()
    return render(request, 'posts/index.html', {'posts': posts, 'form': form})

def create_post(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   
            post.user = request.user
            post.save()
            return redirect('posts:index')    
        return redirect('posts:create_post')
    else:
        form = QuestionForm()
        title = '질문있어요'
        return render(request, 'posts/form.html', {'form': form, 'title': title})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Question, id=post_id)
    if post.user == request.user:
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
            return redirect('posts:edit_post')
        else:
            form = QuestionForm(instance=post)
            return render(request, 'posts/form.html', {'form': form})
    return redirect('posts:index')

@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Question, id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('posts:index')

@require_POST
@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Question, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:index')

@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:index')
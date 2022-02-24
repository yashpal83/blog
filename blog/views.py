from django.shortcuts import redirect, render, HttpResponse
from .models import Post, Comment
from django.contrib import messages

# Create your views here.

def home(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request, "blog/home.html", content)

def readingpost(request, num):
    post = Post.objects.get(num = num)
    comments = Comment.objects.filter(postnum = num)
    content = {'post': post, 'comments': comments}
    return render(request, "blog/blogpost.html", content)

def comments(request):
    if request.method == "POST":
        comment = request.POST['comment']
        postnum = request.POST['postnum']
        user = request.user
        post = Post.objects.get(num = postnum)
        savecomment = Comment(comment = comment, post = post, user = user, postnum = postnum)
        savecomment.save()
        messages.success(request, "Your comment has been posted successfully.")
    return redirect(f"/blog/readingpost/{postnum}")


def updatecomment(request):
    if request.method == "POST":
        updatedcomment = request.POST['updatedcomment']
        commentnum = request.POST['commentnum']
        postnum = request.POST['postnum']

    comment = Comment.objects.get(num = commentnum)
    comment.comment = updatedcomment
    comment.save()
    messages.success(request, "Your comment has been updated successfully.")
    return redirect(f"/blog/readingpost/{postnum}")


def deletecomment(request, num, pnum):
    comment = Comment.objects.get(num = num)
    comment.delete()
    messages.success(request, "Your comment has been deleted successfully.")
    return redirect(f"/blog/readingpost/{pnum}")
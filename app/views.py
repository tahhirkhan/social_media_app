from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render

from .models import Post, Category, Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import*
from django.contrib.auth.models import User
from app2.models import Profile

# Create your views here.


def home(request):
    all_posts = Post.objects.all().order_by("-date_created")
    
    
    
    context_dict = {
        'posts': all_posts,
        
    }
    return render(request, 'app/home.html', context_dict)


def categoryPosts(request, catgs):
    all_posts = Post.objects.filter(
        category=catgs).order_by("-date_created")

    context_dict = {
        'category': catgs,
        'posts': all_posts,
    }
    return render(request, 'app/categories.html', context_dict)



def likePost(request, likeid):
    post = Post.objects.get(id=likeid)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    post.save()
    return HttpResponseRedirect(reverse('viewPost', args=[str(likeid)]))


def addComment(request, pk):
    user_name = request.user.username
    post = Post.objects.get(id=pk)
    
    if request.method == 'POST':
        comment = request.POST['commentData']
        newComment = Comment(
            name = user_name,
            post = post,
            comment = comment,
        )
        newComment.save()
        print(user_name)
        print(comment)
        return redirect(reverse('allComments', args=[str(pk)]))
    return render(request, 'app/addComment.html')



@login_required(login_url='message')
def createPost(request):
    form = BlogForm()
    user = request.user

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            title_field = form.cleaned_data['title']
            category_field = form.cleaned_data['category']
            body_feild = form.cleaned_data['body']
            new_blog = Post(title=title_field, author=user,
                            category=category_field, body=body_feild)
            new_blog.save()
            return redirect('home')

    context_dict = {
        'form': form,
    }
    return render(request, 'app/add_post.html', context_dict)


@login_required(login_url='message')
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            name_field = form.cleaned_data['name']
            new_category = Category(name=name_field)
            new_category.save()
            return redirect('home')

    context_dict = {
        'form': form
    }

    return render(request, 'app/addCategory.html', context_dict)


def allCategories(request):
    all_posts = Post.objects.all()
    all_catgs = Category.objects.all()
    context_dict = {
        'posts': all_posts,
        'categories': all_catgs,
    }
    return render(request, 'app/all_categories.html', context_dict)


def viewPost(request, pk):
    post = Post.objects.get(id=pk)
    post_likes = post.likes.count()
    cmnt = post.name_rel.all().order_by('-date_added')
    
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    context_dict = {
        'posts': post,
        'post_likes': post_likes,
        'liked': liked,
        'comments': cmnt
    }

    return render(request, 'app/viewPost.html', context_dict)

def allComments(request, pk):
    post = Post.objects.get(id=pk)
    cmnt = post.name_rel.all().order_by('-date_added')
    context_dict = {
        'post': post,
        'comments': cmnt
    }
    return render(request, 'app/allComments.html', context_dict)


@login_required(login_url='message')
def editPost(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    form = BlogForm(instance=post)
    author = post.author

    if user == author:
        if request.method == "POST":
            form = BlogForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        return HttpResponse('You are not the correct user for this page to make changes!')

    context_dict = {
        'form': form,
    }
    return render(request, 'app/editPost.html', context_dict)


def index(request):
    return render(request, 'app/delete.html')


@login_required(login_url='message')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    post.delete()

    return redirect('usersPosts')


def message(request):
    return render(request, 'app2/message.html')

def usersPosts(request):
    myPosts = Post.objects.filter(author=request.user).order_by('-date_created')
    context_dict = {
        'myPosts': myPosts,
    }
    return render(request, 'app/usersPosts.html', context_dict)

def usersLikedPosts(request):
   
    l_posts = Post.objects.filter(likes=request.user).order_by('-date_created')

    context_dict = {
        'likedPosts': l_posts,
    }
    return render(request, 'app/usersLikedPosts.html', context_dict)

def commonProfilePafe(request, pk):
    randomUser = Profile.objects.get(id=pk)
    context_dict = {
        'randomUser': randomUser 
    }

    return render(request, 'app/commonProfilePage.html', context_dict)

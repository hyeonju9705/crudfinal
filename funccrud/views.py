from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment
from .forms import NewBlog, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# 페이지네이션을 위해서 추가
from django.core.paginator import Paginator

@login_required(login_url='/login/')
def del_comment(request, pk):
    print("hello")
    # comment = get_object_or_404(Comment, pk=pk)
    # comment.delete()
    return redirect('home')


def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'funccrud/add_comment.html', {'form': form})

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('home')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'funccrud/add_comment.html', {'form': form})


@login_required(login_url='/login/')
def delete(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    return redirect('home')

def welcome(request):
    return render(request, 'funccrud/index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'funccrud/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'funccrud/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'funccrud/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def read(request):
    # blogs = Blog.objects.all().order_by('-created_date', 'title')

    # 기존 플로그 조회 내용을 pagination용으로 변경 
    
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all().order_by('-created_date' , 'title')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request, 'funccrud/funccrud.html', {'blogs':blogs , 'posts' : posts})



@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'funccrud/new.html', {'form':form})

@login_required(login_url='/login/')
def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == "POST":
        form = NewBlog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
       form = NewBlog(instance=blog) 
    return render(request, 'funccrud/new.html', {'form':form})

# @login_required(login_url='/login/')
# def del_comment(request, pk):
#     blog = get_object_or_404(Blog, pk = pk)
#     blog.delete()
#     return redirect('home')

# @login_required(login_url='/login/')
# def delete(request, pk):
#     blog = get_object_or_404(Blog, pk = pk)
#     blog.delete()
#     return redirect('home')

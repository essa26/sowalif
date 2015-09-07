from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from main.forms import UserSignup, UserLogin, TagSearch, TagCreate, CreatePost, Comment_On
from main.models import Post, Comment, Tag
# Create your views here.


def post_list(request):
    context ={}
    posts = Post.objects.all()
    context['posts'] = posts

    return render(request, 'post_list.html', context)


def home(request):

    context = {}

    return render_to_response('home.html', context, context_instance=RequestContext(request))


def post_create(request):

    context = {}
    form = Create_Post()
    context['form'] = form
    if request.method == 'POST':
        form = Create_Post(request.POST)
        context['form'] = form
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author_id = form.cleaned_data['author']

            print author_id

            #author = User.objects.get(pk=author_id)

            form.author = author_id

            print form.author

            form.save()

            context['valid'] = "Post Created"
    elif request.method == 'GET':
        context['valid'] = form.errors

    return render_to_response('add_post.html', context, context_instance=RequestContext (request))


def tag_search(request):

    context = {}

    get = request.GET 
    post = request.POST

    context['get'] = get
    context['post'] = post

    form = TagSearch()
    context['form'] = form

    if request.method == "POST":
        form = TagSearch(request.POST)

        if form.is_valid():
            tag = form.cleaned_data['name']

            tags = Tag.objects.filter(name__startswith=tag)

            context['tags'] = tags
            context['valid'] = "The Form Was Valid"

        else:
            context['valid'] = form.errors
        
    elif request.method == "GET":
        context['method'] = 'The method was GET'

    return render_to_response('tag_search.html', context, context_instance=RequestContext(request))


def tag_create(request):

    context = {}

    if request.method == 'POST':
        form = TagCreate(request.POST)
        context["form"] = form

        if form.is_valid():
            form.save()

            context['valid'] = "is valid"

        else:
            context['valid'] = form.errors

    else:
        form = TagCreate()
        context['form'] = form

    return render_to_response('tag_create.html', context, context_instance=RequestContext(request))


def post_detail_view(request, pk):

    context = {}

    post = Post.objects.get(pk=pk)

    form = Comment_On

    context['form'] = form

    context['post'] = post

    if request.method == 'POST':
        form = Comment_On(request.POST)

        if form.is_valid():
            form.save()

            context['valid'] = "Comment Added"
    elif request.method == 'GET':
        context['valid'] = form.errors

    return render_to_response('post_detail.html', context, context_instance=RequestContext(request))


def index(request):
    context = {'form': UserSignup()}

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def signup_view(request):

    context = {}

    form = UserSignup()
    context['form'] = form
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = "no@email.com"

            try:
                User.objects.create_user(name, email, password)
                context['valid'] = "Thank you for signing up!"
                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/')
            except IntegrityError, e:
                context['valid'] = "A user with that name is already taken. Please try again."

        else:
            context['valid'] = form.errors
    context['signup'] = UserSignup()

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

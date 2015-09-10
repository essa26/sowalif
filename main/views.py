from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from main.forms import UserSignup, UserLogin,  CreatePost, CommentOn, TagSearch#, TagCreate,
from main.models import Post, Comment, UserProfile
# Create your views here.


def date_list(request):
    context ={}
    posts = Post.objects.all().order_by('-date_created')
    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)


def home(request):

    context = {}

    posts = Post.objects.all().order_by('-date_created')

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('home.html', context, context_instance=RequestContext(request))


def post_create(request):

    context = {}
    form = CreatePost()
    context['form'] = form
    if request.method == 'POST':
        form = CreatePost(request.POST)
        context['form'] = form
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author_id = request.POST['author']
            tags = form.cleaned_data['tags']

            new_obj = Post()

            #author = User.objects.get(pk=author_id)

            new_obj.author = User.objects.get(pk=author_id)
            new_obj.title = title
            new_obj.text = text

            new_obj.save()

            for tag in tags:
                new_obj.tags.add(tag)

            new_obj.save()

            context['valid'] = "Post Created"

            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        context['valid'] = form.errors

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('add_post.html', context, context_instance=RequestContext (request))


def tag_search(request, tag=""):

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

            posts = Post.objects.filter(tags__name__icontains=tag)

            context['posts'] = posts
            context['valid'] = "The Form Was Valid"

        else:
            context['valid'] = form.errors

    elif request.method == "GET":
        posts = Post.objects.filter(tags__name__icontains=tag)

        context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('tag_search.html', context, context_instance=RequestContext(request))


# def tag_create(request):
#
#     context = {}
#
#     if request.method == 'POST':
#         form = TagCreate(request.POST)
#         context["form"] = form
#
#         if form.is_valid():
#             form.save()
#
#             context['valid'] = "is valid"
#
#         else:
#             context['valid'] = form.errors
#
#     else:
#         form = TagCreate()
#         context['form'] = form
#
#     return render_to_response('tag_create.html', context, context_instance=RequestContext(request))


def post_detail_view(request, pk):

    context = {}

    post = Post.objects.get(pk=pk)

    tags = post.tags.all()

    context['tags'] = tags

    form = CommentOn

    context['form'] = form

    context['post'] = post

    if request.method == 'POST':
        form = CommentOn(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            author_id = request.POST['author']
            posted_on = request.POST['posted_on']

            new_obj = Comment()

            new_obj.text = text
            new_obj.author = User.objects.get(pk=author_id)
            new_obj.posted_on = Post.objects.get(pk=posted_on)

            new_obj.save()

            context['valid'] = "Comment Added"
    elif request.method == 'GET':
        context['valid'] = form.errors

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('post_detail.html', context, context_instance=RequestContext(request))


def index(request):

    context = {}
    context['form'] = UserSignup()
    context['login_form'] = UserLogin()

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags
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
                user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank you for signing up!"
                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                userprof, created = UserProfile.objects.get_or_create(user=user)

                return HttpResponseRedirect('/')
            except IntegrityError, e:
                context['valid'] = "A user with that name is already taken. Please try again."

        else:
            context['valid'] = form.errors
    context['signup'] = UserSignup()

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags
    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
        if auth_user.is_active:
            login(request, auth_user)
            context['valid'] = "Login Successful"

            return HttpResponseRedirect('/')
        else:
            context['valid'] = "Invalid User"
    else:
        context['valid'] = "Please enter a User"

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags
    return render_to_response('login.html', context, context_instance=RequestContext(request))


def user_detail_add(request):

    context = {}

    if request.method == 'POST':
        tag = request.POST.get('tag')
        user = request.user
        userprof = UserProfile.objects.get(user=user)
        userprof.tags.add(tag)

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('user_detail_add.html', {}, context_instance=RequestContext(request))


def user_tags_view(request):
    user = request.user
    userprof = UserProfile.objects.get(user=user)
    user_tags = userprof.tags.all()
    context = {}
    context['user_tags'] = user_tags

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags
    return render_to_response('user_detail.html', context, context_instance=RequestContext(request))

def hometest(request):

    context = {}

    posts = Post.objects.all().order_by('-date_created')

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('hometest.html', context, context_instance=RequestContext(request))

def vote(request, pk):

    if request.user.is_authenticated():

        user = User.objects.get(pk=request.user.pk)

    else:

        user = User.objects.get(pk=88)

    vote_type = request.GET.get('vote_type', None)

    post = Post.objects.get(pk=pk)


    print post
    print user
    if vote_type == 'up':
        print post.down_votes
        post.up_votes.add(user)

        try:
            post.down_votes.get(pk=request.user.pk)
            post.down_votes.remove(user)
        except Exception, e:
            print 'e'

    if vote_type == 'down':
        post.down_votes.add(user)

        try:
            post.up_votes.get(pk=request.user.pk)
            post.up_votes.remove(user)
        except Exception, e:
            print 'e'

    return HttpResponseRedirect('/post_list/')


def popular_list(request):
    context ={}
    posts = Post.objects.all().order_by('-up_votes')
    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)

def unpopular_list(request):
    context ={}
    posts = Post.objects.all().order_by('-down_votes')
    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)




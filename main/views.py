from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
# , TagCreate,
from main.forms import UserSignup, UserLogin,  CreatePost, CommentOn, TagSearch
from main.models import Post, Comment, UserProfile
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.


def home(request):

    posts = Post.objects.all().order_by('-date_created')

    paginator = Paginator(posts, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except Exception, e:
        page = 1

    try:

        posts = paginator.page(page)

    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    context = {}

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('home.html', context, context_instance=RequestContext(request))


def date_list(request):
    posts = Post.objects.all().order_by('-date_created')

    paginator = Paginator(posts, 16)

    try:
        page = int(request.GET.get('page', '1'))
    except Exception, e:
        page = 1

    try:

        posts = paginator.page(page)

    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    context = {}

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)


def popular_list(request):
    posts = Post.objects.all().order_by('-up_votes')

    paginator = Paginator(posts, 16)

    try:
        page = int(request.GET.get('page', '1'))
    except Exception, e:
        page = 1

    try:

        posts = paginator.page(page)

    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    context = {}

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)


def unpopular_list(request):
    posts = Post.objects.all().order_by('-down_votes')

    paginator = Paginator(posts, 16)

    try:
        page = int(request.GET.get('page', '1'))
    except Exception, e:
        page = 1

    try:

        posts = paginator.page(page)

    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    context = {}

    context['posts'] = posts

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render(request, 'post_list.html', context)


def post_create(request):

    context = {}

    if request.user.is_authenticated():
        form = CreatePost(initial={'author': request.user.pk})
    else:
        form = CreatePost(initial={'author': '88'})

    context['form'] = form



    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            context['form'] = form
            print form.cleaned_data
            print "3"
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author_id = request.POST['author']
            image = form.cleaned_data['image']
            tags = form.cleaned_data['tags']

            print "image thing"
            print image

            new_obj = Post()


            new_obj.author = User.objects.get(pk=author_id)
            new_obj.title = title
            new_obj.text = text
            new_obj.image = image

            new_obj.save()

            for tag in tags:
                new_obj.tags.add(tag)

            new_obj.save()

            context['valid'] = "Post Created"

            return HttpResponseRedirect('/')
        else:
            context['form'] = form
    elif request.method == 'GET':
        context['valid'] = form.errors

    if request.user.is_authenticated():

        user = User.objects.get(pk=request.user.pk)

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('add_post.html', context, context_instance=RequestContext(request))


def tag_search(request):

    context = {}

    get = request.GET
    post = request.POST

    context['get'] = get
    context['post'] = post

    form = TagSearch()
    context['form'] = form

    if request.method == "GET":
        form = TagSearch(request.GET)

        if form.is_valid():
            tag = form.cleaned_data['name']

            print tag

            posts = Post.objects.filter(tags__name__icontains=tag)

            context['posts'] = posts
            context['valid'] = "The Form Was Valid"

        else:
            context['valid'] = form.errors


    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('tag_search.html', context, context_instance=RequestContext(request))


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

                userprof, created = UserProfile.objects.get_or_create(
                    user=user)

                return HttpResponseRedirect('/')
            except IntegrityError, e:
                context[
                    'valid'] = "A user with that name is already taken. Please try again."

        else:
            context['valid'] = form.errors
    context['signup'] = UserSignup()

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags
    return render_to_response('signup.html', context, context_instance=RequestContext(request))


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


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


def upvote(request):
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.pk)
        postpk = request.GET.get('postpk', None)
        post = Post.objects.get(pk=postpk)
        post.up_votes.add(user)
        try:
            post.down_votes.get(pk=request.user.pk)
            post.down_votes.remove(user)
        except Exception, e:
            print 'e'


    return HttpResponse(['%s' % post.up_votes.count(),'%s' % post.down_votes.count()])

def downvote(request):
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.pk)
        postpk = request.GET.get('postpk', None)
        post = Post.objects.get(pk=postpk)
        post.down_votes.add(user)
        try:
            post.up_votes.get(pk=request.user.pk)
            post.up_votes.remove(user)
        except Exception, e:
            print 'e'

    return HttpResponse(['%s' % post.up_votes.count(),'%s' % post.down_votes.count()])

def handler404(request):

    context = {}

    response = render_to_response('404.html', context,
                                  context_instance=RequestContext(request))
    response.status_code = 404

    context['response'] = response
    return response


def handler500(request):

    context = {}

    response = render_to_response('500.html', context,
                                  context_instance=RequestContext(request))
    context['response'] = response

    response.status_code = 500
    return response


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


def about(request):

    context = {}

    if request.user.is_authenticated():

        user = request.user

        userprof = UserProfile.objects.get(user=user)

        home_tags = userprof.tags.all()

        context['home_tags'] = home_tags

    return render_to_response('about.html', context, context_instance=RequestContext(request))

# def index(request):
#
#     context = {}
#     context['form'] = UserSignup()
#     context['login_form'] = UserLogin()
#
#     if request.user.is_authenticated():
#
#         user = request.user
#
#         userprof = UserProfile.objects.get(user=user)
#
#         home_tags = userprof.tags.all()
#
#         context['home_tags'] = home_tags
#     return render_to_response('signup.html', context, context_instance=RequestContext(request))
#
#

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

# def vote(request, pk):
#
#     context = {}
#
#     redirect_to = request.REQUEST.get('next', '')
#
#
#     if request.user.is_authenticated():
#
#         user = User.objects.get(pk=request.user.pk)
#
#     # else:
#     #
#     #     user = User.objects.get(pk=88)
#
#     vote_type = request.GET.get('vote_type', None)
#
#     post = Post.objects.get(pk=pk)
#
#
#     print post
#     print user
#     if vote_type == 'up':
#         print post.down_votes
#         post.up_votes.add(user)
#
#         try:
#             post.down_votes.get(pk=request.user.pk)
#             post.down_votes.remove(user)
#         except Exception, e:
#             print 'e'
#         return HttpResponseRedirect(redirect_to)
#
#     if vote_type == 'down':
#         post.down_votes.add(user)
#
#         try:
#             post.up_votes.get(pk=request.user.pk)
#             post.up_votes.remove(user)
#         except Exception, e:
#             print 'e'
#
#         return HttpResponseRedirect(redirect_to)
#
#     return render_to_response('vote.html', context, context_instance=RequestContext(request))

# return render_to_response('tag_create.html', context,
# context_instance=RequestContext(request))

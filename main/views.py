from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.forms import UserSignup, UserLogin

# Create your views here.
from main.models import Post




def post_create(request):





def post_detail_view(request, pk):

    context = {}

    posts = Post.objects.get(pk=pk)

    context['posts'] = posts


    return render_


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

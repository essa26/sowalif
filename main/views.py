from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.forms import UserSignup, UserLogin

# Create your views here.
from main.models import UserProfile, Tag


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
                user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank you for signing up!"
                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                userprof, created = UserProfile.objects.get_or_create(user=user)

                return HttpResponseRedirect('/')
            except IntegrityError, e:
                print e
                context['valid'] = "A user with that name is already taken. Please try again."

        else:
            context['valid'] = form.errors
    context['signup'] = UserSignup()

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_tag(request):
    tag_name = request.POST.get('tag')
    tag, created = Tag.objects.get_or_create(name=tag_name)
    userprof, created = UserProfile.objects.get_or_create(user=request.user)
    userprof.tag.add(tag)
    userprof.save()

    context = {}
    context['list'] = []

    for tag in userprof.tag.all():
        context['list'].append(tag)

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


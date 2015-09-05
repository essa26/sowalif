from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.backends.mysql.base import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.forms import UserSignup, UserLogin

# Create your views here.


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

            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            try:
                User.objects.create_user(name, password)
                context['valid'] = "Thank you for signing up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/')
            except IntegrityError, e:
                context['valid'] = "A user with that name is already taken. Please try again."

        else:
            context['valid'] = form.errors
    context['signup'] = UserSignup()

    return render_to_response('index.html', context, context_instance=RequestContext(request))

from django.shortcuts import render

# Create your views here.
from main.models import Post




def post_create(request):





def post_detail_view(request, pk):

    context = {}

    posts = Post.objects.get(pk=pk)

    context['posts'] = posts


    return render_
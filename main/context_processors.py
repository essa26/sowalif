from main.models import Post
from main.forms import CreatePost


def main_menu(request):

    postform = CreatePost

    context['postform'] = postform

    return {'postform': postform}



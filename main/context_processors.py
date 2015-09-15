from main.models import Post
from main.forms import CreatePost


def main_menu(request):

    context = {}

    postform = CreatePost

    context['postform'] = postform

    return {'postform': postform}



"""sowalif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index'),
    url(r'^home/$', 'main.views.home'),
    url(r'^signup/$', 'main.views.signup_view'),
    url(r'^login/$', 'main.views.login_view'),
    url(r'^logout/$', 'main.views.logout_view'),

    url(r'^post_detail/(?P<pk>\w+)/$', 'main.views.post_detail_view'),
    url(r'^post_create/$', 'main.views.post_create'),
    url(r'^post_list/$', 'main.views.post_list'),
    url(r'^tag_search/$', 'main.views.tag_search'),
<<<<<<< HEAD
=======
    #url(r'^tag_create/$', 'main.views.tag_create'),
    url(r'^user_detail/$', 'main.views.user_detail'),
    url(r'^user_detail_add/$', 'main.views.user_detail_add'),
>>>>>>> 8eaaa440ed4f6b52ac83cae894e5cec5a1405147
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

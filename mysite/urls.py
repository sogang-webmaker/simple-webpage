from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    url(r'^signup/$','blog.views.signup',name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    #모든 요청을 블로그 url로
]

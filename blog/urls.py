from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views
import django

urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$',views.show,name='show'),
    url(r'^signup_ok/$',views.signup_ok,name='signup_ok'),
    url(r'^$',views.post_list, name='post_list'),
    
    url(r'^login/$',auth_views.login,name='login_url',kwargs={'template_name':'blog/login.html'}),
    #url(r'^logout/$',auth_views.logout,{'next_page':'/login/'},name='logout_url'),
]
from django.shortcuts import render
from .models import Post

#
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
#

#from django.utils import timezone

# Create your views here.

def signup_ok(request):
	return render(request,'blog/signup_ok.html',{})

def show(request,pk):
	post = Post.objects.get(pk=pk)
	return render(request,'blog/show.html',{'post':post})

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts':posts})

def signup(request):
	if request.method == "POST":
		userform = UserCreationForm(request.POST)
		if userform.is_valid():
			userform.save()

			return HttpResponseRedirect(
                reverse("signup_ok")
			)
	elif request.method == "GET":
	    userform = UserCreationForm()

	return render(request,"blog/signup.html",{"userform":userform,})
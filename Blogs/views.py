from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponseRedirect(reverse('blogapp:blog_list'))

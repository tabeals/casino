# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django import template
import random
from django.views.generic.base import View
from django.views.generic.base import TemplateView

register = template.Library
# but you can do it with the httpResponse as well.
#the main way to strucure view is with the render method which takes 3 args.
#functinon based views. they accept three params the request object,
# a template and context in term of a template called a dictionary
#they way that django handles urls and remembers who you are and what you do
#is with the request respoonse objects.

def home(request):

    some_list = [
        random.randint(0,10000000000),
        random.randint(0,100000000000),
        random.randint(0, 100000000000)
                 ]
    html_ = '''A*
   '''
    condition_bool_item= True
    if condition_bool_item:
        num = random.randint(0, 10000000)
    context = {
        "num": num,
        "some_list": some_list,
        "html_": html_
    }
    return render(request, "home.html", context)
class HomeView(TemplateView):
    template_name = 'home.html'


def about(request):
    context = {

    }
    return render(request, "about.html", context)
class AboutView(TemplateView):
    template_name = 'about.html'


def contact(request):
    context = {

    }
    return render(request, "contact.html", context)


class ContactView(TemplateView):
    template_name = 'contact.html'

    # def post(self, request, *args, **kwargs):
    #    context = {}
    #    return render(request, "contact.html", context)
    # def put(self, request, *args, **kwargs):
    #    context = {}
    #    return render(request, "contact.html", context)
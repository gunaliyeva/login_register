import imp
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'
    


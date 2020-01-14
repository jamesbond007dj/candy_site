from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class TwixPageView(TemplateView):
    template_name = 'twix.html'


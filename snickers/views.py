from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class SnickersPageView(TemplateView):
    template_name = 'snickers.html'


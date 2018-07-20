from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class DatasetPageView(TemplateView):
    template_name = 'dataset.html'


class TargetPageView(TemplateView):
    template_name = 'target_model.html'


class AccuracyPageView(TemplateView):
    template_name = 'accuracy.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
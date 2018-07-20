from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import TemplateView


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'home.html',
        context={
                 'num_visits': num_visits},
    )


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
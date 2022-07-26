from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Thing
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

class ThingsListView(ListView):
    template_name = 'thing_list.html'
    model = Thing
    context_object_name = 'things'
class ThingsDetailView(DetailView):
    template_name = 'thing_detail.html'
    model = Thing

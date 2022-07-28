from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Thing
# Create your views here.
class ThingListView(ListView):
    template_name = 'things_list.html'
    model = Thing
    context_object_name = 'things'

class ThingDetailView(DetailView):
    template_name = 'thing_detail.html'
    model = Thing

class ThingCreateView(CreateView):
    template_name = 'thing_create.html'
    model = Thing
    fields = ['name', 'rank', 'reviewer']

class ThingUpdateView(UpdateView):
    template_name = 'thing_update.html'
    model = Thing
    fields = ['name', 'rank', 'reviewer']

class ThingDeleteView(DeleteView):
    template_name = 'thing_delete.html'
    model = Thing
    success_url = reverse_lazy('things_list')

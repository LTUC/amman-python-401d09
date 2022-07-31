from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Thing


class ThingListView(ListView):
    template_name = "pages/thing-list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "pages/thing-detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "pages/thing-create.html"
    model = Thing
    fields = []


class ThingUpdateView(UpdateView):
    template_name = "pages/thing-update.html"
    model = Thing
    fields = []


class ThingDeleteView(DeleteView):
    template_name = "pages/thing-delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")
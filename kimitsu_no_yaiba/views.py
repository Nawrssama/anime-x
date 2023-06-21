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
from .models import kimitsu


class kimitsuListView(ListView):
    template_name = "k/kimitsu-list.html"
    model = kimitsu
    context_object_name = "Anime"


class kimitsuDetailView(DetailView):
    template_name = "k/kimitsu-detail.html"
    model = kimitsu


class kimitsuCreateView(CreateView):
    template_name = "k/kimitsu-create.html"
    model = kimitsu
    fields = '__all__'


class kimitsuUpdateView(UpdateView):
    template_name = "k/kimitsu-update.html"
    model = kimitsu
    fields = '__all__'
    success_url = reverse_lazy("kimitsu_list")


class kimitsuDeleteView(DeleteView):
    template_name = "k/kimitsu-delete.html"
    model = kimitsu
    success_url = reverse_lazy("kimitsu_list")
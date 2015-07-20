from django.shortcuts import render
from django.views import generic
from . import models

class BlogIndexView(generic.ListView):
    model = models.Entry
    template_name = "index.html"
    paginate_by = 2

class EntryListView(generic.ListView):
    model = models.Entry
    template_name = "entry_list.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"


class EntryDetailView(generic.DetailView):
    model = models.Entry
    template_name = "entry_detail.html"

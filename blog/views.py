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


class TagFilterView(generic.ListView,slug):
    entries = models.Entry.objects.all()
    queryset=[entry for entry in entries if entry.tags.filter(tag=slug)]
    template_name = "tag_filter.html"
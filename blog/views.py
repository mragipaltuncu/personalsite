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

class EntryArchiveView(generic.dates.ArchiveIndexView):
    model = models.Entry
    date_field = "created"
    template_name = "entry_archive.html"
    def years(self):
        date_time_list = models.Entry.objects.all().datetimes('created','year')
        years = [date.year for date in date_time_list ]
        return years

"""

experimenting to create a view which would take a tag from the url and filter objects to
show them in a listview

class TagFilterView(generic.ListView,slug=None):
    entries = models.Entry.objects.all()
    queryset=[entry for entry in entries if entry.tags.filter(tag=None)]
    template_name = "tag_filter.html"
"""
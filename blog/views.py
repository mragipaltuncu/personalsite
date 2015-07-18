from django.shortcuts import render
from django.views import generic
from . import models

class BlogIndexView(generic.ListView):
    model = models.Entry
    template_name = "index.html"
    paginate_by = 2


def index(request):
    entry = models.Entry.objects.order_by('created').last()
    return render(request,'index.html', {
        'entry':entry
        })
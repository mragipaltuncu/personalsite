from django.shortcuts import render
from django.views import generic
from blog import models

class BlogIndexView(generic.TemplateView):
    model = models.Entry
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogIndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['entry'] = models.Entry.objects.order_by('created').last()
        return context

def index(request):
    entry = models.Entry.objects.order_by('created').last()
    return render(request,'index.html', {
        'entry':entry
        })
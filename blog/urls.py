from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.BlogIndexView.as_view(),
        name="index"),
    url(r'^about/$',
        views.AboutView.as_view(),
        name="about"),
    url(r'^blog/entry_detail/(?P<slug>[-\w]+)/$',
        views.EntryDetailView.as_view(),
        name="entry_detail"),
    url(r'^blog/archive/$',
        views.EntryArchiveView.as_view(),
        name="entry_archive"),
    ]
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^',include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include('django_markdown.urls')),
]

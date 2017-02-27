from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^apply/$', apply, name="apply"),
    url(r'^allocate/$', house_list, name="allocate"),
]


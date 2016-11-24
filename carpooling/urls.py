from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from django.views.generic import TemplateView

app_name = 'carpooling'
urlpatterns = [
    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    url(r'^ride/$',TemplateView.as_view(template_name='carpooling/startride.html'),name="success"),
    url(r'^register/$', views.register),
    url(r'^success/$', views.register_success),
]
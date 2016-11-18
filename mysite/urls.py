from django.conf.urls import include, url
from django.contrib import admin
from carpooling import views 
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='home'),
	url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^polls/', include('polls.urls')),
    url(r'^carpooling/', include('carpooling.urls')),
    url(r'^login/$', login, {'template_name': 'carpooling/login.html'},name='django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
]

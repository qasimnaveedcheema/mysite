
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView

from django.http import Http404
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from models import Registration
from forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndexView(generic.TemplateView):
    template_name = 'carpooling/index.html'
    context_object_name = 'qlist'
    
    
    
class HomeView(CreateView):
    template_name = 'carpooling/home.html'
    model = Registration
    fields = ['first_name','last_name','email','phone','date','time']
    success_url = '/carpooling/ride/'
    
 
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/carpooling/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'carpooling/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'carpooling/success.html',
    )
    
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
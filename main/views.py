from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from main.forms import RegisterForm


# Create your views here.
def index(request):
    data = {'title':'Главная страница' }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
def maps(request):
    return render(request, 'main/maps.html')
def languages(request):
    return render(request, 'main/maps/languages.html')
def track(request):
    return render(request, 'main/maps/track.html')
def maps_other(request):
    return render(request, 'main/maps/other.html')
@login_required
def profile_view(request):
    return render(request, 'main/profile/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


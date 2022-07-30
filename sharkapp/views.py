from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Shark, Sighting
from .forms import SightingForm


class SharkCreate(LoginRequiredMixin, CreateView):
    model = Shark
    fields = ['species', 'image', 'length', 'weight', 'top_speed', 'preferred_prey']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/sharks/'

class SharkUpdate(LoginRequiredMixin, UpdateView):
    model = Shark
    fields = ['length', 'weight', 'top_speed', 'preferred_prey']

class SharkDelete(LoginRequiredMixin, DeleteView):
    model = Shark
    success_url = '/sharks/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def sharks_index(request):
    sharks = Shark.objects.filter(user = request.user)

    return render(request, 'sharks/index.html', {'sharks': sharks})

@login_required
def shark_detail(request, shark_id):
    shark = Shark.objects.get(id=shark_id)
    sightings_not_assigned = Sighting.objects.exclude(id__in = shark.sightings.all().values_list('id'))
    return render(request, 'sharks/detail.html', {'shark': shark, 'sightings': sightings_not_assigned})


class SightingList(LoginRequiredMixin, ListView):
    model = Sighting

class SightingDetail(LoginRequiredMixin, DetailView):
    model = Sighting

class SightingCreate(LoginRequiredMixin, CreateView):
    model = Sighting
    fields = '__all__'

class SightingUpdate(LoginRequiredMixin, UpdateView):
    model = Sighting
    fields = '__all__'

class SightingDelete(LoginRequiredMixin, DeleteView):
    model = Sighting
    success_url = '/sightings/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Couldn't sign you up - Please try again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# def add_sighting(request, shark_id):
#     form = SightingForm(request.POST)
#     if form.is_valid():
#         new_sighting = form.save(commit=False)
#         new_sighting.shark_id = shark_id
#         new_sighting.save()

#     return redirect('detail', shark_id = shark_id)

@login_required
def assoc_sighting(request, shark_id, sighting_id):
    Shark.objects.get(id=shark_id).sightings.add(sighting_id)
    return redirect('detail', shark_id = shark_id)
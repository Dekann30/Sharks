from re import U
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shark


class SharkCreate(CreateView):
    model = Shark
    fields = '__all__'
    success_url = '/sharks/'

class SharkUpdate(UpdateView):
    model = Shark
    fields = ['length', 'weight', 'top_speed', 'preferred_prey']

class SharkDelete(DeleteView):
    model = Shark
    success_url = '/sharks/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sharks_index(request):
    sharks = Shark.objects.all()
    return render(request, 'sharks/index.html', {'sharks': sharks})

def shark_detail(request, shark_id):
    shark = Shark.objects.get(id=shark_id)
    return render(request, 'sharks/detail.html', {'shark': shark })
from django.shortcuts import render
from .forms import SubscribersFrom

# Create your views here.
def landing(request):
    name = "Jackal"
    current_day = "30.05.17"
    form = SubscribersFrom(request.POST or None)
    return render(request, 'landing/landing.html', locals())
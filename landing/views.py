from django.shortcuts import render
from .forms import SubscriberFrom

# Create your views here.
def landing(request):
    name = "Jackal"
    current_day = "30.05.17"
    form = SubscriberFrom(request.POST or None)

    if request.method =="POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
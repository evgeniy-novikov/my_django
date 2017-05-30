from django import forms
from .models import *

class SubscribersFrom(forms.ModelForm):

    class Meta:
        model = Subscribers
        exclude = [""]
from .models import *
from django.forms import ModelForm


class ApplicantForm(ModelForm):
    class Meta:
        model = Occupant
        fields =  '__all__'

from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *

def house_list(request):
    house_wai = House.objects.filter(status='WAI')
    house_ala = House.objects.filter(status='ALA')
    house_dea = House.objects.filter(status='DEA')
    users = Occupant.objects.all()
    
    return render(request, 'allocate.html', {'house_wai': house_wai, 'house_dea': house_dea, 'house_ala': house_ala, 'users': users })


def apply(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ApplicantForm()
    return render(request, 'apply.html', {'form': form})


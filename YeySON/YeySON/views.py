from django.shortcuts import render
from django.utils import timezone

from YeySON.forms import CommitteeForm, ContactForm
from YeySON.models import Committee, Contact

def home(request):
    if request.method == 'POST':
        if "fname-1" in request.POST:
            Committee.objects.create(title=request.POST["fname-1"])
        elif "fname-2" in request.POST:
            Contact.objects.create(committee=request.POST["committees"], name=request.POST["fname-2"], position=request.POST["fname-3"], mail=request.POST["fname-4"])

    return render(request, 'base.html')
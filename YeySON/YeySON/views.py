from django.shortcuts import render
from django.utils import timezone

from YeySON.models import Committee, Contact, Post, Page

def home(request):
    all_committees = Committee.objects.all()
    all_contacts = Contact.objects.all()
    context = {
        'committees': all_committees,
        'contacts': all_contacts
    }

    if request.method == 'POST':
        if "fname-1" in request.POST:
            Committee.objects.create(title=request.POST["fname-1"])
        elif "fname-2" in request.POST:
            Contact.objects.create(committee=request.POST["committees"], name=request.POST["fname-2"], position=request.POST["fname-3"], mail=request.POST["fname-4"])
        elif "fname-5" in request.POST:
            Page.objects.create(title=request.POST["fname-5"], path=request.POST["fname-6"], content=request.POST["area-1"])
        elif "fname-7" in request.POST:
            Post.objects.create(title=request.POST["fname-7"], date=request.POST["post-date"], content=request.POST["area-2"])

    return render(request, 'base.html', context)
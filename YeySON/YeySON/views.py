from django.shortcuts import render
from django.utils import timezone

from YeySON.models import Committee, Contact, Post, Page
from YeySON.serializers import PostSerializer

from rest_framework import generics

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


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

    return render(request, 'base.html', context)


def posts(request):
    all_posts = Post.objects.all()

    context = {
        'posts': all_posts
    }

    if request.method == 'POST':
        if "fname-7" in request.POST:
            Post.objects.create(title=request.POST["fname-7"], date=request.POST["post-date"], content=request.POST["area-2"])

    return render(request, 'posts.html', context)


def pages(request):
    all_pages = Page.objects.all()

    context = {
        'pages': all_pages
    }

    if request.method == 'POST':
        if "fname-5" in request.POST:
            Page.objects.create(title=request.POST["fname-5"], path=request.POST["fname-6"], content=request.POST["area-1"])

    return render(request, 'pages.html', context)


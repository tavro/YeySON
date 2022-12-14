"""YeySON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from YeySON.views import home, posts, pages, PostListCreate, PageListCreate, CommitteeListCreate, ContactListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('posts/', posts),
    path('pages/', pages),
    path('api/posts/', PostListCreate.as_view()),
    path('api/pages/', PageListCreate.as_view()),
    path('api/committees/', CommitteeListCreate.as_view()),
    path('api/contacts/', ContactListCreate.as_view())
]

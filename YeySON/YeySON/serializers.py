from rest_framework import serializers
from YeySON.models import Post, Page, Contact, Committee


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'date', 'content')


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'path', 'content')


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = ('id', 'title')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('committee', 'name', 'position', 'mail')
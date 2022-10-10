from django.contrib import admin

from YeySON.models import Committee, Contact, Post, Page


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'committee', 'name', 'position', 'mail']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'content']


class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'path', 'content']


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
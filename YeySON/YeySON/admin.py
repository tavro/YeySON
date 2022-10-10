from django.contrib import admin

from YeySON.models import Committee, Contact

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'committee', 'name', 'position', 'mail']

admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Contact, ContactAdmin)
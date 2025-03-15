from django.contrib import admin

from .models import Contact, Project, Video, Partner 

admin.site.register(Project)
admin.site.register(Video)
admin.site.register(Partner)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_at','updated_at']
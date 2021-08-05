from django.contrib import admin

from .models import*

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_filter =('title', 'slug')
    prepopulated_fields={'slug':[('slug')]}

# Register your models here.

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
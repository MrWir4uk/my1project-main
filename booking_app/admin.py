from django.contrib import admin

# Register your models here.
from .models import Room
from .models import Booking


class BookiAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'persons', 'phone_number', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')


admin.site.register(Room)
admin.site.register(Booking, BookiAdmin)

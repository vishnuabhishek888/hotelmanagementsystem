from django.contrib import admin
from .models import Category, Room, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'category')
    list_filter = ('category',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_date', 'end_date', 'guest_name')
    list_filter = ('room', 'start_date', 'end_date')

admin.site.site_header = "Hotel Management System"
admin.site.site_title = "Hotel Management System"

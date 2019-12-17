from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_filter = ('title', 'realtor')
    search_fields = ('title', 'city', 'state', 'zipcode')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 6


admin.site.register(Listing, ListingAdmin)

from django.contrib import admin

from .models import Mountain, Climber

# Register your models here.
#class MountainAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Mountain Details', {'fields': ['mountain_name', 'mountain_height', 'mountain_range']}),
#        ('Climb Details', {'fields': []}),
#    ]

#    list_display = ('mountain_name', 'mountain_height', 'mountain_range',)

#    search_fields = ['mountain_name']
#admin.site.register(Mountain, MountainAdmin)


# Testing
admin.site.register(Mountain)
admin.site.register(Climber)
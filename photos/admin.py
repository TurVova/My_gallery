from django.contrib import admin
from photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "create"]
    
    class Meta:
        model = Photo
        
admin.site.register(Photo, PhotoAdmin)

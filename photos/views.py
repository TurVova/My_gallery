from django.shortcuts import render
from photos.models import Photo

def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos":queryset,
    }
    return  render(request, "photo.html", context)

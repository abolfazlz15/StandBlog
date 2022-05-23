from django.shortcuts import render
from .models import AboutUs, SocialMedia


def aboutUs(request):
    aboutus = AboutUs.objects.all().last()
    social_media = SocialMedia.objects.last()

    context = {
        'aboutus': aboutus,
        'social_media': social_media,
    }
    return render(request, 'aboutus/about.html', context)

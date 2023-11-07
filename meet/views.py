from django.shortcuts import render
from django.conf import settings

from .models import Header, Menu, SocialMenu

# Create your views here.
def meet(request):

    header = Header.objects.all()
    menu = Menu.objects.all()
    social = SocialMenu.objects.all()

    google_tag_url = settings.MEASUREMENT_ID
    measurement_id = settings.GOOGLE_TAG_URL

    context = {
        'header':header,
        'menu':menu,  
        'social':social,
        'google_tag_url':google_tag_url,
        'measurement_id':measurement_id,   
    }
    
    return render(request, 'index.html', context)
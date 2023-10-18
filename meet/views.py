from django.shortcuts import render

from .models import Header, Menu, SocialMenu

# Create your views here.
def meet(request):

    header = Header.objects.all()
    menu = Menu.objects.all()
    social = SocialMenu.objects.all()

    context = {
        'header':header,
        'menu':menu,  
        'social':social    
    }
    
    return render(request, 'index.html', context)
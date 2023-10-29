from django.shortcuts import render
from django.conf import settings

from meet.models import Header

# Create your views here.
def schedule(request):

    header = Header.objects.all()
    google_api_key = settings.GOOGLE_API_KEY
    google_calendar_id = settings.GOOGLE_CALENDAR_ID

    context = {
        'header':header,
        'google_api_key':google_api_key,
        'google_calendar_id':google_calendar_id,
    }
    
    return render(request, 'schedule.html', context)
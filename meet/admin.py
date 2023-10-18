from django.contrib import admin

from .models import Header, Menu, SocialMenu

# Register your models here.
admin.site.register(Header)
admin.site.register(Menu)
admin.site.register(SocialMenu)
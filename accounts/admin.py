from django.contrib import admin
from .models import User, Client

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.site_header = 'Auto Design Administration'
admin.site.site_title = 'Auto Design'
admin.site.index_title = 'Auto Design Database'
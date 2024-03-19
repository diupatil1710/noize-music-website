from django.contrib import admin
from .models import Song,user_login,category,contact

# Register your models here.
admin.site.register(Song)
admin.site.register(category)
admin.site.register(user_login)
admin.site.register(contact)


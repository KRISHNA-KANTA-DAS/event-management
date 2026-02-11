from django.contrib import admin
from .models import CustomUser, Membership

admin.site.register(CustomUser)
admin.site.register(Membership)

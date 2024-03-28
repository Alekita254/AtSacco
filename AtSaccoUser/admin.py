from django.contrib import admin
from .models import UserMember

@admin.register(UserMember)
class UserMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number', 'phone_number', 'email')


from django.contrib import admin
from .models import registerAdmin


class MembersAdmin(admin.ModelAdmin):

    list_display= "id","name","email","password"

admin.site.register(registerAdmin,MembersAdmin)
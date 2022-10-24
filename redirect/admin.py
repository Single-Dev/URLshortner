from django.contrib import admin
from .models import *

admin.site.register(CustomeUser)

@admin.register(UrlShortner)
class RegisterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('url', )}
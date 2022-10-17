from django.contrib import admin
from .models import *

# admin.site.register(URLshortner)

@admin.register(URLshortner)
class RegisterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('url', )}
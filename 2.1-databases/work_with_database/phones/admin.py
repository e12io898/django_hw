from django.contrib import admin
from phones.models import Phone

class Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Phone, Admin)
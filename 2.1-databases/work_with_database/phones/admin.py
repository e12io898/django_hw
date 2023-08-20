from django.contrib import admin
from phones.models import Phone

class Admin(admin.ModelAdmin):
    """ Автоматическое заполнение поля 'slug' при добавлении нового товара. """
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Phone, Admin)
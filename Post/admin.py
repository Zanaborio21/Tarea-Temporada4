from django.contrib import admin

# Register your models here.

from .models import Post,Ipe

admin.site.register(Post)
admin.site.register(Ipe)
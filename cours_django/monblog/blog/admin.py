from django.contrib import admin
from .models import *

admin.site.register(categorie)
# Register your models here.

admin.site.register(article)
admin.site.register(commentaire)

from django.contrib import admin
from .models import Lead, Language, Genre, Business
# Register your models here.
admin.site.register(Lead)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Business)

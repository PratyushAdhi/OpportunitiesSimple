from django.contrib import admin
from .models import Mail
# Register your models here.

# class MailAdmin(admin.ModelAdmin):
#     def has_view_or_change_permission(self, request, obj=None):
#         return True

#     def has_add_permission(self, request):
#         return True
    

# admin.site.register(Mail, MailAdmin)
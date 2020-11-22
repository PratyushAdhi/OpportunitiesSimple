from django.contrib import admin
from .models import Detail, Contact
admin.site.register(Contact)
# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    model = Detail

    def get_lead(self, obj):
        return obj.lead

    get_lead.short_description = "lead"

    def get_event_date(self, obj):
        return obj.date_of_event

    get_event_date.short_description = "date of event"

    def get_is_verified(self, obj):
        return obj.is_verified

    get_is_verified.short_description = "Verified"
    get_is_verified.boolean = True

    def get_is_published(self, obj):
        return obj.is_published

    get_is_published.short_description = "Published"
    get_is_published.boolean = True


    list_display = ["get_lead", "get_event_date", "get_is_verified", "get_is_published"]
    list_filter = ["date_of_event", "genre_id", "language_id"]

admin.site.register(Detail, DetailAdmin)

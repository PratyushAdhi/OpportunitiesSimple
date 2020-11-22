from .models import Lead, Language, Genre, Business
from evaluations.models import Evaluation
import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
# Register your models here.
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Business)

class LeadAdmin(admin.ModelAdmin):
    change_list_template = "./admin/leads/Lead/change_list.html"
    model = Lead

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            if obj.pending_status == "rejected":
                return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Lead.objects.annotate(date=TruncDay("created_date"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


    def get_lead(self, obj):
        return obj.event_title

    get_lead.short_description = "name"

    def get_status(self, obj):
        return obj.pending_status

    get_status.short_description = "status"

    def get_user(self, obj):
        return obj.user

    get_user.short_description = "user"

    def get_genres(self, obj):
        arr = []
        for item in obj.genre_id.all():
            arr.append(item.name)
        return arr


    get_genres.short_description = "genres"

    def get_created_date(self, obj):
        return obj.created_date

    get_created_date.short_description = "created date"

    def get_updated_date(self, obj):
        if obj.updated_date == obj.created_date:
            return "-"
        else:
            return obj.updated_date

    def get_sent_email(self, obj):
        qs = Evaluation.objects.get(lead=obj)
        return qs.send_email == True
        
    get_sent_email.short_description = "Email Sent"
    get_sent_email.boolean = True
    get_updated_date.short_description = "last update"

    list_display = ["get_lead", "get_user",  "get_genres", "get_created_date", "get_updated_date", "get_status", "get_sent_email"]
    list_filter = ("pending_status","genre_id",)



admin.site.site_header = "Songdew Opportunities Admin"
admin.site.site_title = "Songdew Opportunities Admin Website"
admin.site.register(Lead, LeadAdmin)
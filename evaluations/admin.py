from django.contrib import admin
from .models import Evaluation
from leads.models import Lead
from leads.admin import LeadAdmin
from django.db.models import Q
from .forms import EvaluationForm
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect, reverse
from mails.models import Mail
from django.urls import path
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.admin.options import add_preserved_filters
from django import template
from django import forms
from django.utils.html import format_html

register = template.Library()


class EvaluationForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = "__all__"

    def form_action(self, product):
        mail = Evaluation.objects.get(id = product.id).mail
        send_mail(
            mail.subject,
            mail.message,
            settings.EMAIL_HOST_USER,
            [product.lead.user.email,]
        )
        print("sent")
        return
# Register your models here.

class EvaluationAdmin(admin.ModelAdmin):

    # list_display = ['lead','process_button',]

    form = EvaluationForm

    def get_form(self, request, obj=None, **kwargs):
        form  = super(EvaluationAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['second_eval'].queryset = User.objects.filter(groups__name='AdminII')
        form.base_fields['first_eval'].queryset = User.objects.filter(groups__name='AdminI')
        return form

    class Media:
        js = ('./evaluations/buttonfile.js', )



    # def get_queryset(self, request):
    #     queryset = Evaluation.objects.all()
    #     if request.user.is_superuser:
    #         return queryset
    #     # if request.user.is_staff:
    #     #     criterion1 = Q(first_eval=request.user)
    #     #     criterion2 = Q(is_second_review=False)
    #     #     criterion3 = Q(second_eval=request.user)
    #     #     return queryset.filter((criterion1 & criterion2) | criterion3)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            elif obj.decision == "rejected" or obj.decision == "success":
                return False
            elif request.user == obj.first_eval and (obj.is_second_review == False):
                return True
            elif request.user == obj.second_eval:
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            elif request.user == obj.first_eval and (obj.is_second_review == False):
                return True
            elif request.user == obj.second_eval:
                return True
        return False

    def get_created_date(self, obj):
        return obj.lead.created_date

    get_created_date.short_description = "create date"

    def get_status(self, obj):
        return obj.lead.pending_status

    get_status.short_description = "status"

    def get_updated_date(self, obj):
        if obj.lead.updated_date == obj.lead.created_date:
            return "-"
        else:
            return obj.lead.updated_date

    get_updated_date.short_description = "last update"

    def get_lead(self, obj):
        return obj.lead.event_title or "-"

    get_lead.short_description = "lead"

    def get_sent_email(self, obj):
        return obj.send_email == True
    
    get_sent_email.boolean = True
    get_sent_email.short_description = "Email Sent"

    def is_under_second_review(self, obj):
        return obj.is_second_review == True

    is_under_second_review.boolean = True
    is_under_second_review.short_description = "Under Second Review"


    list_display = ['lead','get_created_date', 'get_updated_date', 'get_status', "is_under_second_review", 'get_sent_email']
    list_filter = ["decision", "is_second_review"]
        
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Mail)
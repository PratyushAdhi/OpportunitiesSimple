from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from mails.models import Mail
from details.models import Detail
from django.conf import settings
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your models here.

class Evaluation(models.Model):

    PENDING_STATUS = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("second_review", "Second Review"),
        ("clarification", "Clarification Sought"),
        ("rejected", "Rejected"),
    )

    REJECTION_REASON = (
        ("non_serious_enquiry", "Non Serious Enquiry"),
        ("out_of_scope", "Out Of Scope"),
        ("not_suitable", "Not Suitable"),
        ("disagreement_on_terms", "Disagreement On Terms"),
        ("others", "Others (Mention)")
    )

    first_eval                  = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="evaluator")
    second_eval                 = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="second_evaluator")
    is_second_review            = models.BooleanField(default=False)
    lead                        = models.ForeignKey('leads.Lead', null=True, blank=True, on_delete=models.CASCADE) #nu
    decision                    = models.CharField(choices=PENDING_STATUS, max_length=120, default="pending")
    rejection_reason            = models.CharField(choices=REJECTION_REASON, max_length=120, null=True, blank=True)
    # success_reason              = models.CharField(choices=SUCCESS_REASON, max_length=120, null=True, blank=True)
    comment                     = models.TextField() # in case of rejection or comments
    mail                        = models.ForeignKey(Mail, related_name="evaluation", null=True, blank=True, on_delete=models.CASCADE)
    send_email                  = models.BooleanField(default=True)

    def process_button(self):
        return format_html('<button id="%(id)s class="btn btn-default process_btn" '
                'data-value="%(value)s>Process</button>' % {'id': self.pk, 'value': "Send Email"})

    process_button.short_description = 'Action'
    process_button.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            user = User.objects.filter(is_staff=True).filter(groups__name='AdminI').order_by("?").first()
            self.first_eval = user
        if self.second_eval is not None:
            self.is_second_review = True
        if self.mail and self.send_email:
            send_mail(
                self.mail.subject,
                self.mail.body,
                settings.EMAIL_HOST_USER,
                [self.lead.user.email],
                fail_silently=False
            )
        super(Evaluation, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.lead.event_title

@receiver(post_save, sender=Evaluation)
def lead_accepted_create_detail_form(sender, instance, created, **kwargs):
    lead = instance.lead
    if instance.lead.user.is_staff:
        instance.decision = "accepted"
    if instance.decision == "accepted":
        if not instance.lead.user.is_staff:
            try:
                Detail.objects.get(lead=lead)
                return 
            except:
                print("here")
                print(instance.lead.user)
                detail = Detail.objects.create(
                    lead=instance.lead,
                    user=instance.lead.user, 
                    event_title=instance.lead.event_title,
                    budget=instance.lead.budget,
                    partner_type=instance.lead.partner_type,
                    college_name=instance.lead.college_name,
                    college_activity=instance.lead.college_activity,
                    date_of_event=instance.lead.date_of_event,
                    prizes=instance.lead.prizes,
                    college_music_contest=instance.lead.college_music_contest,
                    )
                for item in instance.lead.language_id.all():
                    detail.language_id.add(item)
                detail.genre_id.add(*instance.lead.genre_id.all())
                detail_form_url = settings.BASE_URL + "details/" + str(detail.id) + "/"
                send_mail(
                    "Detail Form",
                    detail_form_url,
                    settings.EMAIL_HOST_USER,
                    [instance.lead.user.email],
                )
                return
        else:
            try:
                Detail.objects.get(lead=lead)
                return 
            except:
                print("here one")
                print(instance.lead.user)
                detail = Detail.objects.create(
                    lead=instance.lead,
                    user=instance.lead.user, 
                    event_title=instance.lead.event_title,
                    budget=instance.lead.budget,
                    partner_type=instance.lead.partner_type,
                    college_name=instance.lead.college_name,
                    college_activity=instance.lead.college_activity,
                    date_of_event=instance.lead.date_of_event,
                    prizes=instance.lead.prizes,
                    college_music_contest=instance.lead.college_music_contest,
                    is_verified=True,
                    is_published=True
                    )
                print("check2")
                detail.language_id.add(*instance.lead.language_id.all())
                detail.genre_id.add(*instance.lead.genre_id.all())
                print("check1")
                detail_form_url = settings.BASE_URL + "details/" + str(detail.id) + "/"
                send_mail(
                    "Detail Form",
                    detail_form_url,
                    settings.EMAIL_HOST_USER,
                    [instance.lead.user.email, instance.lead.email],
                )
                print("mail-sent")
    


        
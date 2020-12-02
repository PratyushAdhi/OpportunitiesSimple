from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from evaluations.models import Evaluation


# Create your models here.
class Genre(models.Model):
    name            = models.CharField(max_length=255)
    # created_date    = models.DateTimeField(auto_now_add=True)
    # updated_date    = models.DateTimeField(auto_now=True)
    # status          = models.BooleanField(default=False)
    # image           = models.ImageField(upload_to=genre_image_directory_path,null=True,blank=True,validators=[validate_image_file_extension])
    # is_onboard      = models.BooleanField(default=False)
    # _var = models.BooleanField(default=False)

    # class Meta:

    #     db_table = '{0}_{1}'.format(settings.DB_TABLE_PREFIX,'Genre')

    #     permissions = (
    #             ('view_genre', 'Can view  Genre'),
    #         )
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

#already an app

class Language(models.Model):


    LANGUAGES = (
        ("assamese","Assamese"),
        ("bengali", "Bengali"),
        ("bodo", "Bodo"),
        ("dogri", "Dogri"),
        ("gujrati","Gujarati"),
        ("hindi", "Hindi"),
        ("kannada", "Kannada"),
        ("kashmiri", "Kashmiri"),
        ("konkani", "Konkani"),
        ("malayalam", "Malayalam"),
        ("manipuri", "Manipuri"),
        ("marathi","Marathi"),
        ("maithili", "Maithili"),
        ("nepali", "Nepali"),
        ("oriya","Oriya"),
        ("punjabi","Punjabi"),
        ("sanskrit","Sanskrit"),
        ("santhali","Santhali"),
        ("sindhi","Sindhi"),
        ("tamil","Tamil"),
        ("telugu", "Telugu"),
        ("urdu","Urdu"),
    )


    name            = models.CharField(max_length=255, choices=LANGUAGES)
    # created_date    = models.DateTimeField(auto_now_add=True)
    # updated_date    = models.DateTimeField(auto_now=True)
    # status          = models.BooleanField(default=False)
    # image           = models.ImageField(upload_to=language_image_directory_path,null=True,blank=True,validators=[validate_image_file_extension])
    # is_onboard      = models.BooleanField(default=False)
    # class Meta:

    #     db_table = '{0}_{1}'.format(settings.DB_TABLE_PREFIX,'Language')

    #     permissions = (
    #             ('view_language', 'Can view Language'),
    #         )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

class Business(models.Model):
    BUSINESS_CHOICES = (
        ('agency', 'Advertising/Media Agency'),
        ('organizer', 'Event Organizer'),
        ('label','Label'),
        ('music_company', 'Music Company'),
        ('tv_channel', 'TV Channel'),
        ('radio_station', 'Radio Station'),
        ('publication', 'Publication'),
        ('streaming_app', 'Streaming App'),
        ('series_producer', 'TV/ Web Series Producer'),
        ('film_producer','Film Producer'),
        ('artist_manager', 'Artist Manager'),
        ('college', 'College'),
        ('corporate_body', 'Corporate Body'),
        ('recording_studio','Recording Studio'),
        ('other', 'Other'),
    )
    name            = models.CharField(max_length=255, choices=BUSINESS_CHOICES, default="other")
    other           = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        if self.name == "other":
            return self.other
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Lead(models.Model):

    ACTIVITY = (
        ('record_deals', 'Record Deals'),
        ('artist_management', 'Artist Management'),
        ('talent_contest', 'Talent Contest'),
        ('music_production', 'Music Production'),
        ('influencer_marketing', 'Influencer Marketing'),
        ('collaboration', 'Collaboration'),
        ('retail_outlets', 'Licensing For Retail Outlets'),
        ('series_or_film', 'Licensing For Series Or Film'),
        ('radio_or_platforms', 'Radio Or Platforms'),
        ('gigs', 'Book Artists/Bands For Gigs'),
        ('broadcast', 'Music Videos For Broadcast'),
    )

    PARTNER_TYPES = (
        ("college", "College"),
        ("organization", "Organization"),
        ("individual", "Individual"),
        ("other", "Other")
    )

    COLLEGE_MUSIC_CONTEST = (
        ("band_battle_hindi", "Battle Of Bands (Hindi)"),
        ("band_battle_english", "Battle Of Bands (English)"),
        ("solo_singing", "Solo Singing Contest"),
        ("others", "Others"),
    )

    CHOICES = (
        ('agency', 'Advertising/Media Agency'),
        ('organizer', 'Event Organizer'),
        ('label','Label'),
        ('music_company', 'Music Company'),
        ('tv_channel', 'TV Channel'),
        ('radio_station', 'Radio Station'),
        ('publication', 'Publication'),
        ('streaming_app', 'Streaming App'),
        ('series_producer', 'TV/ Web Series Producer'),
        ('film_producer','Film Producer'),
        ('artist_manager', 'Artist Manager'),
        ('college', 'College'),
        ('corporate_body', 'COrporate Body'),
        ('recording_studio','Recording Studio'),
        ('other', 'Other'),
    )

    COLLEGE_ACTIVITIES = (
        ("music_contest", "Music Contest"),
        ("college_festival", "College Festival"),
    )

    BUDGETS = (
        ("upto_one_lac", "Upto Rs 1 L"),
        ("one_to_two_lac", "Rs 1L - 2L"),
        ("two_to_four_lac", "Rs 2L- 4L"),
        ("more_than_four_lac", "Rs 4L +"),
    )

    GIGS = (
        ("corporate_gig", "Corporate Gig"),
        ("festival", "Festival"),
        ("private_function", "Private Function")
    )

    PENDING_STATUS = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("second_review", "Second Review"),
        ("clarification", "Clarification Sought"),
        ("rejected", "Rejected"),
    )

    name                    = models.CharField(max_length=120, null=True, blank=True, verbose_name="name")
    email                   = models.EmailField(blank=True, null=True, verbose_name="email")
    phone_no                = models.BigIntegerField(blank=True, null=True, verbose_name="Phone Number")
    city                    = models.CharField(max_length=50, null=True, blank=True, verbose_name="City Of Partner")
    user                    = models.ForeignKey(User, on_delete=models.CASCADE, default=4, blank=True, verbose_name="User")
    partner_type            = models.CharField(max_length=50, choices=PARTNER_TYPES, null=True, blank=True, verbose_name="Partner Type")
    activity                = models.CharField(choices=ACTIVITY, max_length=100, null=True, blank=True, verbose_name="Activity For Which You Would Like To Work With Songdew")
    gigs                    = models.CharField(max_length=120, choices=GIGS, null=True, blank=True, verbose_name="Type Of Gigs")
    event_title             = models.CharField(max_length=120, null=True, blank=True, verbose_name="Name Of Event/Opportunity")
    event_city              = models.CharField(max_length=120, null=True, blank=True, verbose_name="City Of Event/Gig")
    business_id             = models.ManyToManyField(Business, blank=True, null=True, verbose_name="Businesses") #if partner business
    language_id             = models.ManyToManyField(Language, blank=True, verbose_name="Language Of Gig/Music Event") 
    genre_id                = models.ManyToManyField(Genre, blank=True, verbose_name="Genres")
    college_name            = models.CharField(max_length=50, blank=True, null=True, verbose_name="Name Of College (for college)") #if partner type college
    college_activity        = models.CharField(max_length = 50, choices=COLLEGE_ACTIVITIES, null=True, blank=True, verbose_name="College Activity") #if partner type college
    budget                  = models.CharField(choices=BUDGETS, max_length = 20, null=True, blank=True, verbose_name="Budget")
    college_music_contest   = models.CharField(max_length=120, choices=COLLEGE_MUSIC_CONTEST, null=True, blank=True, verbose_name="College Music Contest")
    date_of_event           = models.DateTimeField(null=True, blank=True, verbose_name="Date Of Event/Opportunity")
    prizes                  = models.CharField(max_length=500, null=True, blank=True, verbose_name="Prizes")
    org_name                = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name Of Organization")
    created_date            = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)   
    pending_status          = models.CharField(choices=PENDING_STATUS, max_length=100, default="pending")
    status                  = models.BooleanField(default=False) # This is for soft-delete
    other                   = models.TextField(null=True, blank=True)


    # def __str__(self):
    #     if not self.event_title:
    #         return self.name
    #     return self.event_title
#already an app



    #admin decisions
    def save(self, *args, **kwargs):
        if not self.id:
            super(Lead, self).save(*args, **kwargs)
            eval = Evaluation.objects.create(lead=self)
            self.evaluator = eval.first_eval.username
            return 
        super(Lead, self).save(*args, **kwargs)




@receiver(post_save, sender=Evaluation)
def update_lead_status(sender, instance, created, **kwargs):
    post_save.disconnect(update_lead_status, sender=sender)
    instance.lead.pending_status = instance.decision
    instance.lead.save()
    post_save.connect(update_lead_status, sender=sender)

@receiver(pre_delete, sender=Evaluation)
def eval_deleted(sender, instance, **kwargs):
    instance.lead.pending_status = "rejected"
    instance.lead.save()


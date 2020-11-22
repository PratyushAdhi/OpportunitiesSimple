from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name                = models.CharField(max_length=120)
    email               = models.EmailField()
    phone_no            = models.BigIntegerField()

    def __str__(self):
        return self.email

class Detail(models.Model):

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

    COLLEGE_MUSIC_CONTEST = (
        ("band_battle_hindi", "Battle Of Bands (Hindi)"),
        ("band_battle_english", "Battle Of Bands (English)"),
        ("solo_singing", "Solo Singing Contest"),
        ("others", "Others"),
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

    FREQUENCY = (
        ("month", "Monthly"),
        ("quarter", "Quarterly"),
        ("six_months", "Six Months"),
        ("yearly", "Yearly"),
    )

    user                    = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    lead                    = models.ForeignKey("leads.Lead", on_delete=models.CASCADE)
    event_title             = models.CharField(max_length=120, null=True, blank=True)
    partner_type            = models.CharField(max_length=120, null=True, blank=True)
    college_name            = models.CharField(max_length=120, blank=True, null=True)
    logo                    = models.FileField(upload_to="logos/", null=True, blank=True)
    about                   = models.TextField(null=True, blank=True)
    website_url             = models.URLField(null=True, blank=True)
    facebook_url            = models.URLField(null=True, blank=True)
    twitter_url             = models.URLField(null=True, blank=True)
    instagram_url           = models.URLField(null=True, blank=True)
    youtube_url             = models.URLField(null=True, blank=True)
    contact_1               = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True, related_name="contact_1_detail")
    contact_2               = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True, related_name="contact_2_detail")
    opportunity_category    = models.CharField(max_length=120, blank=True, null=True)
    offering                = models.TextField(null=True, blank=True)
    number_of_artists       = models.IntegerField(null=True, blank=True)
    if_recurring            = models.BooleanField(default=False)
    recurring_frequency     = models.CharField(max_length=120, choices=FREQUENCY, blank=True, null=True)
    city                    = models.CharField(max_length=120, null=True, blank=True)
    college_activity        = models.CharField(max_length=120,null=True, blank=True)
    date_of_event           = models.DateField(null=True, blank=True)
    college_music_contest   = models.CharField(max_length=120, choices=COLLEGE_MUSIC_CONTEST, null=True, blank=True)
    prizes                  = models.CharField(max_length=500, null=True, blank=True)
    genre_id                = models.ManyToManyField('leads.Genre', related_name="details")
    language_id             = models.ManyToManyField('leads.Language', related_name="details")
    budget                  = models.CharField(choices=BUDGETS, max_length=120, null=True, blank=True)
    other                   = models.TextField(null=True, blank=True)
    is_verified             = models.BooleanField(default=False)
    is_published            = models.BooleanField(default=False)

    def __str__(self):
        return self.lead.event_title
        




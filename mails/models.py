from django.db import models

# Create your models here.
class Mail(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    body  = models.TextField()

    def __str__(self):
        if self.name:
            return self.name
        return self.subject
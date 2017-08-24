from django.db import models
from django.utils.crypto import get_random_string

class URL(models.Model):
    url = models.URLField()
    slug = models.CharField(max_length=7, unique=True)
    clicks = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_random_string(length=7, allowed_chars='MINURLminurl1vV')
            return super(URL, self).save(*args, **kwargs)

class Analytic(models.Model):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    referrer = models.URLField(blank=True, null=True)
    url = models.ForeignKey(URL, related_name='analytics', blank=True, null=True)

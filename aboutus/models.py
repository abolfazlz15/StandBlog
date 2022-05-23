from django.db import models


class AboutUs(models.Model):
    body = models.TextField()


class SocialMedia(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    be = models.URLField()
    in_company = models.URLField()

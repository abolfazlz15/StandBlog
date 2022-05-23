from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class ContactInformation(models.Model):
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()


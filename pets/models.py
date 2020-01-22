from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField(default=0)
    age = models.PositiveSmallIntegerField(help_text="Years", default=0)
    photo = models.ImageField(upload_to="pet/photo", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    messages = models.TextField(max_length=10000)


    def __str__(self):
        return self.name
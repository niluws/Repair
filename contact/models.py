from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.subject

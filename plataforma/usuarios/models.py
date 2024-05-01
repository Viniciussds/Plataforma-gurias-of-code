from django.db import models

# Create your models here.
class user(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.full_name

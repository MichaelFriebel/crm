from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(models.Model):

    SOURCE = {
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    }

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address_street_1 = models.CharField(max_length=50)
    address_street_2 = models.CharField(max_length=50)
    address_state = models.CharField(max_length=15)
    address_zip = models.IntegerField()
    age = models.IntegerField()
    contact = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE, max_length=100)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
#    profile_pic = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
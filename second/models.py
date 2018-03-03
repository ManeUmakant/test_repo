from django.db import models



class Profile(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)




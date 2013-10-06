from django.db import models

class Client(models.Model):
    ip = models.IPAddressField()
    cookie = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
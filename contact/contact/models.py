from django.db import models

class Contact_Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    wrap = models.CharField(max_length=20)
    message = models.TextField(max_length=500)


    def __str__(self):
        return self.name
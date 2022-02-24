from datetime import datetime
from django.db import models

# Create your models here.



class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
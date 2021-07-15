from django.db import models

# Create your models here.

class yazı(models.Model):
    Name = models.CharField(max_length=20)
    Surname  = models.CharField(max_length=20)
    yayinTarihi= models.DateTimeField()

    def __str__(self):
        return self.Name
    

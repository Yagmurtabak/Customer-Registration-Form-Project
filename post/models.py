from django.db import models

# Create your models here.

class NewCustomer(models.Model):
    Name = models.CharField(max_length=20)
    Surname  = models.CharField(max_length=20)
    TC = models.IntegerField(null=True, unique=True)
    City = models.CharField(max_length=15,null=True)
    District = models.CharField(max_length=15,null=True)
    Telephone = models.IntegerField(null=True)
    yayinTarihi= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    

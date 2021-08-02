from django.db import models


class NewCustomer(models.Model):
    name = models.CharField(max_length=20)
    surname  = models.CharField(max_length=20)
    tc = models.CharField(max_length=11,null=True, unique=True)
    city = models.CharField(max_length=15,null=True)
    district = models.CharField(max_length=15,null=True)
    telephone = models.CharField(max_length=11,null=True,unique=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    

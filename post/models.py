from django.db import models


class NewCustomer(models.Model):
    Name = models.CharField(max_length=20)
    Surname  = models.CharField(max_length=20)
    TC = models.CharField(max_length=11,null=True, unique=True)
    City = models.CharField(max_length=15,null=True)
    District = models.CharField(max_length=15,null=True)
    Telephone = models.CharField(max_length=11,null=True,unique=True)
    Date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    
    

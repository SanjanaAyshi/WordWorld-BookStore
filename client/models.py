from django.db import models

# Create your models here.
#table: client
class Client(models.Model):
    name=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=11)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.phoneNumber}-{self.createdAt}"
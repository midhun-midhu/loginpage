
from django.db import models
import uuid


class registerAdmin(models.Model):
    id= models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.TextField()


    class Meta:
        db_table = "register"


        
import email
from unicodedata import name
from django.db import models
#makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
# model vo chiz hoti hai ho aapke database ko define karti hai ki data store karne ke liye
# it simply just like a table sheet jo ki data store karte hai. name, email and so on are the tables in our database
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    # This above all are the fields in django for more just search  fields in django on google.

    def __str__(self):
        return self.name
        # this above is used for saving name of form submitter by there own name without this line it was save as contact 1 contact2 and so on 
from django.db import models
from django.core.validators import RegexValidator
#from testapp.models import Signup
from django.contrib.auth.models import User

# Create your models here.
class listing_model(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200, blank=True)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    price=models.IntegerField()
    pincode=models.IntegerField()
    sqfoot=models.IntegerField()
    rooms=models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
def __str__(self):
    return self.title
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
today  = str(datetime.now().date())
#this is a test
class Registration(models.Model):
	first_name = models.CharField(max_length=200,default="")
	last_name = models.CharField(max_length=200,default="")
	email = models.EmailField(max_length=300,default="")
	phone = models.PositiveIntegerField(default=1)
	date = models.DateField('date of ride',blank=True,null=True)
	time = models.CharField(max_length=200)
    
    


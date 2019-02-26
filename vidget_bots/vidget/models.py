from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.IntegerField(blank=True)
	first_name = models.CharField(max_length=50, default="None")
	last_name =  models.CharField(max_length=50, default="None")
	img_url = models.CharField(max_length=300, default="None")

	
	def __str__(self):
		return str(self.user_id)

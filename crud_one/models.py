from django.db import models

class City(models.Model):
	id = models.AutoField(primary_key=True)
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=40)
	population = models.IntegerField()
	owner = models.IntegerField()

	

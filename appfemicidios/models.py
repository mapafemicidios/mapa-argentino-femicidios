from django.db import models
from django.utils import timezone

class Femicidio(models.Model):
	uploader = models.ForeignKey('auth.User')
	name = models.TextField()
	age = models.IntegerField(blank = True)
	country = models.TextField()
	province = models.TextField()
	city = models.TextField()
	date = models.DateField()
	created_at = models.DateTimeField(
		default = timezone.now)

	def __str__(self):
		return self.name
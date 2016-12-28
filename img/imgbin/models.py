from django.db import models
from django.utils import timezone

class IMG(models.Model):
	file = models.FileField(upload_to = '.')
	name = models.CharField(max_length = 50)
	created_time = models.DateTimeField(default = timezone.now)

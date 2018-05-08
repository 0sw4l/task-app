from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	success = models.BooleanField(default=False)
	text = models.TextField()
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'



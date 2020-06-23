from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


user_types = (
	('Teacher', 'Teacher'),
	('Student', 'Student'),
)


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=12, blank=True)
	date_of_birth = models.DateField(default=str(datetime.datetime.now()).split(' ')[0], blank=True)
	user_type = models.CharField(max_length=20, choices=user_types, blank=True, default='Student')

	def __str__(self):
		return self.user.username

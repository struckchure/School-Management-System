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

	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'


class Class(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=30, blank=False, unique=True)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.class_name

	class Meta:
		verbose_name = "Class"
		verbose_name_plural = "Classes"

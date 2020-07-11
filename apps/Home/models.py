from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


user_types = (
	('Teacher', 'Teacher'),
	('Student', 'Student'),
)

notification_types = (
	('Events', 'Events'),
	('Notice', 'Notice'),
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


class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	notification_type = models.CharField(max_length=20, choices=notification_types, blank=False)
	notification_title = models.CharField(max_length=200, blank=False)
	notification_content = models.TextField(blank=False)
	notification_date = models.DateTimeField(default=timezone.now)
	notification_expiry_date = models.DateTimeField(default=timezone.now)

	def _str__(self):
		return self.notification_type + ' ' + self.notification_title

	class Meta:
		verbose_name = 'Notification'
		verbose_name_plural = 'Notifications'

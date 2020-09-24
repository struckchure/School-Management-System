from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime

from . import managers



class User(AbstractBaseUser):

	class Gender(models.TextChoices):
		Male = 'M', _('Male')
		Female = 'F', _('Female')

	avatar = models.ImageField(blank=True, upload_to='avatars/')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100, unique=True, blank=False)
	email = models.CharField(max_length=100, blank=False)
	phone = models.CharField(max_length=100, blank=False)
	gender = models.CharField(max_length=20, choices=Gender.choices, blank=False)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now=True)
	last_updated = models.DateTimeField(auto_now_add=True)

	objects = managers.UserManager()
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.first_name
	
	def get_full_name(self):
		return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user}'


class Class(models.Model):
	class_teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=30, blank=False, unique=True)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.class_name


class Notification(models.Model):

	class NotificationTypes(models.TextChoices):
		event = 'E', _('Event')
		notice = 'N', _('Notice')

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	notification_type = models.CharField(max_length=20, choices=NotificationTypes.choices, blank=False)
	notification_title = models.CharField(max_length=200, blank=False)
	notification_content = models.TextField(blank=False)
	notification_date = models.DateTimeField(default=timezone.now)
	notification_expiry_date = models.DateTimeField(default=timezone.now)

	def _str__(self):
		return self.notification_type + ' ' + self.notification_title

from django.db import models
from django.contrib.auth.models import User


user_types = (
	('Teacher', 'Teacher'),
	('Student', 'Student'),
)


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=12, blank=True)
	date_of_birth = models.DateField(blank=True)
	user_type = models.CharField(max_length=20, choices=user_types)
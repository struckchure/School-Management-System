import getpass

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from Home import models

"""
    Management utility to create admin.
"""


class Command(BaseCommand):
    help = 'Creates admin'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        checker = True

        while checker:
            try:
                username = input('Username: ')
                if username not in [get_user_model().objects.all().only('username')]:
                    email = input('E-Mail: ')
                    phone = input('Phone: ')
                    gender = input('Gender (Male or Female?): ')
                    password = getpass.getpass('Password: ')
                    password1 = getpass.getpass('Password Confirmation: ')

                    if password == password1:
                        new_user = models.User.objects.create_teacher(
                            username=username,
                            email=email,
                            phone=phone,
                            gender=gender
                        )

                        new_user.set_password(password)

                        new_user.save()

                        if new_user:
                            self.stdout.write(self.style.SUCCESS('Successfully created user\n Only on admin can exist for referrral'))
                            checker = False
                    else:
                        self.stdout.write(self.style.WARNING('Password mismatch !!!'))
                else:
                    self.stdout.write(self.style.WARNING('User already exist'))
                    checker = False
            except IntegrityError:
                checker = True
                self.stdout.write(self.style.WARNING('User already exist'))

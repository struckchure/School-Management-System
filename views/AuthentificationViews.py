from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


# Custom Modules Imports

from views import pageConfigurations
from views import mainWindow

# Custom Modules End


'''
	Authentification Views
'''


class Login(QGroupBox):
	def __init__(self, pageController):
		QGroupBox.__init__(self)

		self.pageController = pageController

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.groupLayout)
		self.setObjectName('login')
		self.setStyleSheet(
			'''
				QGroupBox#login {
					border: 0px;
					background-image: url(resources/assets/images/home_bg_color_particles.jpg);
					background-repeat: no-repeat;
					background-position: center;
				}
			'''
		)

		self.initialization()

	def initialization(self):
		self.leftPageWidth = 1 - pageConfigurations.cardWidthRatio
		self.rightPageWidth = pageConfigurations.cardWidthRatio
		self.rightPageHeight = pageConfigurations.cardHeightRatio

		self.mainPage()
		# self.leftPage()
		self.rightPage()

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignCenter)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setMinimumSize(750, 600)
		self.mainPageGroup.setLayout(self.mainPageLayout)
		self.mainPageGroup.setObjectName('mainPageGroup')
		self.mainPageGroup.setStyleSheet(
			'''
				QGroupBox#mainPageGroup {
					border-radius: 20px;
					padding: 10px;
				}
			'''
		)

		self.groupLayout.addWidget(self.mainPageGroup)

	def leftPage(self):
		self.leftPageLayout = QVBoxLayout()
		self.leftPageLayout.setContentsMargins(0, 0, 0, 0)
		self.leftPageLayout.setAlignment(Qt.AlignCenter)

		self.leftPageGroup = QGroupBox()
		self.leftPageGroup.setLayout(self.leftPageLayout)
		self.leftPageGroup.setFixedSize(int(self.leftPageWidth * self.mainPageGroup.width()), self.mainPageGroup.height())
		self.leftPageGroup.setObjectName('leftPageGroup')
		self.leftPageGroup.setStyleSheet(
			'''
				QGroupBox#leftPageGroup {
					background-color: #405BC1;
					border: 0px;
					border-bottom-left-radius: 20px;
					border-top-left-radius: 20px;
				}
			'''
		)

		img_size = (self.leftPageGroup.width() // 2, self.leftPageGroup.height() // 2)
		img_size = (300, 300)

		# img_file = 'resources/assets/images/user-male-circle-filled.png'
		# image_ = cv2.resize(cv2.imread(img_file), img_size)
		# cv2.imwrite('resources/assets/images/logo.png', image_)
		# img_file = 'resources/assets/images/logo.png'

		img_file = 'resources/assets/images/icon.png'

		self.image = QPixmap(img_file)
		self.logo = QLabel()
		# self.logo.setMaximumSize(self.leftPageGroup.width() // 2, self.leftPageGroup.height() // 2)
		self.logo.setPixmap(self.image)
		self.leftPageLayout.addWidget(self.logo)

		self.mainPageLayout.addWidget(self.leftPageGroup)

	def rightPage(self):
		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.username = QLineEdit()
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(120, 50)
		self.rightPageLayout.addWidget(self.username)

		self.password = QLineEdit()
		self.password.setPlaceholderText('Password')
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaximumSize(120, 50)
		self.rightPageLayout.addWidget(self.password)

		self.loginButton = QPushButton('Login')
		self.loginButton.setMaximumSize(120, 45)
		self.loginButton.clicked.connect(self.loginButtonView)
		self.rightPageLayout.addWidget(self.loginButton)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setLayout(self.rightPageLayout)
		self.rightPageGroup.setFixedSize(int(self.rightPageWidth * self.mainPageGroup.width()), int(self.mainPageGroup.height() * self.rightPageHeight))
		self.rightPageGroup.setObjectName('rightPageGroup')
		self.rightPageGroup.setStyleSheet(
			'''
				QGroupBox#rightPageGroup {
					background-color: #FEE4E4;
					border: 0px;
					/* border-bottom-right-radius: 20px; */
					/* border-top-right-radius: 20px; */
				}
			'''
		)

		self.mainPageLayout.addWidget(self.rightPageGroup)

	def loginButtonView(self):
		try:
			from django.contrib.auth.models import User

			username = self.username.text()
			password = self.password.text()

			if username:
				if password:
					if len(password) >= pageConfigurations.minPasswordLength:
						try:
							self.get_user = User.objects.get(username=username)

							if password == self.get_user.password:
								self.nextPage()

								msg = f'Welcome Back {self.get_user.first_name} :) '
								message_box = QMessageBox()
								message_box.about(self, 'School Manager', msg)
							else:
								msg = 'Invalid Username or Password.'
								message_box = QMessageBox()
								message_box.about(self, 'School Manager', msg)
						except User.DoesNotExist:
							msg = 'Invalid Username or Password.'
							message_box = QMessageBox()
							message_box.about(self, 'School Manager', msg)
					else:
						msg = 'Password length is too short.\nShould contain at least six(6) characters.'
						message_box = QMessageBox()
						message_box.about(self, 'School Manager', msg)
				else:
					msg = 'Enter a valid Password.'
					message_box = QMessageBox()
					message_box.about(self, 'School Manager', msg)
			else:
				msg = 'Enter a valid Username.'
				message_box = QMessageBox()
				message_box.about(self, 'School Manager', msg)
		except Exception as e:
			raise e

	def nextPage(self):
		self.pageController.addWidget(mainWindow.Home(self.pageController, self.get_user))
		self.pageController.setCurrentIndex(self.pageController.currentIndex() + 1)


class Register(QGroupBox):
	def __init__(self, pageController):
		QGroupBox.__init__(self)

		self.pageController = pageController

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.groupLayout)
		self.setObjectName('login')
		self.setStyleSheet(
			'''
				QGroupBox#login {
					border: 0px;
					background-image: url(resources/assets/images/home_bg_color_particles.jpg);
					background-repeat: no-repeat;
					background-position: center;
				}
			'''
		)

		self.initialization()

	def initialization(self):
		self.leftPageWidth = 1 - pageConfigurations.cardWidthRatio
		self.rightPageWidth = pageConfigurations.cardWidthRatio
		self.rightPageHeight = pageConfigurations.cardHeightRatio

		self.mainPage()
		# self.leftPage()
		self.rightPage()

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignCenter)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setMinimumSize(750, 600)
		self.mainPageGroup.setLayout(self.mainPageLayout)
		self.mainPageGroup.setObjectName('mainPageGroup')
		self.mainPageGroup.setStyleSheet(
			'''
				QGroupBox#mainPageGroup {
					border-radius: 20px;
					padding: 10px;
				}
			'''
		)

		self.groupLayout.addWidget(self.mainPageGroup)

	def leftPage(self):
		self.leftPageLayout = QVBoxLayout()
		self.leftPageLayout.setContentsMargins(0, 0, 0, 0)
		self.leftPageLayout.setAlignment(Qt.AlignCenter)

		self.leftPageGroup = QGroupBox()
		self.leftPageGroup.setLayout(self.leftPageLayout)
		self.leftPageGroup.setFixedSize(int(self.leftPageWidth * self.mainPageGroup.width()), self.mainPageGroup.height())
		self.leftPageGroup.setObjectName('leftPageGroup')
		self.leftPageGroup.setStyleSheet(
			'''
				QGroupBox#leftPageGroup {
					background-color: #405BC1;
					border: 0px;
					border-bottom-right-radius: 20px;
					border-top-right-radius: 20px;
				}
			'''
		)

		img_size = (self.leftPageGroup.width() // 2, self.leftPageGroup.height() // 2)
		img_size = (300, 300)

		# img_file = 'resources/assets/user-male-circle-filled.png'
		# image_ = cv2.resize(cv2.imread(img_file), img_size)
		# cv2.imwrite('resources/assets/logo.png', image_)
		# img_file = 'resources/assets/logo.png'

		img_file = 'resources/assets/icon.png'

		self.image = QPixmap(img_file)
		self.logo = QLabel()
		# self.logo.setMaximumSize(self.leftPageGroup.width() // 2, self.leftPageGroup.height() // 2)
		self.logo.setPixmap(self.image)
		self.leftPageLayout.addWidget(self.logo)

		self.mainPageLayout.addWidget(self.leftPageGroup)

	def rightPage(self):
		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.formGridLayout = QGridLayout()
		self.formGridLayout.setAlignment(Qt.AlignCenter)
		self.rightPageLayout.addLayout(self.formGridLayout)

		self.first_name = QLineEdit()
		self.first_name.setPlaceholderText('First name')
		self.first_name.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.first_name)

		self.last_name = QLineEdit()
		self.last_name.setPlaceholderText('Last name')
		self.last_name.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.last_name)
		
		self.email = QLineEdit()
		self.email.setPlaceholderText('E-Mail')
		self.email.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.email)

		self.username = QLineEdit()
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.username)

		self.password1 = QLineEdit()
		self.password1.setPlaceholderText('New password')
		self.password1.setEchoMode(QLineEdit.Password)
		self.password1.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.password1)

		self.password2 = QLineEdit()
		self.password2.setPlaceholderText('Confirm password')
		self.password2.setEchoMode(QLineEdit.Password)
		self.password2.setMaximumSize(160, 70)
		self.rightPageLayout.addWidget(self.password2)

		self.buttonLayout = QHBoxLayout()
		self.buttonLayout.setAlignment(Qt.AlignCenter)
		self.rightPageLayout.addLayout(self.buttonLayout)

		self.loginButton = QPushButton('Register')
		self.loginButton.setMaximumSize(120, 45)
		self.loginButton.clicked.connect(self.registerButtonView)
		self.buttonLayout.addWidget(self.loginButton)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setLayout(self.rightPageLayout)
		self.rightPageGroup.setFixedSize(int(self.rightPageWidth * self.mainPageGroup.width()), int(self.mainPageGroup.height() * self.rightPageHeight))
		self.rightPageGroup.setObjectName('rightPageGroup')
		self.rightPageGroup.setStyleSheet(
			'''
				QGroupBox#rightPageGroup {
					background-color: #FEE4E4;
					border: 0px;
					/* border-bottom-left-radius: 20px; */
					/* border-top-left-radius: 20px; */
				}
			'''
		)

		self.mainPageLayout.addWidget(self.rightPageGroup)

	def registerButtonView(self):
		try:
			from django.contrib.auth.models import User
			from apps.Home import models

			first_name = self.first_name.text()
			last_name = self.last_name.text()
			username = self.username.text()
			email = self.email.text()
			password1 = self.password1.text()
			password2 = self.password2.text()

			if first_name and last_name:
				if username and email:
					if username not in [i.username for i in list(User.objects.all().only('username'))]:
						if '@' in email:
							email_extension = email.split('@')[1]
							if email_extension and ('.com' in email_extension):
								if (len(password1) >= 6) and (len(password2) >= 6):
									if password1 and password2:
										if password1 == password2:
											new_user = User.objects.create(
												first_name = first_name,
												last_name = last_name,
												username = username,
												email = email,
												password = password1
											)
											new_user.save()

											user_profile = models.Profile.objects.create(
												user=new_user
											)
											user_profile.save()

											msg = f'{first_name} {last_name} has been successfully registered, please check your mail for more information.'
											message_box = QMessageBox()
											message_box.about(self, 'School Manager', msg)

											self.pageController.addWidget(Login(self.pageController))
											self.pageController.setCurrentIndex(self.pageController.currentIndex() + 1)
										else:
											msg = 'Your passwords don\'t match. Try again.'
											message_box = QMessageBox()
											message_box.about(self, 'School Manager', msg)
									else:
										msg = 'Please enter a valid password.'
										message_box = QMessageBox()
										message_box.about(self, 'School Manager', msg)
								else:
									msg = 'Passwords should contain at least six(6) characters.'
									message_box = QMessageBox()
									message_box.about(self, 'School Manager', msg)
							else:
								msg = 'Your email extension is not valid.'
								message_box = QMessageBox()
								message_box.about(self, 'School Manager', msg)
						else:
							msg = 'Your email is not valid.'
							message_box = QMessageBox()
							message_box.about(self, 'School Manager', msg)
					else:
						msg = f'{username} is already taken.'
						message_box = QMessageBox()
						message_box.about(self, 'School Manager', msg)
				else:
					msg = 'Please enter a valid Username and E-Mail.'
					message_box = QMessageBox()
					message_box.about(self, 'School Manager', msg)
			else:
				msg = 'First name and Last name is required.'
				message_box = QMessageBox()
				message_box.about(self, 'School Manager', msg)
		except Exception as e:
			raise e

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


# Custom Modules Imports

from views import pageConfigurations
from views import mainWindow
from resources.assets.customWidgets import customWidgets

# Custom Modules End


'''
	Authentification Views
'''


class Login(QGroupBox):
	def __init__(self, pageController, pageFinders=pageConfigurations.pageFinders):
		QGroupBox.__init__(self)

		self.pageController = pageController
		self.pageFinders = pageFinders

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
		qss = open('resources/assets/qss/authQLineEdit.qss', 'r').read()
		qss_button = open('resources/assets/qss/authQPushButton.qss', 'r').read()

		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.pageTitle = QLabel('School Management System')
		self.pageTitle.setAlignment(Qt.AlignCenter)
		self.pageTitle.setObjectName('pageTitle')
		self.pageTitle.setMaximumSize(500, 100)
		self.pageTitle.setStyleSheet(qss_button)
		self.rightPageLayout.addWidget(self.pageTitle, stretch=0, alignment=Qt.AlignTop)

		self.spacer = QLabel()
		self.spacer.setFixedHeight(30)
		self.rightPageLayout.addWidget(self.spacer, stretch=0, alignment=Qt.AlignTop)

		self.username = QLineEdit()
		self.username.setObjectName('username')
		self.username.setStyleSheet(qss)
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.username)

		self.password = QLineEdit()
		self.password.setObjectName('password')
		self.password.setStyleSheet(qss)
		self.password.setPlaceholderText('Password')
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.password)

		'''
			Caps Lock warning, Session Keeper, Forgot Password
		'''

		self.spacer2 = QLabel()
		self.spacer2.setFixedHeight(10)
		self.rightPageLayout.addWidget(self.spacer2)

		self.extraLayout = QHBoxLayout()
		self.extraLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.addLayout(self.extraLayout)

		self.spacer2 = QLabel()
		self.spacer2.setFixedHeight(10)
		self.rightPageLayout.addWidget(self.spacer2)

		self.keepSession = QCheckBox('Keep me logged in for 30 days')
		self.extraLayout.addWidget(self.keepSession, stretch=0, alignment=Qt.AlignLeft)

		self.forgotPassword = QPushButton('Forgot password?')
		self.forgotPassword.setObjectName('forgotPassword')
		self.forgotPassword.setStyleSheet(qss_button)
		self.extraLayout.addWidget(self.forgotPassword, stretch=0, alignment=Qt.AlignRight)

		self.loginButton = QPushButton('Login')
		self.loginButton.setObjectName('login')
		self.loginButton.setStyleSheet(qss_button)
		self.loginButton.setMaximumSize(400, 80)
		self.loginButton.clicked.connect(self.loginButtonView)
		self.rightPageLayout.addWidget(self.loginButton)

		self.spacer3 = QLabel()
		self.spacer3.setFixedHeight(30)
		self.rightPageLayout.addWidget(self.spacer3)

		self.signUpLayout = QHBoxLayout()
		self.signUpLayout.setSpacing(0)
		self.signUpLayout.setAlignment(Qt.AlignCenter)
		self.rightPageLayout.addLayout(self.signUpLayout)

		self.signUpLabel = QLabel('Need an account?')
		self.signUpLabel.setObjectName('signUpLabel')
		self.signUpLabel.setStyleSheet(qss_button)
		self.signUpLabel.setMaximumSize(120, 50)
		self.signUpLayout.addWidget(self.signUpLabel)

		self.signUpButton = QPushButton('Sign Up')
		self.signUpButton.setObjectName('signUpButton')
		self.signUpButton.clicked.connect(self.signUpButtonView)
		self.signUpButton.setStyleSheet(qss_button)
		self.signUpButton.setMaximumSize(120, 50)
		self.signUpLayout.addWidget(self.signUpButton)

		blurRadius = 90
		offset = 20
		color = QColor(0, 0, 0, 255 * .3)

		self.rightPageEffect = QGraphicsDropShadowEffect()
		self.rightPageEffect.setBlurRadius(blurRadius)
		self.rightPageEffect.setOffset(offset)
		self.rightPageEffect.setColor(color)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setGraphicsEffect(self.rightPageEffect)
		self.rightPageGroup.setLayout(self.rightPageLayout)
		self.rightPageGroup.setFixedSize(int(self.rightPageWidth * self.mainPageGroup.width()), int(self.mainPageGroup.height() * self.rightPageHeight))
		self.rightPageGroup.setObjectName('rightPageGroup')
		self.rightPageGroup.setStyleSheet(
			'''
				QGroupBox#rightPageGroup {
					border: 0px;
					background-color: #DEF3F1;
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

								self.trayIcon = customWidgets.Notification()

								msg = f'Welcome Back {self.get_user.first_name} :) '
								self.trayIcon.show()
								print(dir(self.trayIcon))

								message_box = QMessageBox()
								# message_box.about(self, 'School Manager', msg)
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

	def signUpButtonView(self):
		if 'signUpPage' not in self.pageFinders['page']:
			self.pageFinders['page'].append('signUpPage')
			self.pageFinders['index'].append(self.pageController.currentIndex() + 1)

			self.pageController.addWidget(Register(self.pageController))
			self.pageController.setCurrentIndex(self.pageController.currentIndex() + 1)

		else:
			self.pageController.setCurrentIndex(self.pageFinders['index'][self.pageFinders['page'].index('signUpPage')])


class Register(QGroupBox):
	def __init__(self, pageController, pageFinders=pageConfigurations.pageFinders):
		QGroupBox.__init__(self)

		self.pageController = pageController
		self.pageFinders = pageFinders

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
		qss = open('resources/assets/qss/authQLineEdit.qss', 'r').read()
		qss_button = open('resources/assets/qss/authQPushButton.qss', 'r').read()

		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.pageTitle = QLabel('School Management System')
		self.pageTitle.setAlignment(Qt.AlignCenter)
		self.pageTitle.setObjectName('pageTitle')
		self.pageTitle.setMaximumSize(500, 100)
		self.pageTitle.setStyleSheet(qss_button)
		self.rightPageLayout.addWidget(self.pageTitle, stretch=0, alignment=Qt.AlignTop)

		self.spacer = QLabel()
		self.spacer.setFixedHeight(10)
		self.rightPageLayout.addWidget(self.spacer, stretch=0, alignment=Qt.AlignTop)

		self.first_name = QLineEdit()
		self.first_name.setObjectName('first_name')
		self.first_name.setStyleSheet(qss_button)
		self.first_name.setPlaceholderText('First name')
		self.first_name.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.first_name)

		self.last_name = QLineEdit()
		self.last_name.setObjectName('last_name')
		self.last_name.setStyleSheet(qss_button)
		self.last_name.setPlaceholderText('Last name')
		self.last_name.setMaximumSize(400, 80)
		self.rightPageLayout.addWidget(self.last_name)

		self.username = QLineEdit()
		self.username.setObjectName('username')
		self.username.setStyleSheet(qss)
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.username)

		self.email = QLineEdit()
		self.email.setObjectName('email')
		self.email.setStyleSheet(qss)
		self.email.setPlaceholderText('E-Mail')
		self.email.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.email)

		self.password1 = QLineEdit()
		self.password1.setObjectName('password')
		self.password1.setStyleSheet(qss)
		self.password1.setPlaceholderText('New Password')
		self.password1.setEchoMode(QLineEdit.Password)
		self.password1.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.password1)

		self.password2 = QLineEdit()
		self.password2.setObjectName('password')
		self.password2.setStyleSheet(qss)
		self.password2.setPlaceholderText('Confirm Password')
		self.password2.setEchoMode(QLineEdit.Password)
		self.password2.setMaximumSize(400, 60)
		self.rightPageLayout.addWidget(self.password2)

		'''
			Caps Lock warning, Session Keeper, Forgot Password
		'''

		self.spacer2 = QLabel()
		self.spacer2.setFixedHeight(5)
		self.rightPageLayout.addWidget(self.spacer2)

		self.extraLayout = QHBoxLayout()
		self.extraLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.addLayout(self.extraLayout)

		self.spacer2 = QLabel()
		self.spacer2.setFixedHeight(5)
		self.rightPageLayout.addWidget(self.spacer2)

		self.keepSession = QCheckBox('I Agree')
		self.extraLayout.addWidget(self.keepSession, stretch=0, alignment=Qt.AlignLeft)

		self.termsAndConditions = QPushButton('Terms and Conditions')
		self.termsAndConditions.setObjectName('forgotPassword')
		self.termsAndConditions.setStyleSheet(qss_button)
		self.extraLayout.addWidget(self.termsAndConditions, stretch=0, alignment=Qt.AlignRight)

		self.registerButton = QPushButton('Register')
		self.registerButton.setObjectName('login')
		self.registerButton.setStyleSheet(qss_button)
		self.registerButton.setMaximumSize(400, 80)
		self.registerButton.clicked.connect(self.registerButtonView)
		self.rightPageLayout.addWidget(self.registerButton)

		self.spacer3 = QLabel()
		self.spacer3.setFixedHeight(10)
		self.rightPageLayout.addWidget(self.spacer3)

		self.signInLayout = QHBoxLayout()
		self.signInLayout.setSpacing(0)
		self.signInLayout.setAlignment(Qt.AlignCenter)
		self.rightPageLayout.addLayout(self.signInLayout)

		self.signInLabel = QLabel('Already have an account?')
		self.signInLabel.setObjectName('signUpLabel')
		self.signInLabel.setStyleSheet(qss_button)
		self.signInLabel.setMaximumSize(200, 50)
		self.signInLayout.addWidget(self.signInLabel)

		self.signInButton = QPushButton('Sign In')
		self.signInButton.clicked.connect(self.signInButtonView)
		self.signInButton.setObjectName('signUpButton')
		self.signInButton.setStyleSheet(qss_button)
		self.signInButton.setMaximumSize(120, 50)
		self.signInLayout.addWidget(self.signInButton)

		blurRadius = 90
		offset = 20
		color = QColor(0, 0, 0, 255 * .3)

		self.rightPageEffect = QGraphicsDropShadowEffect()
		self.rightPageEffect.setBlurRadius(blurRadius)
		self.rightPageEffect.setOffset(offset)
		self.rightPageEffect.setColor(color)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setGraphicsEffect(self.rightPageEffect)
		self.rightPageGroup.setLayout(self.rightPageLayout)
		self.rightPageGroup.setFixedSize(int(self.rightPageWidth * self.mainPageGroup.width()), int(self.mainPageGroup.height() * self.rightPageHeight))
		self.rightPageGroup.setObjectName('rightPageGroup')
		self.rightPageGroup.setStyleSheet(
			'''
				QGroupBox#rightPageGroup {
					border: 0px;
					background-color: #DEF3F1;
					/* border-bottom-right-radius: 20px; */
					/* border-top-right-radius: 20px; */
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

	def signInButtonView(self):
		if 'signInPage' not in self.pageFinders['page']:
			self.pageFinders['page'].append('signInPage')
			self.pageFinders['index'].append(self.pageController.currentIndex() + 1)
			
			self.pageController.addWidget(Register(self.pageController, self.pageFinders))
			self.pageController.setCurrentIndex(self.pageController.currentIndex() + 1)

		else:
			self.pageController.setCurrentIndex(self.pageFinders['index'][self.pageFinders['page'].index('signInPage')])

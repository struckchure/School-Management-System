from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Custom Modules Imports

from views import utils
from resources.assets.customWidgets import customWidgets
from views import pageConfigurations
from Home import models

# Custom Modules End


'''
	Teacher Views
'''


class Teachers(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Teachers')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		self.allTeacherstable()

	def allTeacherstable(self):
		self.teacherTables = customWidgets.Table(
			[
				'First name',
				'Last name',
				'Username',
				'E-Mail',
				'Date',
				'View',
				'Delete',
			]
		)

		self.teacherCell = customWidgets.Cell(self.getAllTeachers)
		self.teacherCell.startCell()

		self.groupLayout.addWidget(self.teacherTables)

	def getAllTeachers(self):
		allTeachers = models.User.objects.all().filter(is_teacher=True)
		# allTeachers = models.User.objects.all()

		for teacher in allTeachers:
			self.teacherTables.addRow(
				[
					teacher.first_name,
					teacher.last_name,
					teacher.username,
					teacher.email,
					teacher.date_joined.strftime('%B %d, %Y')
				],
				[
					('View', 'black', 'User', 'view'),
					('Delete', 'orange', 'User', 'delete'),
				]
			)


class TeacherAdmission(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Teacher Admission')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)
		self.setSizePolicy(
			QSizePolicy.Expanding,
			QSizePolicy.Expanding
		)

		self.initalization()

	def initalization(self):
		# self.infoCardWidth = self.width() * 12
		# self.infoCardWidth = 1800
		self.infoCardWidth = self.width() * 8
		self.infoCardHeight = self.height() * 5

		self.page()

	def page(self):
		rightRatio = 0.1
		leftRatio = 1 - rightRatio
		headerHeight = 30
		self.headerHeight = headerHeight

		self.headerBG = pageConfigurations.pageHeaderBG
		self.headerBorder = pageConfigurations.pageHeaderBorder

		self.pageLayout = QVBoxLayout()
		self.pageLayout.setSpacing(0)
		self.pageLayout.setContentsMargins(0, 0, 0, 0)
		self.pageLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

		self.groupLayout.addLayout(self.pageLayout, 1, 0)

		self.admissionCard = customWidgets.CardBasic(
			accent='rgba(0, 0, 0, 0)',
			width=self.infoCardWidth,
			height=self.infoCardHeight,
		)

		self.admissionCardContent = customWidgets.CardContent()

		self.admissionCard.cardLayout.addWidget(self.admissionCardContent)
		self.pageLayout.addWidget(self.admissionCard)

		self.formLayout = QGridLayout()
		self.formLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		self.formLayout.setSpacing(0)
		self.formLayout.setContentsMargins(0, 0, 0, 0)

		self.admissionForm()

	def admissionForm(self):
		self.teacherFormDetailsHeader = customWidgets.CardHeader(
			text='Teacher Information',
			accent=self.headerBG,
		)

		self.admissionCardContent.cardLayout.addWidget(self.teacherFormDetailsHeader)

		# First row

		self.first_name = customWidgets.TextInput(
			labelText='First name',
			placeHolderText='John',
			enabled=True,
		)

		self.last_name = customWidgets.TextInput(
			labelText='Last name',
			placeHolderText='Doe',
			enabled=True,
		)

		self.username = customWidgets.TextInput(
			labelText='Username',
			placeHolderText='JohnDoe',
			enabled=True,
		)

		self.gender = customWidgets.ComboInput(
			labelText='Gender',
			placeHolderText='select'
		)

		self.gender.addItem('Male')
		self.gender.addItem('Female')

		self.image = customWidgets.ImageInput(
			# labelText='image',
			width=320,
			height=330
		)

		# Second row
		
		self.password1 = customWidgets.TextInput(
			labelText='New Password',
			placeHolderText='Keep it secret',
			password=True
		)

		self.password2 = customWidgets.TextInput(
			labelText='Confirm Password',
			placeHolderText='Keep it secret',
			password=True
		)

		self.phone_number = customWidgets.TextInput(
			labelText='Mobile Number',
			placeHolderText='+234 801 234 5678'
		)

		self.email = customWidgets.TextInput(
			labelText='E-Mail',
			placeHolderText='johndoe@school.com'
		)

		self.formLayout.addWidget(self.first_name, 0, 0)
		self.formLayout.addWidget(self.last_name, 0, 1)
		self.formLayout.addWidget(self.image, 0, 4, 5, 1)

		self.formLayout.addWidget(self.phone_number, 1, 0)
		self.formLayout.addWidget(self.email, 1, 1)

		self.formLayout.addWidget(self.username, 2, 0)
		self.formLayout.addWidget(self.gender, 2, 1)

		self.formLayout.addWidget(self.password1, 3, 0)
		self.formLayout.addWidget(self.password2, 3, 1)
		
		self.formButtonLayout = QVBoxLayout()
		self.formButtonLayout.setAlignment(Qt.AlignCenter)

		self.signUpLabel = QLabel('Already have an account?')
		self.signUpLabel.setObjectName('signUpLabel')
		self.signUpLabel.setMaximumSize(200, 50)
		self.formButtonLayout.addWidget(self.signUpLabel)

		self.signUpButton = QPushButton('Sign Up')
		self.signUpButton.setStyleSheet(
			'''
				QPushButton {
					background-color: blue;
					color: white;
				}
				QPushButton:hover {
					background-color: rgba(0, 0, 0, 0.9);
				}
			'''
		)
		self.signUpButton.clicked.connect(self.signUpButtonView)
		self.signUpButton.setObjectName('admissionButton')
		self.signUpButton.setMaximumSize(500, 50)
		self.signUpButton.setSizePolicy(
			QSizePolicy.Expanding,
			QSizePolicy.Expanding
		)
		self.formButtonLayout.addWidget(self.signUpButton)

		self.admissionCardContent.cardLayout.addLayout(self.formLayout)
		self.admissionCardContent.cardLayout.addLayout(self.formButtonLayout)
	
	def signUpButtonView(self):
		try:
			phone_length = 10
			password_length = 6
			all_usernames = list(models.User.objects.values_list('username', flat=True))

			if not self.image.imagePath:
				self.image.imagePath = '../images/default-avatar.png'

			if self.first_name.text() and self.last_name.text():
				if self.username.text() not in all_usernames:
					if self.gender.text() != self.gender.placeHolderText:
						if len(self.phone_number.text()) >= phone_length:
							if self.email.text():
								if len(self.password1.text()) >= password_length and len(self.password2.text()) >= password_length:
									if self.password1.text() == self.password2.text():
										new_user = models.User.objects.create_teacher(
											first_name=self.first_name.text(),
											last_name=self.last_name.text(),
											avatar=self.image.imagePath(),
											gender=self.gender.text(),
											username=self.username.text(),
											email=self.email.text(),
											phone=self.phone_number.text(),
											is_teacher=True,
										)

										new_user.set_password(self.password1.text())
										new_user.save()

										message = f'Congratulations !!! \nYour registration was successful'
										
										self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
										self.messagePopUp.show()

										self.cleanFormFields()
									else:
										message = f'Password mismatch'
										self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
										self.messagePopUp.show()
								else:
									message = f'Password length too short, At least six(6) characters are required'
									self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
									self.messagePopUp.show()
							else:
								message = f'Enter a valid E-Mail address'
								self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
								self.messagePopUp.show()
						else:
							message = f'Phone number must be at least ten(10) characters'
							self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
							self.messagePopUp.show()
					else:
						message = f'Please select your gender'
						self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
						self.messagePopUp.show()
				else:
					message = f'{self.username.text()} already exist, try something different'
					self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
					self.messagePopUp.show()
			else:
				message = f'First name and Last name is required'
				self.messagePopUp = customWidgets.PopUp(title='School Manager', body=message, buttonText='&Ok')
				self.messagePopUp.show()
		except Exception as e:
			message = str(e)
			self.messagePopUp = customWidgets.PopUp(title='Error Manager', body=message, buttonText='&Ok')
			self.messagePopUp.show()
	
	def cleanFormFields(self):
		self.first_name.textInput.setText('')
		self.last_name.textInput.setText('')
		self.email.textInput.setText('')
		self.phone_number.textInput.setText('')
		self.username.textInput.setText('')
		self.password1.textInput.setText('')
		self.password2.textInput.setText('')
		self.image.setPixmap('')


class TeacherPromotion(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Teacher Promotion')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		pass

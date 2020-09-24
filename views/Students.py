from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

# Custom Modules Imports

from views import pageConfigurations
from views import utils
from resources.assets.customWidgets import customWidgets
from Home import models

# Custom Modules End


'''
	Student Views
'''


class Students(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Students')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 2)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		self.allStudentstable()

	def allStudentstable(self):
		self.studentTables = customWidgets.Table(
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

		self.StudentCell = customWidgets.Cell(self.getAllStudents)
		self.StudentCell.startCell()

		self.groupLayout.addWidget(self.studentTables)

	def getAllStudents(self):
		allStudents = models.User.objects.all().filter(is_student=True)
		# allStudents = models.User.objects.all()

		for student in allStudents:
			self.studentTables.addRow(
				[
					student.first_name,
					student.last_name,
					student.username,
					student.email,
					student.date_joined.strftime('%B %d, %Y')
				],
				[
					('View', 'black', 'User', 'view'),
					('Delete', 'orange', 'User', 'delete'),
				]
			)


class StudentDetails(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Students')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 2)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		self.infoCardWidth = self.width() * 5
		self.infoCardHeight = self.height() * 5
		rightRatio = 0.1
		leftRatio = 1 - rightRatio

		headerHeight = 30
		self.headerBG = pageConfigurations.pageHeaderBG
		self.headerBorder = pageConfigurations.pageHeaderBorder

		self.studentInfo = customWidgets.CardBasic(
			width=self.infoCardWidth * rightRatio,
			height=self.infoCardHeight,
			# accent='$theme'
		)

		self.studentInfoHeader = customWidgets.CardHeader(
			'Student Information',
			width=self.studentInfo.width(),
			height=headerHeight,
			accent=self.headerBG
		)

		self.studentInfo.cardLayout.addWidget(self.studentInfoHeader)

		self.studentSiblings = customWidgets.CardBasic(
			width=self.infoCardWidth * rightRatio,
			height=self.infoCardHeight,
			# accent='$theme'
		)

		self.studentSiblingsHeader = customWidgets.CardHeader(
			'Student Siblings',
			width=self.studentSiblings.width(),
			height=headerHeight,
			accent=self.headerBG
		)

		self.studentSiblings.cardLayout.addWidget(self.studentSiblingsHeader)

		self.tabCardWidth, self.tabCardHeight = 500, 400

		self.studentExtras = customWidgets.TabCardBasic(
			width=900,
			height=900
		)

		self.studentExtrasTab = customWidgets.TabBasic()

		self.profile = customWidgets.Tab('Profile')

		self.profileContent = customWidgets.CardBasic(
			width=self.tabCardWidth,
			height=self.tabCardHeight,
			accent='rgba(0, 0, 0, 0)'
		)

		self.profile.groupLayout.addWidget(self.profileContent)
		self.studentExtrasTab.addTabWidget(self.profile)

		self.fees = customWidgets.Tab('Fees')
		self.fees.groupLayout.addWidget(QLabel('Fees'))
		self.studentExtrasTab.addTabWidget(self.fees)

		self.exam = customWidgets.Tab('Exam')
		self.exam.groupLayout.addWidget(QLabel('Exam'))
		self.studentExtrasTab.addTabWidget(self.exam)

		self.reports = customWidgets.Tab('Reports')
		self.reports.groupLayout.addWidget(QLabel('Reports'))
		self.studentExtrasTab.addTabWidget(self.reports)

		self.studentExtras.cardLayout.addWidget(
			self.studentExtrasTab,
			stretch=0,
			alignment=Qt.AlignCenter
		)

		self.groupLayout.addWidget(self.studentInfo, 1, 0)
		self.groupLayout.addWidget(self.studentExtras, 1, 1, 2, 1)
		self.groupLayout.addWidget(self.studentSiblings, 2, 0)


class StudentAdmission(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Student Admission')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
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
		all_usernames = models.User.objects.values_list('username', flat=True)

		admission_num = utils.generate_admission_number(all_usernames)

		self.studentFormDetailsHeader = customWidgets.CardHeader(
			text='Student Information',
			accent=self.headerBG,
		)

		self.admissionCardContent.cardLayout.addWidget(self.studentFormDetailsHeader)

		# First row

		self.admission_num = customWidgets.TextInput(
			labelText='Admission Number',
			placeHolderText=f'{admission_num}',
			enabled=False,
		)

		self.school_class = customWidgets.ComboInput(
			labelText='Class',
			placeHolderText='select'
		)

		self.school_class.addItem('SSS 1')
		self.school_class.addItem('SSS 2')
		self.school_class.addItem('SSS 3')

		self.gender = customWidgets.ComboInput(
			labelText='Gender',
			placeHolderText='select'
		)

		self.gender.addItem('Male')
		self.gender.addItem('Female')

		self.section = customWidgets.ComboInput(
			labelText='Section',
			placeHolderText='select'
		)

		self.section.addItem('A')
		self.section.addItem('B')

		self.image = customWidgets.ImageInput(
			# labelText='image',
			width=320,
			height=330
		)
		# self.image.connectButton(self.select_image_dialog)

		# Second row
		
		self.first_name = customWidgets.TextInput(
			labelText='First Name',
			placeHolderText='John'
		)

		self.last_name = customWidgets.TextInput(
			labelText='Last Name',
			placeHolderText='Doe'
		)

		self.phone_number = customWidgets.TextInput(
			labelText='Mobile Number',
			placeHolderText='+234 801 234 5678'
		)

		self.email = customWidgets.TextInput(
			labelText='E-Mail',
			placeHolderText='johndoe@school.com'
		)

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

		self.formLayout.addWidget(self.admission_num, 0, 0)
		self.formLayout.addWidget(self.school_class, 0, 1)
		self.formLayout.addWidget(self.image, 0, 4, 5, 1)

		self.formLayout.addWidget(self.gender, 1, 0)
		self.formLayout.addWidget(self.section, 1, 1)

		self.formLayout.addWidget(self.first_name, 2, 0)
		self.formLayout.addWidget(self.last_name, 2, 1)

		self.formLayout.addWidget(self.phone_number, 3, 0)
		self.formLayout.addWidget(self.email, 3, 1)

		self.formLayout.addWidget(self.password1, 4, 0)
		self.formLayout.addWidget(self.password2, 4, 1)

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
				if self.admission_num.placeHolderText not in all_usernames:
					if self.gender.text() != self.gender.placeHolderText:
						if len(self.phone_number.text()) >= phone_length:
							if self.email.text():
								if len(self.password1.text()) >= password_length and len(self.password2.text()) >= password_length:
									if self.password1.text() == self.password2.text():
										new_user = models.User.objects.create_student(
											first_name=self.first_name.text(),
											last_name=self.last_name.text(),
											avatar=self.image.imagePath(),
											gender=self.gender.text(),
											username=self.admission_num.placeHolderText,
											email=self.email.text(),
											phone=self.phone_number.text(),
											is_student=True,
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
					message = f'{self.admission_num.placeHolderText} already exist, try something different'
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
		all_usernames = models.User.objects.values_list('username', flat=True)

		admission_num = utils.generate_admission_number(all_usernames)

		self.admission_num.placeHolderText = admission_num
		self.first_name.textInput.setText('')
		self.last_name.textInput.setText('')
		self.email.textInput.setText('')
		self.phone_number.textInput.setText('')
		self.password1.textInput.setText('')
		self.password2.textInput.setText('')
		self.image.setPixmap('')


class StudentPromotion(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('Student Promotion')
		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		pass

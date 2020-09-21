from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Custom Modules Imports

from views import utils
from resources.assets.customWidgets import customWidgets
from views import pageConfigurations

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
		# for teacher in allTeachers:
		# 	pass

		self.teacherTables.addRow(
			[
				'Mohammed',
				'Ameen',
				'MD',
				'ameenmohammed2311@gmail.com',
				'12/07/20'
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
		self.infoCardWidth = 1800
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
			width=900,
			height=self.gender.height() * 8
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

		self.formLayout.addWidget(self.image, 0, 4, 4, 4)

		self.formLayout.addWidget(self.phone_number, 1, 0)
		self.formLayout.addWidget(self.email, 1, 1)

		self.formLayout.addWidget(self.username, 2, 0)
		self.formLayout.addWidget(self.gender, 2, 1)
		self.formLayout.addWidget(self.password1, 3, 0)
		self.formLayout.addWidget(self.password2, 3, 1)
		

		self.admissionCardContent.cardLayout.addLayout(self.formLayout)


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

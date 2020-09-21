from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

# Custom Modules Imports

from views import pageConfigurations
from resources.assets.customWidgets import customWidgets

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
		self.studentFormDetailsHeader = customWidgets.CardHeader(
			text='Student Information',
			accent=self.headerBG,
		)

		self.admissionCardContent.cardLayout.addWidget(self.studentFormDetailsHeader)

		# First row

		self.admission_num = customWidgets.TextInput(
			labelText='Admission Number',
			placeHolderText='8642ABC',
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
			width=900,
			height=self.gender.height() * 8
		)

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

		self.formLayout.addWidget(self.admission_num, 0, 0)
		self.formLayout.addWidget(self.school_class, 0, 1)
		self.formLayout.addWidget(self.gender, 1, 0)
		self.formLayout.addWidget(self.section, 1, 1)
		self.formLayout.addWidget(self.image, 0, 4, 4, 4)

		self.formLayout.addWidget(self.first_name, 2, 0)
		self.formLayout.addWidget(self.last_name, 2, 1)
		self.formLayout.addWidget(self.phone_number, 3, 0)
		self.formLayout.addWidget(self.email, 3, 1)

		self.admissionCardContent.cardLayout.addLayout(self.formLayout)


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

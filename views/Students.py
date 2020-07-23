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

		self.studentInfo = customWidgets.CardBasic(
			width=self.infoCardWidth * rightRatio,
			height=self.infoCardHeight,
			accent='orange'
		)

		self.studentInfoHeader = customWidgets.CardHeader(
			'Student Information',
			width=self.studentInfo.width(),
			height=headerHeight,
		)

		self.studentInfo.cardLayout.addWidget(self.studentInfoHeader)

		self.studentSiblings = customWidgets.CardBasic(
			width=self.infoCardWidth * rightRatio,
			height=self.infoCardHeight,
			accent='orange'
		)

		self.studentSiblingsHeader = customWidgets.CardHeader(
			'Student Siblings',
			width=self.studentSiblings.width(),
			height=headerHeight,
		)

		self.studentSiblings.cardLayout.addWidget(self.studentSiblingsHeader)

		self.tabCardWidth, self.tabCardHeight = 500, 400

		self.studentExtras = customWidgets.TabCardBasic(
			width=(self.infoCardWidth * leftRatio) * 3,
			height=self.infoCardHeight
		)

		self.studentExtrasTab = customWidgets.TabBasic()

		self.profile = customWidgets.Tab('Profile')

		self.profileContent = customWidgets.CardBasic(
			width=self.tabCardWidth,
			height=self.tabCardHeight,
			accent='rgba(0, 0, 0, 0)'
		)
		self.profileContent.setMinimumSize(400, 500)

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
		pass


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

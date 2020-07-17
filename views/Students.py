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
		self.infoCardWidth = 600

		self.studentInfo = customWidgets.CardBasic(
			width=self.infoCardWidth,
			height=200,
			accent='blue'
		)

		self.studentInfoHeader = customWidgets.CardHeader(
			'Student Information',
			width=self.studentInfo.width(),
			height=50,
		)

		self.studentInfo.cardLayout.addWidget(self.studentInfoHeader)

		self.studentExtras = customWidgets.CardBasic(
			width=self.infoCardWidth,
			height=420,
			accent='blue'
		)

		self.studentExtrasHeader = customWidgets.CardHeader(
			'Extras',
			width=self.studentExtras.width(),
			height=50,
		)

		self.studentExtrasContent = customWidgets.CardContent(
			width=100,
			height=50,
		)

		self.studentExtras.cardLayout.addWidget(self.studentExtrasHeader)
		self.studentExtras.cardLayout.addWidget(
			self.studentExtrasContent,
			stretch=0,
			alignment=Qt.AlignCenter
		)

		self.studentSiblings = customWidgets.CardBasic(
			width=self.infoCardWidth,
			height=200,
			accent='blue'
		)

		self.studentSiblingsHeader = customWidgets.CardHeader(
			'Student Siblings',
			width=self.studentSiblings.width(),
			height=50,
		)

		self.studentSiblings.cardLayout.addWidget(self.studentSiblingsHeader)

		self.groupLayout.addWidget(self.studentInfo, 1, 0)
		self.groupLayout.addWidget(self.studentSiblings, 2, 0)
		self.groupLayout.addWidget(self.studentExtras, 1, 1, 2, 2)


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

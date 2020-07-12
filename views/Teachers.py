from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Custom Modules Imports

from views import utils
from resources.assets.customWidgets import customWidgets

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
				'Registered By',
				'Date Joined',
				'View'
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
				'MD',
				'12/07/20'
			],
			[
				('View', self.viewUser, '#C13A3A')
			]
		)

	def viewUser(self):
		pass


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

		self.initalization()

	def initalization(self):
		pass


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

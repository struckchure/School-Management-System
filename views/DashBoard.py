from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

# Custom Modules Imports

from views import pageConfigurations
from resources.assets.customWidgets import customWidgets

# Custom Modules End


'''
	DashBoard Views
'''


class DashBoard(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
		self.groupLayout.setSpacing(20)
		
		self.studentButton = customWidgets.DashButton('Students', 100, buttonIcon='resources/assets/images/icons/group.png')
		self.teacherButton = customWidgets.DashButton('Teachers', 15, buttonIcon='resources/assets/images/icons/group2.png', borderColor='green')
		self.groupButton = customWidgets.DashButton('Groups', 10, buttonIcon='resources/assets/images/icons/group3.png', borderColor='green')
		self.clubsButton = customWidgets.DashButton('Clubs', 20, buttonIcon='resources/assets/images/icons/group4.png', borderColor='green')

		self.groupLayout.addWidget(self.studentButton, 0, 0)
		self.groupLayout.addWidget(self.teacherButton, 0, 1)
		self.groupLayout.addWidget(self.groupButton, 0, 2)
		self.groupLayout.addWidget(self.clubsButton, 0, 3)

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		pass

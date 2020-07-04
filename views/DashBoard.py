from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


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

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		self.groupLayout.setSpacing(0)

		self.groupLayout.addWidget(customWidgets.DashButton())

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		pass

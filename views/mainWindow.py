'''
	-_- Authors -_-
	Names - Mohammed Al Ameen Bolutife, Omoyajowo Solomon
	E-Mails - ameenmohammed2311@gmail.com, solo@gamil.com
	GitHub - Mohammed2702, Soloskido
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


# Custom Modules Imports

# Custom Modeles End


class Login(QGroupBox):
	def __init__(self):
		QGroupBox.__init__(self)

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop)

		self.setLayout(self.groupLayout)

		self.initialization()

	def initialization(self):
		self.leftPageWidth = 0.4
		self.rightPageWidth = 0.6

		self.mainPage()
		self.leftPage()
		self.rightPage()

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignCenter)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setMinimumSize(700, 600)
		self.mainPageGroup.setLayout(self.mainPageLayout)
		self.mainPageGroup.setObjectName('mainPageGroup')
		self.mainPageGroup.setStyleSheet(
			'''
				QGroupBox#mainPageGroup {
					border-radius: 5px;
					border: 0px;
				}
			'''
		)

		self.groupLayout.addWidget(self.mainPageGroup)

	def leftPage(self):
		self.leftPageLayout = QHBoxLayout()
		self.leftPageLayout.setContentsMargins(0, 0, 0, 0)
		self.leftPageLayout.setAlignment(Qt.AlignCenter)

		self.leftPageGroup = QGroupBox()
		self.leftPageGroup.setLayout(self.leftPageLayout)
		self.leftPageGroup.setFixedWidth(int(self.leftPageWidth * self.mainPageGroup.width()))
		self.leftPageGroup.setObjectName('leftPageGroup')
		self.leftPageGroup.setStyleSheet(
			'''
				QGroupBox#leftPageGroup {
					background-color: #EC2727;
				}
			'''
		)

		self.mainPageLayout.addWidget(self.leftPageGroup)

	def rightPage(self):
		self.rightPageLayout = QHBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setLayout(self.rightPageLayout)
		self.rightPageGroup.setFixedWidth(int(self.rightPageWidth * self.mainPageGroup.width()))
		self.rightPageGroup.setObjectName('rightPageGroup')
		self.rightPageGroup.setStyleSheet(
			'''
				QGroupBox#rightPageGroup {
					background-color: #FEE4E4;
				}
			'''
		)

		self.mainPageLayout.addWidget(self.rightPageGroup)

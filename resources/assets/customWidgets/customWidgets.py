from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class NavBarButtons(QPushButton):
	def __init__(text, image):
		super(NavBarButtons, self).__init__()

		self.buttonText = text
		self.buttonImage = image



class NavBarUser(QGroupBox):
	def __init__(self, imagePath='resources/assets/images/icons/delete.png', user='John Doe'):
		super(NavBarUser, self).__init__()

		self.imagePath = imagePath
		self.user = user

		self.itemLayout = QGridLayout()
		self.itemLayout.setContentsMargins(0, 0, 0, 0)
		self.itemLayout.setSpacing(0)
		self.itemLayout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.itemLayout)
		self.setObjectName('NavBarUser')
		self.setStyleSheet(
			'''
				QGroupBox#NavBarUser {
					border: 0px;
					border-bottom: 1px solid grey;
					background-color: rgba(0, 0, 0, 0);
				}
			'''
		)

		self.initialization()

	def initialization(self):
		self.imageSet()
		self.userInfoSet()

	def imageSet(self):
		self.imageLayout = QVBoxLayout()
		self.imageLayout.setAlignment(Qt.AlignCenter)

		self.imagePixmap = QPixmap(self.imagePath)
		self.userImage = QLabel()
		self.userImage.setPixmap(self.imagePixmap)
		self.userImage.setAlignment(Qt.AlignCenter)
		self.userImage.setObjectName('userImage')
		self.userImage.setMaximumSize(80, 80)
		self.userImage.setStyleSheet(
			'''
				QLabel#userImage {
					border: 2px solid #DAA5A5;
					border-radius: 40px;
				}
			'''
		)
		
		self.imageLayout.addWidget(self.userImage)

		self.imageGroup = QGroupBox()
		# self.imageGroup.setMaximumWidth(300)
		self.imageGroup.setLayout(self.imageLayout)
		self.imageGroup.setObjectName('imageGroup')
		self.imageGroup.setStyleSheet(
			'''
				QGroupBox#imageGroup {
					border: 0px;
					border-radius: 50px;
				}
			'''
		)

		self.itemLayout.addWidget(self.imageGroup, 0, 0)

	def userInfoSet(self):
		self.infoLayout = QVBoxLayout()
		self.infoLayout.setAlignment(Qt.AlignCenter)

		self.userInfo = QLabel(self.user.get_full_name())
		self.userInfo.setAlignment(Qt.AlignLeft)
		self.userInfo.setObjectName('userInfo')
		self.userInfo.setMaximumSize(200, 50)
		self.userInfo.setStyleSheet(
			'''
				QLabel#userInfo {
					border: 0px;
					color: white;
					font-family: Verdana;
				}
			'''
		)
		
		self.imageLayout.addWidget(self.userInfo)

		self.infoGroup = QGroupBox()
		self.infoGroup.setLayout(self.imageLayout)
		self.infoGroup.setObjectName('infoGroup')
		self.infoGroup.setStyleSheet(
			'''
				QGroupBox#infoGroup {
					border: 0px;
				}
			'''
		)

		self.itemLayout.addWidget(self.infoGroup, 1, 0)

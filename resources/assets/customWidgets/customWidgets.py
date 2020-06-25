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
	def __init__(self, imagePath='resources/assets/images/icons/039-physics.png', user='John Doe'):
		super(NavBarUser, self).__init__()

		self.imagePath = imagePath
		self.user = user

		self.itemLayout = QVBoxLayout()
		self.itemLayout.setContentsMargins(0, 0, 0, 0)
		# self.itemLayout.setSpacing(0)
		self.itemLayout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.itemLayout)
		self.setObjectName('NavBarUser')
		self.setStyleSheet(
			'''
				QGroupBox#NavBarUser {
					border: 0px;
					border-bottom: 1px solid grey;
					padding-top: 20px;
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
		
		self.itemLayout.addWidget(self.userImage, stretch=0, alignment=Qt.AlignCenter)

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
		
		self.itemLayout.addWidget(self.userInfo, stretch=0, alignment=Qt.AlignCenter)


class PushNotification(QSystemTrayIcon):
	def __init__(self, icon=QIcon('resources/assests/images/heart.png'), parent=None):
		QSystemTrayIcon.__init__(self, icon, parent)
		menu = QMenu(parent)
		exitAction = menu.addAction("Exit")
		self.setContextMenu(menu)


class PopUp(QWidget):
	def __init__(self, title='School Manager', body='Body', buttonText='&Ok, thanks', parent=None):
		super(QWidget, self).__init__(parent=None)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)

		self.title = title
		self.body = body
		self.buttonText = buttonText

		self.windowLayout = QVBoxLayout()

		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.resize(300, 170)
		self.setMaximumSize(600, 600)
		resolution = QDesktopWidget().availableGeometry().center()
		qr = self.frameGeometry()
		qr.moveCenter(resolution)
		self.move(qr.topLeft())
		self.setLayout(self.windowLayout)

		self.initialization()

	def initialization(self):
		self.titleLabel = QLabel(self.title)
		self.titleLabel.setAlignment(Qt.AlignCenter)
		self.titleLabel.setStyleSheet(
			'''
				QLabel {
					padding: 5px;
					border: 0px;
					border-bottom: 1px solid grey;
				}
			'''
		)
		self.titleLabel.setFixedSize(200, 40)
		self.windowLayout.addWidget(self.titleLabel, stretch=0, alignment=Qt.AlignCenter)

		self.bodyLabel = QLabel(self.body)
		self.bodyLabel.setObjectName('bodyLabel')
		self.bodyLabel.setAlignment(Qt.AlignCenter)
		self.bodyLabel.setWordWrap(True)
		self.bodyLabel.setMaximumSize(500, 500)
		self.windowLayout.addWidget(self.bodyLabel, stretch=0, alignment=Qt.AlignCenter)

		self.spacerLabel = QLabel()
		self.spacerLabel.setFixedWidth(30)
		self.windowLayout.addWidget(self.spacerLabel, stretch=0, alignment=Qt.AlignCenter)

		self.closeButton = QPushButton(self.buttonText)
		self.closeButton.setObjectName('login')
		self.closeButton.setFixedSize(150, 30)
		self.closeButton.clicked.connect(self.close)
		self.windowLayout.addWidget(self.closeButton, stretch=0, alignment=Qt.AlignHCenter | Qt.AlignBottom)

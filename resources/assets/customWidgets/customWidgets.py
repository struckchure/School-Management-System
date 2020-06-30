from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# Custom Modules Imports

from views import pageConfigurations

# Custom Modules End

'''
	Home Views
'''

class NavBar(QGroupBox):
	def __init__(self, user):
		QGroupBox.__init__(self)

		self.user = user

		self.groupLayout = QHBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)

		blurRadius = 20
		offSet = 2.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setObjectName('navBar')
		self.setLayout(self.groupLayout)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		# self.setMaximumHeight(pageConfigurations.navBarHeight)
		self.setFixedHeight(pageConfigurations.navBarHeight)


class SideBarTitle(QLabel):
	def __init__(self, text):
		QLabel.__init__(self)

		self.text = text

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setWordWrap(True)
		self.setText(self.text)
		self.setAlignment(Qt.AlignCenter)
		self.setObjectName('sideBarTitle')


class SideBarUser(QGroupBox):
	def __init__(self, imagePath='resources/assets/images/icons/039-physics.png', user='John Doe'):
		QGroupBox.__init__(self)

		self.imagePath = imagePath
		self.user = user

		self.itemLayout = QVBoxLayout()
		self.itemLayout.setContentsMargins(0, 0, 0, 0)
		self.itemLayout.setAlignment(Qt.AlignCenter)

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setLayout(self.itemLayout)
		self.setObjectName('sideBarUser')

		self.initialization()

	def initialization(self):
		# self.imageSet()
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
		
		self.itemLayout.addWidget(self.userInfo, stretch=0, alignment=Qt.AlignCenter)


class SideBarSection(QGroupBox):
	def __init__(self, title='Menu', width=100):
		QGroupBox.__init__(self)

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setAlignment(Qt.AlignLeft)
		self.groupLayout.setSpacing(10)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setFixedWidth(width * 0.85)
		self.setObjectName('sideBarSection')
		self.setLayout(self.groupLayout)

		self.titleLabel = QLabel(f'{title}')
		self.titleLabel.setAlignment(Qt.AlignLeft)
		self.titleLabel.setObjectName('sideBarSectionTitle')
		self.titleLabel.setFixedSize(width * 0.85, 30)
		self.groupLayout.addWidget(self.titleLabel, stretch=0, alignment=Qt.AlignLeft)

		self.initialization()

	def initialization(self):
		self.widgetLayout = QVBoxLayout()
		self.widgetLayout.setAlignment(Qt.AlignLeft)

		self.widgetGroup = QGroupBox()
		self.widgetGroup.setLayout(self.widgetLayout)
		self.widgetGroup.setObjectName('widgetGroup')
		self.groupLayout.addWidget(self.widgetGroup, stretch=0, alignment=Qt.AlignTop | Qt.AlignLeft)


class SideBarButton(QPushButton):
	def __init__(self, title, image='resources/assets/images/icons/039-physics.png'):
		QPushButton.__init__(self, QIcon(image), title)

		# self.buttonText = title
		# self.buttonImage = QIcon(image)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setFixedHeight(40)
		# self.setText(self.buttonText)
		# self.setIcon(self.buttonIcon)
		self.setObjectName('sideBarButton')


class SideBar(QScrollArea):
	def __init__(self):
		QScrollArea.__init__(self)

		self.sideBarLayout = QVBoxLayout()
		self.sideBarLayout.setAlignment(Qt.AlignCenter)

		self.sideBarGroup = QGroupBox()
		self.sideBarGroup.setFixedHeight(900)
		self.sideBarGroup.setLayout(self.sideBarLayout)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setWidget(self.sideBarGroup)
		self.setWidgetResizable(True)
		self.setMaximumSize(1200, 200)
		self.setObjectName('sideBar')
		self.showMaximized()


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

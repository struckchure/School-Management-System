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

		blurRadius = 30
		offSet = 2.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setObjectName('navBar')
		self.setLayout(self.groupLayout)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setFixedHeight(pageConfigurations.navBarHeight)


class SideBarTitle(QLabel):
	def __init__(self, text):
		QLabel.__init__(self, text)

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setWordWrap(True)
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
		self.userInfoSet()

	def userInfoSet(self):
		self.infoLayout = QVBoxLayout()
		self.infoLayout.setAlignment(Qt.AlignCenter)

		self.userInfo = QLabel(self.user.get_full_name())
		self.userInfo.setAlignment(Qt.AlignLeft)
		self.userInfo.setObjectName('userInfo')
		self.userInfo.setMaximumSize(200, 50)
		
		self.itemLayout.addWidget(self.userInfo, stretch=0, alignment=Qt.AlignCenter)


class SideBarSection(QGroupBox):
	def __init__(self, title='Menu'):
		QGroupBox.__init__(self)

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setAlignment(Qt.AlignLeft)
		self.groupLayout.setSpacing(0)

		widgetWidthRatio = pageConfigurations.sideBarWidgetWidthRatio
		qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setObjectName('sideBarSection')
		self.setLayout(self.groupLayout)
		print(self.width() * widgetWidthRatio)
		self.titleLabel = QLabel(f'{title}')
		self.titleLabel.setAlignment(Qt.AlignLeft)
		self.titleLabel.setObjectName('sideBarSectionTitle')
		self.titleLabel.setFixedSize(self.width() * widgetWidthRatio, 30)
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

		buttonWidth = pageConfigurations.sideBarSize[0] * pageConfigurations.sideBarWidgetWidthRatio
		qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setFixedSize(buttonWidth, 40)
		self.setObjectName('sideBarButton')


class SideBar(QScrollArea):
	def __init__(self):
		QScrollArea.__init__(self)

		self.sideBarLayout = QVBoxLayout()
		self.sideBarLayout.setAlignment(Qt.AlignTop)

		self.sideBarGroup = QGroupBox()
		self.sideBarGroup.setObjectName('sideBarGroup')
		self.sideBarGroup.setMinimumHeight(400)
		self.sideBarGroup.setLayout(self.sideBarLayout)
		
		sideBarSize = pageConfigurations.sideBarSize
		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		
		self.setStyleSheet(qss)
		self.setWidget(self.sideBarGroup)
		self.setWidgetResizable(True)
		self.setMaximumSize(sideBarSize[0], sideBarSize[1])
		self.setObjectName('sideBarScroll')
		self.showMaximized()


class DashButton(QPushButton, QHBoxLayout):
	def __init__(self):
		super(DashButton, self).__init__()

		blurRadius = 30
		offSet = 2.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setContentsMargins(0, 0, 0, 0)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setObjectName('dashButton')
		self.setMinimumSize(250, 100)


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
		self.titleLabel.setObjectName('popUpTitle')
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

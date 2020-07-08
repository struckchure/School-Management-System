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
		QLabel.__init__(self)

		self.text = text

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setWordWrap(True)
		self.setMaximumSize(200, 50)
		self.setText(self.text)
		self.setAlignment(Qt.AlignCenter)
		self.setObjectName('sideBarTitle')


class SideBarSection(QGroupBox):
	def __init__(self, title='Menu', width=pageConfigurations.sideBarSectionWidth):
		QGroupBox.__init__(self)

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setAlignment(Qt.AlignLeft)
		self.groupLayout.setSpacing(5)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setFixedWidth(width)
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
		self.widgetGroup.setFixedWidth(200)
		self.widgetGroup.setLayout(self.widgetLayout)
		self.widgetGroup.setObjectName('widgetGroup')
		self.groupLayout.addWidget(self.widgetGroup, stretch=0, alignment=Qt.AlignTop | Qt.AlignLeft)


class SideBarButton(QPushButton):
	def __init__(self, title, image='resources/assets/images/icons/039-physics.png'):
		QPushButton.__init__(self, QIcon(image), title)

		ratio = 0.7
		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setFixedSize(pageConfigurations.sideBarSize[0] * ratio, pageConfigurations.sideBarButtonHeight)
		self.setObjectName('sideBarButton')


class SideBar(QScrollArea):
	def __init__(self):
		QScrollArea.__init__(self)

		self.sideBarLayout = QVBoxLayout()
		self.sideBarLayout.setAlignment(Qt.AlignTop)

		self.sideBarGroup = QGroupBox()
		self.sideBarGroup.setObjectName('sideBarGroup')
		self.sideBarGroup.setMinimumSize(230, 400)
		self.sideBarGroup.setLayout(self.sideBarLayout)
		
		sideBarSize = pageConfigurations.sideBarSize
		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		
		self.setStyleSheet(qss)
		self.setWidget(self.sideBarGroup)
		self.setWidgetResizable(True)
		self.setMaximumSize(sideBarSize[0], sideBarSize[1])
		self.setObjectName('sideBarScroll')
		self.showMaximized()

'''
	Usage:
		self.teacherButton = customWidgets.DashButton(
		buttonText='Teachers',
		buttonValue=15,
		buttonIcon='resources/assets/images/icons/local_library_black.png',
		borderColor='green')
'''

class DashButton(QPushButton, QHBoxLayout):
	def __init__(self, buttonText, buttonValue, buttonIcon='resources/assets/images/icons/view.png', borderColor='#1554BD'):
		super(DashButton, self).__init__()

		self.buttonText = str(buttonText)
		self.buttonValue = str(buttonValue)
		self.buttonIcon = buttonIcon
		self.borderColor = str(borderColor)
		
		blurRadius = 20
		xOffset = 0.1
		yOffset = 0.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setXOffset(xOffset)
		self.groupGraphicsEffect.setYOffset(yOffset)

		self.buttonLayout = QHBoxLayout()
		self.buttonLayout.setAlignment(Qt.AlignTop | Qt.AlignVCenter)

		iconWidth, iconHeight = pageConfigurations.DashButtonSize
		qss = open('resources/assets/qss/boostrap.qss', 'r').read().split('/* idDashButtonStart */')[1].split('/* idDashButtonStart */')[0].replace('#1554BD', borderColor)

		self.setStyleSheet(qss)
		self.setIcon(QIcon(QPixmap(self.buttonIcon)))
		self.setLayout(self.buttonLayout)
		self.setContentsMargins(0, 0, 0, 0)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setObjectName('dashButton')
		self.setIconSize(QSize(iconWidth, iconHeight))
		self.setMinimumSize(230, 65)
		self.setMaximumSize(250, 100)

		self.initialization()

	def initialization(self):
		self.leftLabel()
		self.rightLabel()

	def leftLabel(self):
		self.leftLayout = QVBoxLayout()
		self.leftLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		buttonRatio = 0.4

		self.buttonTextLabel = QLabel(self.buttonText)
		self.buttonTextLabel.setObjectName('dashText')
		self.buttonTextLabel.setMaximumSize(self.width() * buttonRatio, self.height())
		self.leftLayout.addWidget(self.buttonTextLabel)

		self.buttonIconLabel = QLabel(self.buttonValue)
		self.buttonIconLabel.setObjectName('dashValue')
		self.buttonIconLabel.setMaximumSize(self.width() * buttonRatio, self.height())
		self.leftLayout.addWidget(self.buttonIconLabel)

		self.buttonLayout.addLayout(self.leftLayout)

	def rightLabel(self):
		self.rightLayout = QVBoxLayout()
		self.rightLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		buttonRatio = 0.4
		

		self.buttonTextLabel = QLabel()
		self.buttonTextLabel.setMaximumSize(self.width() * buttonRatio, self.height() * buttonRatio)
		self.rightLayout.addWidget(self.buttonTextLabel)

		self.buttonLayout.addLayout(self.rightLayout)


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


class PageCrumb(QLabel):
	def __init__(self, title=''):
		super(PageCrumb, self).__init__(title)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		
		self.setStyleSheet(qss)
		# self.setMaximumSize(100, 45)
		self.setFixedSize(500, 45)
		self.setObjectName('pageCrumb')

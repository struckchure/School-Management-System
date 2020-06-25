from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from datetime import datetime


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


class PushNotification(QSystemTrayIcon):
	def __init__(self, icon=QIcon('resources/assests/images/heart.png'), parent=None):
		QSystemTrayIcon.__init__(self, icon, parent)
		menu = QMenu(parent)
		exitAction = menu.addAction("Exit")
		self.setContextMenu(menu)


class PopUp(QWidget):
	def __init__(self, title='School Manager', body='Ping!!!'):
		QWidget.__init__(self)

		self.windowLayout = QVBoxLayout()
		self.windowLayout.setContentsMargins(0, 0, 0, 0)

		resolution = QDesktopWidget().availableGeometry().center()
		qr = self.frameGeometry()
		qr.moveCenter(resolution)

		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.move(qr.topLeft())
		self.setLayout(self.windowLayout)
		self.resize(200, 200)

		self.initialization()

	def initialization(self):
		self.closeButton = QPushButton('&x')
		self.closeButton.setFixedSize(20, 20)
		self.closeButton.clicked.connect(self.close)
		self.windowLayout.addWidget(self.closeButton, stretch=0, alignment=Qt.AlignTop|Qt.AlignRight)


class Notification(QWidget):
    signNotifyClose = pyqtSignal(str)

    def __init__(self, parent = None):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        super(QWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #убирает заголовок, поверх всех окон (| QtCore.Qt.WindowStaysOnTopHint)
        self.resize(200, 200)
        resolution = QDesktopWidget().availableGeometry().center()
        qr = self.frameGeometry()
        qr.moveCenter(resolution)
        self.vboxMainLayout = QVBoxLayout() # layout contain notifications
        self.move(qr.topLeft())
        self.setLayout(self.vboxMainLayout)

        self.closeButton = QPushButton('&X')
        self.closeButton.setFixedSize(50, 50)
        self.closeButton.clicked.connect(self.close)
        self.vboxMainLayout.addWidget(self.closeButton, stretch=0, alignment=Qt.AlignTop|Qt.AlignRight)
        # screenWidth = resolution.width()
        # screenHeight = resolution.height()
        # print(self.LOG_TAG + "width: " + str(resolution.width()) + " height: " + str(resolution.height()))
        self.count = 0 # Счетчик уведомлений
        self.timer = 3


    def setNotify(self, title, notify):
        count = self.count
        title = QLabel()
        title.setStyleSheet("border: 1px solid #000")
        title.setText(title)
        title.setStyleSheet("font-family: 'Roboto', sans-serif; font-size: 14px; font-weight: bold; padding: 0;")

        text = QLabel()
        text.setText(notify)
        text.setStyleSheet("font-family: 'Roboto', sans-serif; font-size: 12px; font-weight: normal; padding: 0;")

        gridNotify = QGridLayout()
        gridNotify.addWidget(title, 0, 0)
        gridNotify.addWidget(text, 1, 0)

        buttonClose = QPushButton()
        buttonClose.clicked.connect(self.deleteWidgets)
        buttonClose.setIcon(QIcon("resources/assests/images/delete.png"))
        buttonClose.setFlat(False)
        buttonClose.setMaximumWidth(14)
        buttonClose.setMaximumHeight(14)

        gridClose = QGridLayout()
        gridClose.addWidget(buttonClose, 0, 0)

        gridLayoutMain = QGridLayout()
        gridLayoutMain.setColumnStretch(0,1)
        gridLayoutMain.setColumnStretch(0,2)
        gridLayoutMain.setColumnStretch(0,3)
        gridLayoutMain.addLayout(gridClose, 0, 4)
        gridLayoutMain.addLayout(gridNotify, 0, 0)

        self.count += 1

        self.vboxMainLayout.addLayout(gridLayoutMain)
        self.show()
        threading.Timer(2, self.delete, args=(gridLayoutMain,)).start()

    def delete(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                print("")
                self.delete(item.layout())

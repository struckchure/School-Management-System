from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


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


class FirstRow(QPushButton):
	def __init__(self, head, total_no, icon='resources/assets/images/icons/group.png'):
		QPushButton.__init__(self)

		self.hd = head
		self.tln = total_no
		self.icn = icon

		blurradius = 160
		offset = 17
		color = QColor(0, 0, 0, 255 * .3)

		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(blurradius)
		self.shadow_effect.setOffset(offset)
		self.shadow_effect.setColor(color)
		self.setGraphicsEffect(self.shadow_effect)

		width = 230
		height = 70

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setContentsMargins(0, 0, 0, 0)
		self.setMinimumSize(width, height)
		self.setObjectName('firstRow')
		self.setIcon(QIcon(self.icn))
		self.setIconSize(QSize(50, 50))

		self.assist_layout = QHBoxLayout()
		self.assist_layout.setContentsMargins(0, 0, 0, 0)

		self.firstRow = QVBoxLayout()
		self.firstRow.setSpacing(0)
		self.firstRow.setContentsMargins(0, 0, 0, 0)

		self.head = QLabel(str(self.hd))
		self.head.setMaximumHeight(11)
		self.head.setObjectName("headText")
		self.firstRow.addWidget(self.head)

		self.total = QLabel(str(self.tln))
		self.total.setMaximumHeight(20)
		self.total.setObjectName("totalText")
		self.firstRow.addWidget(self.total)

		self.assist_layout.addLayout(self.firstRow)

		self.box_icon = QLabel()
		self.box_icon.setAlignment(Qt.AlignRight)
		self.box_icon.setContentsMargins(0, 15, 24, 0)
		box_icon = QPixmap(self.icn)
		self.box_icon.setPixmap(box_icon)
		#self.assist_layout.addWidget(self.box_icon)

		self.setLayout(self.assist_layout)


class SecondRow(QGroupBox):
	def __init__(self, title, eventName):
		QGroupBox.__init__(self)
		self.eventName = eventName
		self.title = title

		blurradius = 200
		offset = 16
		color = QColor(0, 0, 0, 255 * .3)

		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(blurradius)
		self.shadow_effect.setOffset(offset)
		self.shadow_effect.setColor(color)
		self.setGraphicsEffect(self.shadow_effect)

		width = 480

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
		self.setContentsMargins(0, 0, 0, 0)
		self.setMaximumWidth(width)
		self.setObjectName('secondRow')

		self.secondRow = QVBoxLayout()
		self.secondRow.setAlignment(Qt.AlignTop)
		self.secondRow.setSpacing(0)
		self.secondRow.setContentsMargins(0, 0, 0, 0)

		#layout for title and add button
		self.box_heading = QHBoxLayout()
		self.box_heading.setSpacing(0)
		self.box_heading.setContentsMargins(0, 0, 0, 0)

		self.box_title = QLabel(self.title)
		self.box_title.setMinimumSize(440, 35)
		self.box_title.setObjectName('boxTitle')
		#self.box_title.setAlignment(Qt.AlignTop)
		self.box_heading.addWidget(self.box_title)

		self.add_button = QPushButton()
		self.add_button.setIcon(QIcon('resources/assets/images/icons/add_icon.png'))
		self.add_button.setIconSize(QSize(20, 20))
		self.add_button.setMinimumHeight(35)
		#self.add_button.clicked.connect(self.addEvent)
		self.add_button.setObjectName('addButton')
		self.box_heading.addWidget(self.add_button)

		self.secondRow.addLayout(self.box_heading)

		self.eventList(self.eventName)

		self.setLayout(self.secondRow)

	def eventList(self, eventName):
		# layout for lists
		self.list_layout = QHBoxLayout()
		self.list_layout.setSpacing(0)
		self.list_layout.setContentsMargins(0, 0, 0, 0)

		height = 30

		self.event_name = QLabel(str(eventName))
		self.event_name.setMinimumHeight(height)
		self.event_name.setWordWrap(True)
		self.event_name.setObjectName('event')
		self.list_layout.addWidget(self.event_name)

		self.edit_list_btn = QPushButton()
		self.edit_list_btn.setMaximumSize(30, height)
		self.edit_list_btn.setIcon(QIcon('resources/assets/images/icons/edit_icon.png'))
		self.edit_list_btn.setIconSize(QSize(15, 15))
		self.edit_list_btn.setObjectName('listBtn')
		self.list_layout.addWidget(self.edit_list_btn)

		self.delete_list_btn = QPushButton()
		self.delete_list_btn.setMaximumSize(30, height)
		self.delete_list_btn.setIcon(QIcon('resources/assets/images/icons/delete_icon.png'))
		self.delete_list_btn.setIconSize(QSize(15, 15))
		self.delete_list_btn.setObjectName('listBtn')
		self.list_layout.addWidget(self.delete_list_btn)

		self.event_scroll = QScrollArea()
		self.event_scroll.setMaximumHeight(50)
		self.event_scroll.setWidgetResizable(True)
		self.event_scroll.setObjectName('eventScroll')
		self.event_scroll.setLayout(self.list_layout)

		self.secondRow.addWidget(self.event_scroll)


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

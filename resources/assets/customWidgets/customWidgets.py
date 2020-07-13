from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# Custom Modules Imports

from views import pageConfigurations
from views import utils

# Custom Modules End


class SleepCells(QThread):
	finished = pyqtSignal()
	intReady = pyqtSignal(int)

	@pyqtSlot()
	def procCounter(self):
		for i in range(1):
			self.intReady.emit(i)
		
		self.finished.emit()


class Cell(SleepCells):
	def __init__(self, function):
		SleepCells.__init__(self)

		self.function = function
		self.cellThread = QThread()

		self.intReady.connect(self.function)
		self.moveToThread(self.cellThread)
		self.finished.connect(self.cellThread.quit)

		self.cellThread.started.connect(self.procCounter)

	def startCell(self):
		self.cellThread.start()


class LineEditButton(QGroupBox):
	def __init__(self, placeHolder, icon, iconText=''):
		super(LineEditButton, self).__init__()

		self.placeHolder = placeHolder
		self.icon = QIcon(icon)
		self.iconText = iconText

		self.groupLayout = QHBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignVCenter)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.groupLayout)
		self.setFixedHeight(30)
		self.setObjectName('lineEditBox')

		self.initialization()

	def initialization(self):
		self.linedEdit = QLineEdit()
		self.linedEdit.setObjectName('lineEdit-Normal')
		self.linedEdit.setPlaceholderText(self.placeHolder)
		self.linedEdit.setFixedHeight(self.height())
		self.linedEdit.setMaximumWidth(250)

		self.groupLayout.addWidget(self.linedEdit)

		self.button = QPushButton(self.icon, self.iconText)
		self.button.clicked.connect(self.text)
		self.button.setObjectName('login')
		self.button.setFixedHeight(self.height())
		self.button.setMaximumWidth(250)
		
		self.groupLayout.addWidget(self.button)

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Return:
			self.text()

	def text(self):
		return self.linedEdit.text()


class NavBarUser(QPushButton, QHBoxLayout):
	def __init__(self, user, default_image='resources/assets/images/icons/user.png'):
		super(NavBarUser, self).__init__()

		self.user = user
		self.userIcon = QIcon(default_image)

		navSideMargins = pageConfigurations.navSideMargins

		self.navBarUserLayout = QGridLayout()
		self.navBarUserLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.navBarUserLayout)
		self.setMaximumWidth(pageConfigurations.sideBarSize[0])
		self.setIcon(self.userIcon)
		self.setText(self.user.get_full_name())
		self.setIconSize(QSize(25, 20))
		self.setObjectName('navBarUser')

		self.initialization()

	def initialization(self):
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showUserOptions)

		profileIcon = QIcon('resources/assets/images/icons/local_library_black.png')
		logoutIcon = QIcon('resources/assets/images/icons/local_post_office_black.png')

		self.userOptions = QMenu(self)

		self.profileAction = QAction(QIcon(profileIcon), 'Profile', self)
		self.profileAction.triggered.connect(self.profileView)

		self.logoutAction = QAction(QIcon(logoutIcon), 'Logout', self)
		self.logoutAction.triggered.connect(self.logoutView)

		self.userOptions.addAction(self.profileAction)
		self.userOptions.addAction(self.logoutAction)

	# def keyPressEvent(self, e):
	# 	if e.key() == Qt.RightButton:
	# 		self.showUserOptions()

	def showUserOptions(self, point):
		point.setX(point.x() - 10)
		point.setY(point.y())

		self.userOptions.exec_(self.mapToGlobal(point))

	def profileView(self):
		print('slots')

	def logoutView(self):
		print('slots')


class NavBar(QGroupBox):
	def __init__(self, user):
		QGroupBox.__init__(self)

		self.user = user

		navSideMargins = pageConfigurations.navSideMargins
		
		self.groupLayout = QHBoxLayout()
		self.groupLayout.setSpacing(5)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)

		blurRadius = 30
		offSet = 0.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		self.setObjectName('navBar')
		self.setLayout(self.groupLayout)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setFixedHeight(pageConfigurations.navBarHeight)

		self.initialization()

	def initialization(self):
		height = self.height() * 0.7

		self.searchBox = LineEditButton(
			placeHolder='search ...',
			icon='resources/assets/images/icons/ic_keyboard_arrow_right_white_48dp.png',
		)
		self.searchBox.linedEdit.setFixedWidth(200)
		self.searchBox.button.setToolTip('search')

		self.groupLayout.addWidget(
			self.searchBox,
			stretch=0,
			alignment=Qt.AlignLeft | Qt.AlignVCenter
		)

		self.navUser = NavBarUser(self.user)

		self.groupLayout.addWidget(
			self.navUser,
			stretch=0,
			alignment=Qt.AlignRight | Qt.AlignVCenter
		)


class SideBarTitle(QLabel):
	def __init__(self, text):
		QLabel.__init__(self)

		self.text = text

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

		self.title = title

		ratio = 0.7

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

		self.setWidget(self.sideBarGroup)
		self.setWidgetResizable(True)
		self.setMaximumSize(sideBarSize[0], sideBarSize[1])
		self.setObjectName('sideBarScroll')
		self.showMaximized()


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
		qss = open('resources/assets/qss/boostrap.qss', 'r').read().split('/* idDashButtonStart */')[1].split('/* idDashButtonEnd */')[0].replace('#1554BD', self.borderColor)

		self.setStyleSheet(qss)
		self.setIcon(QIcon(QPixmap(self.buttonIcon)))
		self.setLayout(self.buttonLayout)
		self.setContentsMargins(0, 0, 0, 0)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setObjectName('dashButton')
		self.setIconSize(QSize(iconWidth, iconHeight))
		self.setMinimumSize(235, 65)
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

		self.title = title
		self.body = body
		self.buttonText = buttonText

		self.windowLayout = QVBoxLayout()

		qss = open('resources/assets/qss/boostrap.qss', 'r').read()
		self.setStyleSheet(qss)
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

		self.setFixedSize(500, 45)
		self.setObjectName('pageCrumb')


class FirstRow(QPushButton):
	def __init__(self, head, total_no, icon='resources/assets/images/icons/group.png'):
		QPushButton.__init__(self)

		self.hd = head
		self.tln = total_no
		self.icn = icon

		blurradius = 30
		offset = 0.1
		color = QColor(0, 0, 0, 255 * .3)

		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(blurradius)
		self.shadow_effect.setOffset(offset)
		self.shadow_effect.setColor(color)
		self.setGraphicsEffect(self.shadow_effect)

		width = 230
		height = 70

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

		self.setLayout(self.assist_layout)


class Card(QGroupBox):
	def __init__(self, title):
		QGroupBox.__init__(self)
		
		self.title = title

		blurradius = 25
		offset = 0.1

		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(blurradius)
		self.shadow_effect.setOffset(offset)

		width = 480

		self.setGraphicsEffect(self.shadow_effect)
		self.setContentsMargins(0, 0, 0, 0)
		self.setMaximumWidth(width)
		self.setFixedHeight(350)
		self.setObjectName('card')

		self.cardLayout = QVBoxLayout()
		self.cardLayout.setAlignment(Qt.AlignTop)
		self.cardLayout.setSpacing(0)
		self.cardLayout.setContentsMargins(0, 0, 0, 0)

		# Layout for title and add button

		self.box_heading = QHBoxLayout()
		self.box_heading.setSpacing(0)
		self.box_heading.setContentsMargins(0, 0, 0, 0)

		self.box_title = QLabel(self.title)
		self.box_title.setObjectName('boxTitle')
		self.box_title.setFixedSize(self.width(), 35)
		self.box_heading.addWidget(self.box_title, stretch=0, alignment=Qt.AlignLeft)

		self.add_button = QPushButton()
		self.add_button.setObjectName('addButton')
		self.add_button.setIcon(QIcon('resources/assets/images/icons/add_icon.png'))
		self.add_button.setIconSize(QSize(20, 20))
		self.add_button.setFixedSize(30, 35)
		# self.add_button.clicked.connect(self.addEvent)
		self.box_heading.addWidget(self.add_button, stretch=0, alignment=Qt.AlignRight)

		self.cardLayout.addLayout(self.box_heading)

		self.setLayout(self.cardLayout)

		self.event_layout = QVBoxLayout()
		self.event_layout.setAlignment(Qt.AlignTop)
		self.event_layout.setSpacing(0)
		self.event_layout.setContentsMargins(0, 0, 0, 0)

		self.list_layout = QVBoxLayout()
		self.list_layout.setAlignment(Qt.AlignTop)
		self.list_layout.setSpacing(0)
		self.list_layout.setContentsMargins(0, 0, 0, 0)

		self.list_layout.addLayout(self.event_layout)

		self.eventGroup = QGroupBox()
		self.eventGroup.setObjectName('noBorderBox')
		self.eventGroup.setLayout(self.list_layout)

		self.event_scroll = QScrollArea()
		self.event_scroll.setObjectName('eventScroll')
		self.event_scroll.setWidget(self.eventGroup)
		self.event_scroll.setWidgetResizable(True)

		self.cardLayout.addWidget(self.event_scroll)

	def addEvent(self, event):
		height = 100
		buttonRatio = 0.3

		self.eventItemsLayout = QHBoxLayout()
		self.eventItemsLayout.setSpacing(0)
		self.eventItemsLayout.setContentsMargins(0, 0, 0, 0)

		self.eventItemsGroup = QGroupBox()
		self.eventItemsGroup.setLayout(self.eventItemsLayout)
		self.eventItemsGroup.setObjectName('cardChildren')
		self.eventItemsGroup.setMaximumHeight(height)

		self.event_name = QLabel(str(
			utils.paginator(
				event,
				max_word=200,
				show_end=True,
				end_length=5
				)
			)
		)
		self.event_name.setMaximumHeight(height)
		self.event_name.setMaximumWidth(self.width())
		self.event_name.setWordWrap(True)
		self.event_name.setObjectName('event')
		self.eventItemsLayout.addWidget(self.event_name)

		self.edit_list_btn = QPushButton()
		self.edit_list_btn.setFixedSize(25, height * buttonRatio)
		self.edit_list_btn.setIcon(QIcon('resources/assets/images/icons/edit_icon.png'))
		self.edit_list_btn.setIconSize(QSize(15, 15))
		self.edit_list_btn.setObjectName('listBtn')
		self.eventItemsLayout.addWidget(self.edit_list_btn)

		self.delete_list_btn = QPushButton()
		self.delete_list_btn.setFixedSize(25, height * buttonRatio)
		self.delete_list_btn.setIcon(QIcon('resources/assets/images/icons/delete_icon.png'))
		self.delete_list_btn.setIconSize(QSize(15, 15))
		self.delete_list_btn.setObjectName('listBtn')
		self.eventItemsLayout.addWidget(self.delete_list_btn)

		self.event_layout.addWidget(self.eventItemsGroup)

	def addNotice(self, notice):
		height = 100
		buttonRatio = 0.3

		self.noticeItemsLayout = QHBoxLayout()
		self.noticeItemsLayout.setSpacing(0)
		self.noticeItemsLayout.setContentsMargins(0, 0, 0, 0)

		self.noticeItemsGroup = QGroupBox()
		self.noticeItemsGroup.setLayout(self.noticeItemsLayout)
		self.noticeItemsGroup.setObjectName('cardChildren')
		self.noticeItemsGroup.setMaximumHeight(height)

		self.notice_name = QLabel(str(
			utils.paginator(
				notice,
				max_word=300,
				show_end=True,
				end_length=5
				)
			)
		)
		self.notice_name.setMaximumHeight(height)
		self.notice_name.setMaximumWidth(self.width())
		self.notice_name.setWordWrap(True)
		self.notice_name.setObjectName('event')
		self.noticeItemsLayout.addWidget(self.notice_name)

		self.event_layout.addWidget(self.noticeItemsGroup)


'''
	Table
'''


class TableHeader(QLabel):
	def __init__(self, text):
		real_text = str(text)
		text = utils.paginator(
			text,
			max_word=10,
			show_end=True,
			end_length=3
		)

		QLabel.__init__(self, str(text))

		self.setObjectName('tableHeader')
		# self.setToolTip(real_text)
		self.setMaximumSize(pageConfigurations.tableSize[0], pageConfigurations.tableSize[1])


class TableItem(QLabel):
	def __init__(
		self,
		text,
		bold=False,
		tableAccent='background-color: rgba(0, 0, 0, 0);'
		):
		real_text = str(text)
		text = utils.paginator(
			text,
			max_word=10,
			show_end=True,
			end_length=3
		)

		QLabel.__init__(self, str(text))

		if tableAccent != 'background-color: rgba(0, 0, 0, 0)':
			qss = open('resources/assets/qss/boostrap.qss', 'r').read().split(
				'/*tableAccentStart*/'
				)[1].split(
				'/*tableAccentEnd*/'
				)[0].replace(
				'background-color: rgba(0, 0, 0, 0);',
				f'background-color: {tableAccent};'
			)

		self.setStyleSheet(qss)
		self.setObjectName('tableItem')
		# self.setToolTip(real_text)
		self.setMaximumSize(
			pageConfigurations.tableSize[0],
			pageConfigurations.tableSize[1]
		)


class TableButtonChild(QPushButton):
	def __init__(
		self,
		text,
		slot,
		icon='resources/assets/images/icons/ic_event_note_white_48dp.png',
		color='#3E63CC'
		):
		QPushButton.__init__(self, QIcon(icon), text)

		self.slot = slot

		qss = open('resources/assets/qss/boostrap.qss', 'r').read().split(
			'/*tableButtonChildAccentStart*/'
			)[1].split(
			'/*tableButtonChildAccentEnd*/'
			)[0].replace(
			'#3E63CC;',
			f'{color};'
			)
		# qss = open('resources/assets/qss/boostrap.qss', 'r').read()

		self.setStyleSheet(qss)
		self.setObjectName('tableButtonChild')
		self.clicked.connect(self.buttonSlot)
		self.setMaximumSize(
			pageConfigurations.tableSize[0],
			pageConfigurations.tableSize[1]
		)

	def buttonSlot(self):
		return self.slot


class TableButton(QGroupBox):
	def __init__(
		self,
		text,
		slot,
		icon='resources/assets/images/icons/ic_event_note_white_48dp.png',
		color='rgba(0, 0, 0, 0)',
		tableAccent=''
		):
		QGroupBox.__init__(self)

		qss = open('resources/assets/qss/boostrap.qss', 'r').read().split(
			'/*tableAccentStart*/'
			)[1].split(
			'/*tableAccentEnd*/'
			)[0].replace(
			'background-color: rgba(0, 0, 0, 0);',
			f'background-color: {tableAccent};'
			)

		buttonRatio = 0.8

		self.buttonLayout = QVBoxLayout()
		self.buttonLayout.setContentsMargins(0, 0, 0, 0)
		self.buttonLayout.setAlignment(Qt.AlignCenter)

		self.buttonLayout.addWidget(
			TableButtonChild(
				text,
				slot,
				icon=icon,
				color=color
				)
			)

		self.setStyleSheet(qss)
		self.setObjectName('tableButton')
		self.setCheckable(False)
		self.setLayout(self.buttonLayout)
		self.setMaximumSize(
			pageConfigurations.tableSize[0],
			pageConfigurations.tableSize[1]
		)


class TableRow(QGroupBox):
	def __init__(self, row: list, showIndex=True, index='s/n', header=False):
		QGroupBox.__init__(self)

		self.row = row
		self.showIndex = showIndex
		self.index = index
		self.header = header

		self.tableRowLayout = QGridLayout()
		self.tableRowLayout.setSpacing(0)
		self.tableRowLayout.setContentsMargins(0, 0, 0, 0)
		self.tableRowLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

		self.setLayout(self.tableRowLayout)
		self.setObjectName('tableRow')
		self.setMaximumHeight(pageConfigurations.tableSize[0])

		self.initialization()
 
	def initialization(self):
		self.m, self.n = 0, 0

		self.createRowsCell = Cell(self.createRows)
		self.createRowsCell.startCell()

	def createRows(self):
		if self.header:
			if self.showIndex:
				self.tableRowLayout.addWidget(TableHeader(self.index), self.m, self.n)
				self.n += 1

			for i in self.row:
				self.tableRowLayout.addWidget(TableHeader(i), self.m, self.n)
				self.n += 1
		else:
			if self.showIndex:
				self.tableRowLayout.addWidget(TableItem(self.index), self.m, self.n)
				self.n += 1

			for i in self.row:
				self.tableRowLayout.addWidget(TableItem(i), self.m, self.n)
				self.n += 1

		self.m += 1
		self.n = 0


class Table(QGroupBox):
	def __init__(self, tableRows: list, tableButtons=[], showIndex=True, index='s/n'):
		QGroupBox.__init__(self)

		self.tableRows = tableRows
		self.tableButtons = tableButtons
		self.showIndex = showIndex
		self.index = index
		self.currentIndex = 1

		self.tableLayout = QGridLayout()
		self.tableLayout.setSpacing(0)
		self.tableLayout.setContentsMargins(0, 0, 0, 0)
		self.tableLayout.setAlignment(Qt.AlignTop)

		self.setObjectName('table')
		self.setLayout(self.tableLayout)

		self.initialization()

	def initialization(self):
		self.m, self.n = 1, 0

		self.createRowsCell = Cell(self.createRows)
		self.createRowsCell.startCell()

	def createRows(self):
		m, n = 0, 0

		if self.showIndex:
			self.tableLayout.addWidget(TableHeader(self.index), m, n)
			n += 1

		for i in self.tableRows:
			self.tableLayout.addWidget(TableHeader(i), m, n)
			n += 1

		for i in self.tableButtons:
			self.tableLayout.addWidget(TableHeader(i), m, n)
			n += 1

		m += 1
		n = 0

	def addRow(self, row, buttons=[]):
		if self.m % 2 == 1:
			tableAccent = '#F1D4D4'
		else:
			tableAccent = '#FFFFFF'
	
		if self.showIndex:
			self.tableLayout.addWidget(
				TableItem(
					self.currentIndex,
					tableAccent=tableAccent
					),
				self.m,
				self.n
			)
			self.currentIndex += 1
			self.n += 1

		for i in row:
			self.tableLayout.addWidget(
				TableItem(
					i,
					tableAccent=tableAccent
					),
				self.m,
				self.n
			)
			self.n += 1

		for i in buttons:
			self.tableLayout.addWidget(
				TableButton(
					i[0],
					slot=i[1],
					color=i[2],
					tableAccent=tableAccent
					),
				self.m,
				self.n
			)
			self.n += 1

		self.m += 1
		self.n = 0

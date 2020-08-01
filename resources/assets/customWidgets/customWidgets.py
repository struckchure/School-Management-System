from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qtawesome as qta
import sys, os


# Custom Modules Imports

from views import pageConfigurations
from views import utils
from resources.assets.customWidgets.CDWidgets.CAvatar import CAvatar

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
	def __init__(self, placeHolder, icon, iconText='', iconColor='white'):
		super(LineEditButton, self).__init__()

		self.placeHolder = placeHolder
		self.icon = qta.icon(icon, color=iconColor)
		self.iconText = iconText

		self.groupLayout = QHBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignVCenter)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.groupLayout)
		self.setFixedHeight(30)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
	def __init__(self, user, default_image=None):
		super(NavBarUser, self).__init__()

		size = [500, 500]

		self.user = user
		self.userIcon = default_image

		navSideMargins = pageConfigurations.navSideMargins

		self.navBarUserLayout = QGridLayout()
		self.navBarUserLayout.setContentsMargins(0, 0, 0, 0)

		userImage = CAvatar(
            self,
            shape=CAvatar.Circle,
            animation=False,
            url=self.userIcon,
        )

		# self.userNameLabel = QLabel(self.user.get_full_name())
		# self.userNameLabel.setMaximumSize(300, 50)
		# self.userNameLabel.setObjectName('navUserLabel')
		# self.userNameLabel.setSizePolicy(
		# 	QSizePolicy(
		# 		QSizePolicy.MinimumExpanding,
		# 		QSizePolicy.MinimumExpanding
		# 	)
		# )

		# self.navBarUserLayout.addWidget(self.userNameLabel, 0, 0)
		self.navBarUserLayout.addWidget(userImage, 0, 0)

		self.setLayout(self.navBarUserLayout)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setMaximumWidth(pageConfigurations.sideBarSize[0])
		# self.setIcon(self.userIcon)
		# self.setText(self.user.get_full_name())
		self.setIconSize(QSize(25, 20))
		self.setObjectName('navBarUser')

		self.initialization()

	def initialization(self):
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showUserOptions)

		profileIcon = qta.icon('fa.user', color='black')
		logoutIcon = qta.icon('fa5s.door-open', color='black')

		self.userOptions = QMenu(self)

		self.profileAction = QAction(profileIcon, 'Profile', self)
		self.profileAction.triggered.connect(self.profileView)

		self.logoutAction = QAction(logoutIcon, 'Logout', self)
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

		self.iconLayout = QHBoxLayout()
		self.iconLayout.setSpacing(5)
		self.iconLayout.setContentsMargins(0, 0, 0, 0)

		self.groupLayout.addLayout(self.iconLayout)

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		self.setObjectName('navBar')
		self.setLayout(self.groupLayout)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setFixedHeight(pageConfigurations.navBarHeight)

		self.initialization()

	def initialization(self):
		height = self.height() * 0.7

		self.searchBox = LineEditButton(
			placeHolder='search ...',
			icon='fa.search',
		)
		self.searchBox.linedEdit.setFixedWidth(200)
		self.searchBox.button.setToolTip('search')

		self.groupLayout.addWidget(
			self.searchBox,
			stretch=0,
			alignment=Qt.AlignCenter
		)

		self.navUser = NavBarUser(self.user, 'resources/assets/images/1.jpg')

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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setMaximumSize(pageConfigurations.sideBarSectionWidth * 0.4, 70)
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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setObjectName('sideBarSection')
		self.setLayout(self.groupLayout)

		self.titleLabel = QLabel(f'{title}')
		self.titleLabel.setAlignment(Qt.AlignLeft)
		self.titleLabel.setObjectName('sideBarSectionTitle')
		self.titleLabel.setFixedSize(width * 0.2, 30)
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
	def __init__(self, title, image, color='white'):
		image = qta.icon(
			image,
			color=color
		)
		QPushButton.__init__(self, image, title)

		ratio = 0.7

		self.setFixedSize(pageConfigurations.sideBarSize[0] * ratio, pageConfigurations.sideBarButtonHeight)
		self.setObjectName('sideBarButton')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setIconSize(QSize(20, 20))


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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setMaximumSize(sideBarSize[0], sideBarSize[1])
		self.setObjectName('sideBarScroll')
		self.showMaximized()


class DashButton(QPushButton, QHBoxLayout):
	def __init__(self, buttonText, buttonValue, buttonIcon='resources/assets/images/icons/view.png', borderColor='#1554BD'):
		super(DashButton, self).__init__()

		self.buttonText = str(buttonText)
		self.buttonValue = str(buttonValue)
		self.buttonIcon = qta.icon(
			buttonIcon,
			color=borderColor,
			options=[
					{
						'scale_factor': 0.7
					}
				]
			)
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

		qss = utils.findReplace('#1554BD', self.borderColor, '/* idDashButton */')
		size = 90

		self.setStyleSheet(qss)
		self.setIcon(self.buttonIcon)
		self.setIconSize(QSize(size, size))
		self.setLayout(self.buttonLayout)
		self.setContentsMargins(0, 0, 0, 0)
		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setObjectName('dashButton')
		self.setMaximumSize(pageConfigurations.DashButtonSize[0], pageConfigurations.DashButtonSize[1])
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)

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

		qss = utils.readQSS()
		self.setStyleSheet(qss)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.resize(300, 170)
		self.setMaximumSize(600, 600)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)


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
		self.color = '#1554BD'
		self.iconColor = self.color

		self.setGraphicsEffect(self.shadow_effect)
		self.setContentsMargins(0, 0, 0, 0)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
		self.add_button.setIcon(
			qta.icon(
				'fa.plus-circle',
				color=self.color
			)
		)
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
		self.edit_list_btn.setIcon(
			qta.icon(
				'fa.edit',
				color=self.iconColor
			)
		)
		self.edit_list_btn.setIconSize(QSize(15, 15))
		self.edit_list_btn.setObjectName('listBtn')
		self.eventItemsLayout.addWidget(self.edit_list_btn)

		self.delete_list_btn = QPushButton()
		self.delete_list_btn.setFixedSize(25, height * buttonRatio)
		self.delete_list_btn.setIcon(
			qta.icon(
				'mdi.delete',
				color=self.iconColor
			)
		)
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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
			qss = utils.findReplace(
				'background-color: rgba(0, 0, 0, 0);',
				f'background-color: {tableAccent};',
				'/*tableAccent*/'
			)

		self.setStyleSheet(qss)
		self.setObjectName('tableItem')
		# self.setToolTip(real_text)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setMaximumSize(
			pageConfigurations.tableSize[0],
			pageConfigurations.tableSize[1]
		)


class TableButtonChild(QPushButton):
	def __init__(
		self,
		text,
		icon='resources/assets/images/icons/ic_event_note_white_48dp.png',
		color='#3E63CC',
		data='',
		mode=''
		):
		QPushButton.__init__(self, QIcon(icon), text)

		self.data = data
		self.mode = mode

		qss = utils.findReplace(
			'#3E63CC;',
			f'{color};',
			'/*tableButtonChildAccent*/'
		)
		blurRadius = 10
		offSet = 0.1

		self.groupGraphicsEffect = QGraphicsDropShadowEffect()
		self.groupGraphicsEffect.setBlurRadius(blurRadius)
		self.groupGraphicsEffect.setOffset(offSet)

		self.setGraphicsEffect(self.groupGraphicsEffect)
		self.setStyleSheet(qss)
		self.setObjectName('tableButtonChild')
		self.clicked.connect(self.buttonSlot)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setMaximumSize(
			pageConfigurations.tableSize[0],
			pageConfigurations.tableSize[1]
		)

	def buttonSlot(self):
		if self.mode == 'delete':
			pass
		elif self.mode == 'view':
			pass


class TableButton(QGroupBox):
	def __init__(
		self,
		text,
		icon='resources/assets/images/icons/ic_event_note_white_48dp.png',
		color='rgba(0, 0, 0, 0)',
		tableAccent='',
		data='',
		mode=''
		):
		QGroupBox.__init__(self)

		self.data = data

		qss = utils.findReplace(
			'background-color: rgba(0, 0, 0, 0);',
			f'background-color: {tableAccent};',
			'/*tableAccent*/'
		)

		buttonRatio = 0.8

		self.buttonLayout = QVBoxLayout()
		self.buttonLayout.setContentsMargins(0, 0, 0, 0)
		self.buttonLayout.setAlignment(Qt.AlignCenter)

		self.buttonLayout.addWidget(
			TableButtonChild(
				text,
				icon=icon,
				color=color
				)
			)

		self.setStyleSheet(qss)
		self.setObjectName('tableButton')
		self.setCheckable(False)
		self.setLayout(self.buttonLayout)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
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
			tableAccent = '#E6E8FF'
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
					color=i[1],
					tableAccent=tableAccent,
					data=i[2],
					mode=i[3]
					),
				self.m,
				self.n
			)
			self.n += 1

		self.m += 1
		self.n = 0


'''
	Cards
'''


class CardBasic(QGroupBox):
	def __init__(self, width=200, height=200, accent='blue'):
		QGroupBox.__init__(self)

		self.accent = accent

		qss = utils.findReplace(
			f'orange;',
			f'{accent};',
			'/*cardBasicAccent*/'
		)

		self.cardLayout = QVBoxLayout()
		self.cardLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.cardLayout.setSpacing(0)
		self.cardLayout.setContentsMargins(0, 0, 0, 0)

		blurRadius = 10
		offSet = 0.1

		self.cardShadow = QGraphicsDropShadowEffect()
		self.cardShadow.setBlurRadius(blurRadius)
		self.cardShadow.setOffset(offSet)

		self.setStyleSheet(qss)
		self.setObjectName('cardBasic')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setLayout(self.cardLayout)
		self.setGraphicsEffect(self.cardShadow)
		self.setMaximumSize(width, height)


class CardHeader(QLabel):
	def __init__(self, text, width=200, height=30, accent='blue'):
		QLabel.__init__(self, text)

		self.accent = accent

		self.setObjectName('cardHeader')
		self.setMaximumHeight(height)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)


class CardContent(QGroupBox):
	def __init__(self, width=200, height=200, accent='blue'):
		QGroupBox.__init__(self)

		self.accent = accent

		self.cardLayout = QVBoxLayout()
		self.cardLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.cardLayout.setSpacing(0)
		self.cardLayout.setContentsMargins(0, 0, 0, 0)

		blurRadius = 10
		offSet = 0.1

		self.cardShadow = QGraphicsDropShadowEffect()
		self.cardShadow.setBlurRadius(blurRadius)
		self.cardShadow.setOffset(offSet)

		qss = utils.findReplace(
			f'orange;',
			f'{self.accent};',
			'/*cardContentAccent*/'
		)

		self.setStyleSheet(qss)
		self.setObjectName('cardContent')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setLayout(self.cardLayout)
		self.setGraphicsEffect(self.cardShadow)
		self.setMaximumSize(width, height * 3)


'''
	Tabs
'''


class TabCardBasic(QGroupBox):
	def __init__(self, width=200, height=200):
		QGroupBox.__init__(self)

		self.cardLayout = QVBoxLayout()
		self.cardLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		self.cardLayout.setSpacing(0)
		self.cardLayout.setContentsMargins(0, 0, 0, 0)

		blurRadius = 10
		offSet = 0.1

		self.cardShadow = QGraphicsDropShadowEffect()
		self.cardShadow.setBlurRadius(blurRadius)
		self.cardShadow.setOffset(offSet)

		self.setObjectName('tabCardBasic')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setLayout(self.cardLayout)
		self.setGraphicsEffect(self.cardShadow)
		# self.setFixedSize(width, height)
		# self.setMinimumSize(width, height)
		self.setMaximumSize(width, height)


class TabBasic(QTabWidget):
	def __init__(self):
		QTabWidget.__init__(self)

		width, height = 1200, 1200

		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.Maximum,
				QSizePolicy.Maximum
			)
		)
		# self.setMinimumWidth(700)
		self.setMaximumSize(width, height)

		self.initialization()

	def initialization(self):
		pass

	def addTabWidget(self, widget, title='Tab'):
		self.addTab(widget, widget.tabTitle)


class Tab(QGroupBox):
	def __init__(self, tabTitle, width=500, height=400):
		QGroupBox.__init__(self)

		self.tabTitle = tabTitle
		self.width = 1000
		self.height = 900

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setAlignment(Qt.AlignTop)

		self.setObjectName('tabContent')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setLayout(self.groupLayout)
		# self.setMinimumSize(width * 0.8, height * 0.2)
		self.setMaximumSize(width, height)

		self.initialization()

	def initialization(self):
		pass

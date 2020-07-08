'''
	-_- Authors -_-
	Names - Mohammed Al Ameen Bolutife, Omoyajowo Solomon Olanrewaju
	E-Mails - ameenmohammed2311@gmail.com, omoyajowosolomon7@gamil.com
	GitHub - Mohammed2702, Soloskido
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
import cv2


# Custom Modules Imports

from views import pageConfigurations
from resources.assets.customWidgets import customWidgets

# Custom Modules End


'''
	Home Views
'''

class Home(QGroupBox):
	def __init__(self, pageController, user):
		QGroupBox.__init__(self)

		self.pageController = pageController
		self.user = user

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop)

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setLayout(self.groupLayout)
		self.resize(1370, 800)
		self.setMaximumSize(1500, 1000)
		self.setObjectName('home')
		self.showMaximized()

		self.initialization()

	def initialization(self):
		self.navBarHeight = pageConfigurations.navBarHeight
		self.sideBarWidth = pageConfigurations.getSideBarWidth(self.width())
		self.pageWidth = pageConfigurations.getPageWidth(self.width())

		self.mainPage()
		self.navBar()
		self.sideBar()
		self.Page()

	def navBar(self):
		self.pageLayout = QVBoxLayout()
		self.pageLayout.setContentsMargins(0, 0, 0, 0)
		self.pageLayout.setAlignment(Qt.AlignTop)

		self.navBarLayout = QHBoxLayout()
		self.navBarLayout.setSpacing(0)
		# self.navBarLayout.setAlignment(Qt.AlignCenter)

		self.titleLayout = QHBoxLayout()
		self.titleLayout.setAlignment(Qt.AlignLeft)
		self.titleLayout.setSpacing(0)
		self.navBarLayout.addLayout(self.titleLayout)

		self.searchLineEdit = QLineEdit()
		self.searchLineEdit.setFocus(False)
		self.searchLineEdit.setMaximumSize(300, 40)
		self.searchLineEdit.setFixedWidth(300)
		self.searchLineEdit.setObjectName('searchQLineEdit')
		self.titleLayout.addWidget(self.searchLineEdit, stretch=0, alignment=Qt.AlignLeft)

		self.searchIcon = QIcon('resources/assets/images/icons/search_icn.png')
		self.searchButton = QToolButton()
		self.searchButton.setFixedSize(30, self.searchLineEdit.height() - 15)
		self.searchButton.setObjectName('Button-no-border')
		self.searchButton.setIcon(self.searchIcon)
		self.searchButton.setIconSize(QtCore.QSize(24, 24))
		self.titleLayout.addWidget(self.searchButton, stretch=0, alignment=Qt.AlignRight)

		self.userLayout = QHBoxLayout()
		self.userLayout.setSpacing(0)
		self.userLayout.setAlignment(Qt.AlignRight)
		self.navBarLayout.addLayout(self.userLayout)

		self.userIcon = QIcon('resources/assets/images/icons/user.png')
		self.userButton = QToolButton()
		self.userButton.setFixedSize(30, 20)
		self.userButton.setObjectName('toolButton')
		self.userButton.setIcon(self.userIcon)
		self.userLayout.addWidget(self.userButton, stretch=0, alignment=Qt.AlignRight)

		blurRadius = 160
		offset = 17
		color = QColor(0, 0, 0, 255 * .3)

		self.navBarShadow = QGraphicsDropShadowEffect()
		self.navBarShadow.setBlurRadius(blurRadius)
		self.navBarShadow.setOffset(offset)
		self.navBarShadow.setColor(color)

		self.navBarGroup = QGroupBox()
		self.navBarGroup.setGraphicsEffect(self.navBarShadow)
		self.navBarGroup.resize(self.width(), self.navBarHeight)
		self.navBarGroup.setFixedHeight(self.navBarHeight)
		self.navBarGroup.setMinimumWidth(self.pageWidth)
		self.navBarGroup.setLayout(self.navBarLayout)
		self.navBarGroup.setObjectName('navBar')
		self.pageLayout.addWidget(self.navBarGroup)

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignTop)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setLayout(self.mainPageLayout)
		self.mainPageGroup.setObjectName('mainPageGroup')

		self.groupLayout.addWidget(self.mainPageGroup, stretch=0, alignment=Qt.AlignTop)

	def sideBar(self):
		self.sideBarLayout = QVBoxLayout()
		self.sideBarLayout.setContentsMargins(0, 0, 0, 0)
		self.sideBarLayout.setSpacing(0)
		self.sideBarLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		self.sideBarButtonRatio = pageConfigurations.sideBarButtonRatio

		self.title = 'smsUI'
		self.sideBarTitle = customWidgets.SideBarTitle(text=self.title)
		self.sideBarTitle.setMaximumWidth(self.sideBarWidth)
		self.sideBarLayout.addWidget(self.sideBarTitle)

		spacer1 = QLabel()
		spacer1.setFixedHeight(60)
		self.sideBarLayout.addWidget(spacer1)

		self.dashBoard = customWidgets.SideBarButton(title='DashBoard', image='resources/assets/images/icons/dashboard_icn.png')
		self.sideBarLayout.addWidget(self.dashBoard)

		self.studentSection = customWidgets.SideBarSection(title='Student', width=self.sideBarWidth)
		self.admissionButton = customWidgets.SideBarButton(title='Admission', image='resources/assets/images/icons/admission.png')
		self.admissionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.admissionButton)

		self.studentPromotionButton = customWidgets.SideBarButton(title='Promotion', image='resources/assets/images/icons/promotion.png')
		self.studentPromotionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.studentPromotionButton)

		self.allStudentsButton = customWidgets.SideBarButton(title='All Students', image='resources/assets/images/icons/all.png')
		self.allStudentsButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.allStudentsButton)

		self.sideBarLayout.addWidget(self.studentSection)

		self.teacherSection = customWidgets.SideBarSection(title='Teacher', width=self.sideBarWidth)
		self.addTeacherButton = customWidgets.SideBarButton(title='New Teacher', image='resources/assets/images/icons/new_teacher.png')
		self.addTeacherButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.addTeacherButton)

		self.teacherPromotionButton = customWidgets.SideBarButton(title='Promotion', image='resources/assets/images/icons/promotion.png')
		self.teacherPromotionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.teacherPromotionButton)

		self.allTeachersButton = customWidgets.SideBarButton(title='All Teachers', image='resources/assets/images/icons/all.png')
		self.allTeachersButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.allTeachersButton)

		self.sideBarLayout.addWidget(self.teacherSection)

		self.sideBarGroup = QGroupBox()
		self.sideBarGroup.setMaximumWidth(self.sideBarWidth)
		# self.sideBarGroup.setFixedHeight(self.sideBarWidth * 3)
		self.sideBarGroup.setLayout(self.sideBarLayout)
		self.sideBarGroup.setObjectName('sideBarGroup')

		self.sideBarScroll = QScrollArea()
		self.sideBarScroll.setMaximumWidth(self.sideBarWidth + 5)
		self.sideBarScroll.setMinimumHeight(self.sideBarWidth * 3)
		self.sideBarScroll.setWidget(self.sideBarGroup)
		self.sideBarScroll.setWidgetResizable(True)
		self.sideBarScroll.setObjectName('sideBarScroll')

		self.mainPageLayout.addWidget(self.sideBarScroll)

	def Page(self):
		self.pageGroup = QGroupBox()
		self.pageGroup.setMaximumWidth(self.pageWidth)
		self.pageGroup.setLayout(self.pageLayout)
		self.pageGroup.setObjectName('pageGroup')

		self.total_students = 2000
		self.total_teachers = 30
		self.total_clubs = 20
		self.total_staffs = 50

		self.pageScroll = QScrollArea()
		self.pageScroll.setMaximumWidth(self.pageWidth)
		self.pageScroll.setWidget(self.pageGroup)
		self.pageScroll.setWidgetResizable(True)
		self.pageScroll.setObjectName('pageScroll')

		self.Dashboard()
		self.mainPageLayout.addWidget(self.pageScroll)

	def Dashboard(self):
		self.dashboard_layout = QVBoxLayout()
		self.dashboard_layout.setContentsMargins(30, 40, 30, 0)

		self.dashboard_title = QLabel("Dashboard")
		self.dashboard_title.setObjectName("dashboardTitle")
		self.dashboard_layout.addWidget(self.dashboard_title)

		width = 230
		height = 210

		self.first_row = QHBoxLayout()
		self.first_row.setContentsMargins(0, 0, 0, 0)

		self.students_display = customWidgets.FirstRow(head="STUDENTS", total_no=self.total_students)
		self.students_display.setStyleSheet('''
		QLabel#headText {
		color:#3E63CC;
		padding-left:20px;
		margin:0px;
		}
		QLabel#totalText {
		padding-left:20px;
		margin:0px;
		}
		QPushButton#firstRow {
		border-bottom:3px solid #3E63CC;
		}
		''')

		self.teachers_display = customWidgets.FirstRow(head="TEACHERS", total_no=self.total_teachers, icon='resources/assets/images/icons/group2.png')
		self.teachers_display.setStyleSheet('''
		QLabel#headText {
		color:#2ECC71;
		padding-left:20px;
		margin:0px;
		}
		QLabel#totalText {
		padding-left:20px;
		margin:0px;
		}
		QPushButton#firstRow {
		border-bottom:3px solid #2ECC71;
		}
		''')

		self.clubs_display = customWidgets.FirstRow(head="CLUBS", total_no=self.total_clubs, icon='resources/assets/images/icons/group3.png')
		self.clubs_display.setStyleSheet('''
		QLabel#headText {
		color:#2ECC71;
		padding-left:20px;
		margin:0px;
		}
		QLabel#totalText {
		padding-left:20px;
		margin:0px;
		}
		QPushButton#firstRow {
		border-bottom:3px solid #2ECC71;
		}
		''')

		self.staffs_display = customWidgets.FirstRow(head="STAFFS", total_no=self.total_staffs, icon='resources/assets/images/icons/group4.png')
		self.staffs_display.setStyleSheet('''
		QLabel#headText {
		color:#2ECC71;
		padding-left:20px;
		margin:0px;
		}
		QLabel#totalText {
		padding-left:20px;
		margin:0px;
		}
		QPushButton#firstRow {
		border-bottom:3px solid #2ECC71;
		}
		''')

		self.first_row.addWidget(self.students_display)
		self.first_row.addWidget(self.teachers_display)
		self.first_row.addWidget(self.clubs_display)
		self.first_row.addWidget(self.staffs_display)

		#adding second row layouts
		self.second_row = QHBoxLayout()
		self.second_row.setAlignment(Qt.AlignLeft)
		self.second_row.setContentsMargins(0, 40, 0, 0)

		self.upcoming_events = customWidgets.SecondRow(title="Upcoming Events", eventName="Inter house Sport Inter house Sport Inter house Sport Inter house Sport")

		self.event_date = QLabel("12 November")
		self.event_date.setMinimumSize(120, 35)
		self.event_date.setObjectName('event2')
		self.upcoming_events.list_layout.addWidget(self.event_date)

		editButton = self.upcoming_events.edit_list_btn
		deleteButton = self.upcoming_events.delete_list_btn
		self.upcoming_events.list_layout.addWidget(editButton)
		self.upcoming_events.list_layout.addWidget(deleteButton)

		self.notice_board = customWidgets.SecondRow(title="Notice Board", eventName="WAEC/NECO Exam")
		self.notice_board.setMinimumWidth(560)
		self.notice_board.box_title.setMinimumSize(430, 35)
		self.notice_board.setStyleSheet('''
		QGroupBox {
		margin-left:55px;
		}
		''')

		self.second_row.addWidget(self.upcoming_events)
		self.second_row.addWidget(self.notice_board)


		self.dashboard_layout.addLayout(self.first_row)
		self.dashboard_layout.addLayout(self.second_row)
		self.pageLayout.addLayout(self.dashboard_layout)


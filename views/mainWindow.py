'''
	-_- Authors -_-
	Names - Mohammed Al Ameen Bolutife, Omoyajowo Solomon
	E-Mails - ameenmohammed2311@gmail.com, solo@gamil.com
	GitHub - Mohammed2702, Soloskido
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


# Custom Modules Imports
# - Tools
from resources.assets.customWidgets import customWidgets
from resources.assets.customWidgets.CDWidgets.CDrawer import CDrawer
from views import utils

# - Pages
from views import pageConfigurations
from views import DashBoard
from views import Students
from views import Teachers

# Custom Modules End


'''
	Home Views
'''


class Home(QGroupBox):
	def __init__(self, pageController, pageFinders, user):
		QGroupBox.__init__(self)

		self.pageController = pageController
		self.pageFinders = pageFinders
		self.user = user
		self.rightPageFinders = {
			'page': [],
			'index': []
		}

		self.groupLayout = QHBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop)

		self.setLayout(self.groupLayout)
		self.setMaximumSize(pageConfigurations.windowWidth, pageConfigurations.windowHeight)
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setObjectName('home')
		self.showMaximized()

		self.initialization()

	def initialization(self):
		self.navBarHeight = pageConfigurations.navBarHeight
		self.sideBarWidth = pageConfigurations.getSideBarWidth(self.width())
		self.pageWidth = pageConfigurations.getPageWidth(self.width())

		# self.sideBar()
		self.mainPage()
		self.navBar()
		self.rightPage()

	def navBar(self):
		self.navBarWidget = customWidgets.NavBar(self.user)
		
		menuIcon = customWidgets.qta.icon('fa.bars', color='white')

		self.menuBar = QPushButton()
		self.menuBar.setMaximumSize(30, 25)
		self.menuBar.setObjectName('login')
		self.menuBar.setIcon(menuIcon)
		self.menuBar.clicked.connect(self.sideBar)

		self.navBarWidget.iconLayout.addWidget(self.menuBar)
		self.mainPageLayout.addWidget(self.navBarWidget)

	def mainPage(self):
		self.mainPageLayout = QVBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignTop)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setObjectName('mainPage')
		self.mainPageGroup.setLayout(self.mainPageLayout)

		self.mainPageScroll = QScrollArea()
		self.mainPageScroll.setObjectName('mainPageScroll')
		self.mainPageScroll.setWidgetResizable(True)
		self.mainPageScroll.setWidget(self.mainPageGroup)

		self.groupLayout.addWidget(self.mainPageScroll)

	def sideBar(self):
		'''
			Add widgets to the sideBar
			self.sideBarWidget.sideBarLayout.addWidget(self.sideBarTitle)
		'''
		
		# SideBar

		self.sideBarScroll = customWidgets.SideBar()

		self.sideBarLayout = self.sideBarScroll.sideBarLayout
		self.sideBarButtonRatio = pageConfigurations.sideBarButtonRatio
		
		self.title = 'School Management System'
		self.sideBarTitle = customWidgets.SideBarTitle(text=self.title)
		self.sideBarLayout.addWidget(self.sideBarTitle)

		spacer1 = QLabel()
		spacer1.setFixedHeight(45)
		self.sideBarLayout.addWidget(spacer1)

		if self.user.is_staff:
			self.adminAccess()
		self.nonAdminAcsess()

		if not hasattr(self, 'topDrawer'):
			self.sideDrawer = CDrawer(self, direction=CDrawer.LEFT)
			self.sideDrawer.setWidget(self.sideBarScroll)
		self.sideDrawer.show()

	def adminAccess(self):
		self.dashBoardButton = customWidgets.SideBarButton(title='DashBoard', image='fa.dashboard')
		self.dashBoardButton.clicked.connect(self.dashBoardButtonView)
		self.sideBarLayout.addWidget(self.dashBoardButton)

		# Students

		self.studentSection = customWidgets.SideBarSection(title='Student')

		self.admissionButton = customWidgets.SideBarButton(title='Admission', image='fa.user-plus')
		self.admissionButton.clicked.connect(self.admissionButtonView)
		self.studentSection.widgetLayout.addWidget(self.admissionButton)

		self.studentPromotionButton = customWidgets.SideBarButton(title='Promotion', image='fa.angle-double-up')
		self.studentPromotionButton.clicked.connect(self.studentPromotionButtonView)
		self.studentSection.widgetLayout.addWidget(self.studentPromotionButton)

		self.allStudentsButton = customWidgets.SideBarButton(title='All Students', image='fa.user')
		self.allStudentsButton.clicked.connect(self.allStudentsButtonView)
		self.studentSection.widgetLayout.addWidget(self.allStudentsButton)

		self.sideBarLayout.addWidget(self.studentSection)

		# Teachers
		
		self.teacherSection = customWidgets.SideBarSection(title='Teacher')

		self.addTeacherButton = customWidgets.SideBarButton(title='New Teacher', image='fa.user-plus')
		self.addTeacherButton.clicked.connect(self.addTeacherButtonView)
		self.teacherSection.widgetLayout.addWidget(self.addTeacherButton)

		self.teacherPromotionButton = customWidgets.SideBarButton(title='Promotion', image='fa.angle-double-up')
		self.teacherPromotionButton.clicked.connect(self.teacherPromotionButtonView)
		self.teacherSection.widgetLayout.addWidget(self.teacherPromotionButton)

		self.allTeachersButton = customWidgets.SideBarButton(title='All Teachers', image='fa.user')
		self.allTeachersButton.clicked.connect(self.allTeachersButtonView)
		self.teacherSection.widgetLayout.addWidget(self.allTeachersButton)

		self.sideBarLayout.addWidget(self.teacherSection)

	def nonAdminAcsess(self):
		pass

	def dashBoardButtonView(self):
		text = self.dashBoardButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(DashBoard.DashBoard(self.rightPageStackedWidget, self.rightPageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def admissionButtonView(self):
		text = self.admissionButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Students.StudentAdmission(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def studentPromotionButtonView(self):
		text = self.studentPromotionButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Students.StudentPromotion(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def allStudentsButtonView(self):
		text = self.allStudentsButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Students.Students(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def addTeacherButtonView(self):
		text = self.addTeacherButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Teachers.TeacherAdmission(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def teacherPromotionButtonView(self):
		text = self.teacherPromotionButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Teachers.TeacherPromotion(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def allTeachersButtonView(self):
		text = self.allTeachersButton.text().replace(' ', '')
		if text in self.rightPageFinders:
			page = utils.findPage(self.pageFinders, text)
			self.rightPageStackedWidget.setCurrentIndex(page)
		else:
			self.rightPageFinders['page'].append(text)
			self.rightPageFinders['index'].append(self.rightPageStackedWidget.currentIndex() + 1)
			
			self.rightPageStackedWidget.addWidget(Teachers.Teachers(self.rightPageStackedWidget, self.pageFinders))
			self.rightPageStackedWidget.setCurrentIndex(self.rightPageStackedWidget.currentIndex() + 1)

	def rightPage(self):
		self.rightPageStackedWidget = QStackedWidget()
		self.rightPageStackedWidget.setContentsMargins(0, 0, 0, 0)
		self.rightPageStackedWidget.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)

		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setSpacing(0)
		self.rightPageLayout.setAlignment(Qt.AlignCenter)

		self.rightPageLayout.addWidget(self.rightPageStackedWidget)

		self.rightPageFinders['page'].append('DashBoard')
		self.rightPageFinders['index'].append(0)

		self.dashBoard = DashBoard.DashBoard(self.rightPageStackedWidget, self.rightPageFinders)
		self.rightPageStackedWidget.addWidget(self.dashBoard)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setMaximumSize(1500, 800)
		self.rightPageGroup.setObjectName('rightMainGroup')
		self.rightPageGroup.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.rightPageGroup.setLayout(self.rightPageLayout)

		self.rightPageScroll = QScrollArea()
		self.rightPageScroll.setObjectName('rightMainScroll')
		self.rightPageScroll.setWidgetResizable(True)
		self.rightPageScroll.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.rightPageGroup.setMaximumSize(1500, 800)
		self.rightPageScroll.setWidget(self.rightPageGroup)

		self.mainPageLayout.addWidget(self.rightPageScroll)

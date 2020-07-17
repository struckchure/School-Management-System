from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

# Custom Modules Imports

from views import pageConfigurations
from resources.assets.customWidgets import customWidgets

# Custom Modules End


'''
	DashBoard Views
'''


class DashBoard(QGroupBox):
	def __init__(self, stackedWidget, pageFinders):
		QGroupBox.__init__(self)

		self.stackedWidget = stackedWidget
		self.pageFinders = pageFinders

		self.groupLayout = QGridLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignCenter)
		self.groupLayout.setSpacing(15)

		
		self.pageCrumb = customWidgets.PageCrumb('DashBoard')

		self.studentButton = customWidgets.DashButton(
			'Students',
			100,
			buttonIcon='fa.users'
		)
		self.teacherButton = customWidgets.DashButton(
			'Teachers',
			15,
			buttonIcon='fa.users',
			borderColor='#7B615C'
		)
		self.groupButton = customWidgets.DashButton(
			'Groups',
			10,
			buttonIcon='fa.users',
			borderColor='#2C7BA8'
		)
		self.clubsButton = customWidgets.DashButton(
			'Clubs',
			20,
			buttonIcon='fa.users',
			borderColor='#6BC10C'
		)

		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)
		self.groupLayout.addWidget(self.studentButton, 1, 0, 1, 1)
		self.groupLayout.addWidget(self.teacherButton, 1, 1, 1, 1)
		self.groupLayout.addWidget(self.groupButton, 1, 2, 1, 1)
		self.groupLayout.addWidget(self.clubsButton, 1, 3, 1, 1)

		self.setObjectName('noBorderBox')
		self.setSizePolicy(
			QSizePolicy(
				QSizePolicy.MinimumExpanding,
				QSizePolicy.MinimumExpanding
			)
		)
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		self.pageContentsLayout = QHBoxLayout()
		self.pageContentsLayout.setAlignment(Qt.AlignLeft)
		self.pageContentsLayout.setContentsMargins(0, 40, 0, 0)

		self.upcomingEvents = customWidgets.Card(
			title="Upcoming Events",
		)

		self.upcomingEvents.addEvent(event='Hey There, we are opening next year :)')

		self.notice_board = customWidgets.Card(
			title="Notice Board",
		)

		self.notice_board.addNotice(notice='Hey There, Next Year is probably not sure...')

		self.pageContentsLayout.addWidget(self.upcomingEvents)
		self.pageContentsLayout.addWidget(self.notice_board)

		self.groupLayout.addLayout(self.pageContentsLayout, 2, 0, 1, 4)

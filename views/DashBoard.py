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
		self.groupLayout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
		self.groupLayout.setSpacing(20)
		
		self.pageCrumb = customWidgets.PageCrumb('DashBoard')

		self.studentButton = customWidgets.DashButton('Students', 100, buttonIcon='resources/assets/images/icons/group1.png')
		self.teacherButton = customWidgets.DashButton('Teachers', 15, buttonIcon='resources/assets/images/icons/group2.png', borderColor='#7B615C')
		self.groupButton = customWidgets.DashButton('Groups', 10, buttonIcon='resources/assets/images/icons/group3.png', borderColor='#2C7BA8')
		self.clubsButton = customWidgets.DashButton('Clubs', 20, buttonIcon='resources/assets/images/icons/group4.png', borderColor='#6BC10C')

		self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)
		self.groupLayout.addWidget(self.studentButton, 1, 0)
		self.groupLayout.addWidget(self.teacherButton, 1, 1)
		self.groupLayout.addWidget(self.groupButton, 1, 2)
		self.groupLayout.addWidget(self.clubsButton, 1, 3)

		self.setObjectName('noBorderBox')
		self.setLayout(self.groupLayout)

		self.initalization()

	def initalization(self):
		self.pageContentsLayout = QHBoxLayout()
		self.pageContentsLayout.setAlignment(Qt.AlignLeft)
		self.pageContentsLayout.setContentsMargins(0, 40, 0, 0)

		self.upcomingEvents = customWidgets.SecondRow(title="Upcoming Events", eventName="Inter house Sport Inter house Sport Inter house Sport Inter house Sport")

		self.eventDate = QLabel("12 November")
		self.eventDate.setMinimumSize(120, 35)
		self.eventDate.setObjectName('event2')
		self.upcomingEvents.list_layout.addWidget(self.eventDate)

		editButton = self.upcomingEvents.edit_list_btn
		deleteButton = self.upcomingEvents.delete_list_btn
		
		self.upcomingEvents.list_layout.addWidget(editButton)
		self.upcomingEvents.list_layout.addWidget(deleteButton)

		self.notice_board = customWidgets.SecondRow(title="Notice Board", eventName="WAEC/NECO Exam")

		self.pageContentsLayout.addWidget(self.upcomingEvents)
		self.pageContentsLayout.addWidget(self.notice_board)

		self.groupLayout.addLayout(self.pageContentsLayout, 2, 0, 1, 4)

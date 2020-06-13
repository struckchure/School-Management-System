from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys



class HomePage(QWidget):
    def __init__(self, school_name, first='First name', last=''):
        QWidget.__init__(self)

        self.school_name = school_name
        self.first_in = first
        self.last_in = last
        self.setWindowTitle(self.school_name)

        self.window_layout = QVBoxLayout()
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.window_layout)

        self.initialization()

    def initialization(self):
        self.create_main_layout()
        self.layout_body()
        self.left_layout()
        self.right_layout()

    def create_main_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_group = QGroupBox()
        self.main_group.setContentsMargins(0, 0, 0, 0)
        self.main_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                }
            '''
            )
        self.main_group.setLayout(self.main_layout)
        self.window_layout.addWidget(self.main_group)

    def layout_body(self):
        self.body_group = QGroupBox()
        self.body_group.setContentsMargins(0, 0, 0, 0)
        self.body_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                }
            ''')
        self.body_layout = QHBoxLayout()
        self.body_layout.setSpacing(0)
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_group.setLayout(self.body_layout)
        self.main_layout.addWidget(self.body_group)

    def left_layout(self):
        self.left_group_layout = QVBoxLayout()
        self.left_group_layout.setContentsMargins(0, 0, 0, 0)

        self.left_group = QGroupBox()
        self.left_group.setContentsMargins(0, 0, 0, 0)
        self.left_group.setLayout(self.left_group_layout)
        self.left_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color:#262626;
                }
            ''')

        self.left_scroll = QScrollArea()
        self.left_scroll.setFixedWidth(230)
        self.left_scroll.setContentsMargins(0, 0, 0, 0)
        self.left_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )
        self.left_scroll.setWidgetResizable(True)
        self.left_scroll.setWidget(self.left_group)

        self.body_layout.addWidget(self.left_scroll)

        self.left_nav_bar()

    def left_nav_bar(self):
        self.left_nav_layout = QVBoxLayout()
        self.left_nav_layout.setSpacing(0)
        self.left_nav_layout.setContentsMargins(0, 0, 0, 0)
        self.left_nav_layout.setAlignment(Qt.AlignLeft)

        self.button_width = 230
        self.button_height = 35

        self.current_right_board = ['']

        self.school_details()

        self.dash_board()
        self.students()
        self.teachers()
        self.class_()
        self.exam()

        self.left_nav_group = QGroupBox()
        self.left_nav_group.setContentsMargins(0, 0, 0, 0)
        self.left_nav_group.setLayout(self.left_nav_layout)

        self.left_group_layout.addWidget(self.left_nav_group)

    def school_details(self):
        self.sch_det_layout = QHBoxLayout()
        self.sch_det_layout.setContentsMargins(0, 0, 0, 0)
        self.sch_det_layout.setSpacing(0)
        self.sch_det_layout.setAlignment(Qt.AlignLeft)

        self.sch_icon = QLabel()
        self.icon_ = QPixmap('school.png')
        self.sch_icon.setPixmap(self.icon_)
        self.sch_icon.setAlignment(Qt.AlignCenter)
        self.sch_icon.setFixedSize(90, 120)
        self.sch_det_layout.addWidget(self.sch_icon)

        self.sch_name = QLabel(self.school_name)
        self.sch_name.setFixedSize((self.button_width - 45) / 2, 100)
        self.sch_name.setWordWrap(True)
        self.sch_name.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.sch_name.setAlignment(Qt.AlignCenter)
        self.sch_det_layout.addWidget(self.sch_name)

        self.sch_det_group = QGroupBox()
        self.sch_det_group.setStyleSheet(
            '''
            QGroupBox {
                padding: 12px;
                background-color: rgb(200, 180, 10);
                }
            '''
        )
        self.sch_det_group.setFixedHeight(150)
        self.sch_det_group.setLayout(self.sch_det_layout)

        self.left_group_layout.addWidget(self.sch_det_group)

    def dash_board(self):
        self.dash_board_button = QPushButton('Dashboard')
        self.dash_board_button.setIcon(QIcon('Icons/home.png'))
        self.dash_board_button.clicked.connect(self.dashboard_slot)
        self.dash_board_button.setFixedSize(self.button_width, self.button_height)
        self.dash_board_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);  
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.dash_board_button)

    def dashboard_slot(self):
        try:
            msg = 'You\'re already on the Dashboard.'
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e

    def students(self):
        self.students_button = QPushButton('Students')
        self.students_button.setIcon(QIcon('Icons/056-student.png'))
        self.students_button.clicked.connect(self.students_slot)
        self.students_button.setFixedSize(self.button_width, self.button_height)
        self.students_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.students_button)

    def students_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Students import Students as Page
            
            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e
        
    def teachers(self):
        self.teacher_button = QPushButton('Teachers')
        self.teacher_button.setIcon(QIcon('Icons/047-portfolio.png'))
        self.teacher_button.clicked.connect(self.teachers_slot)
        self.teacher_button.setFixedSize(self.button_width, self.button_height)
        self.teacher_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);  
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.teacher_button)

    def teachers_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Teachers import Teachers as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def parents(self):
        self.parents_button = QPushButton('Parents')
        self.parents_button.clicked.connect(self.parents_slot)
        self.parents_button.setFixedSize(self.button_width, self.button_height)
        self.parents_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }

        '''
            )
        self.left_nav_layout.addWidget(self.parents_button)

    def parents_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Parents import Parents as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def library(self):
        self.library_button = QPushButton('Library')
        self.library_button.clicked.connect(self.library_slot)
        self.library_button.setFixedSize(self.button_width, self.button_height)
        self.library_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.library_button)

    def library_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Library import Library as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def class_(self):
        self.class_button = QPushButton('Class')
        self.class_button.setIcon(QIcon('Icons/conference.png'))
        self.class_button.clicked.connect(self.class_slot)
        self.class_button.setFixedSize(self.button_width, self.button_height)
        self.class_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230); 
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.class_button)

    def class_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Class import Class as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def subjects(self):
        self.subjects_button = QPushButton('Subjects')
        self.subjects_button.clicked.connect(self.subjects_slot)
        self.subjects_button.setFixedSize(self.button_width, self.button_height)
        self.subjects_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }

        '''
            )
        self.left_nav_layout.addWidget(self.subjects_button)

    def subjects_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Subjects import Subjects as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def class_routine(self):
        self.class_routine_button = QPushButton('Class routine')
        self.class_routine_button.clicked.connect(self.class_routine_slot)
        self.class_routine_button.setFixedSize(self.button_width, self.button_height)
        self.class_routine_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);  
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.class_routine_button)

    def class_routine_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.ClassRoutine import ClassRoutine as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def attendance(self):
        self.attendance_button = QPushButton('Attendance')
        self.attendance_button.clicked.connect(self.attendance_slot)
        self.attendance_button.setFixedSize(self.button_width, self.button_height)
        self.attendance_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }

        '''
            )
        self.left_nav_layout.addWidget(self.attendance_button)

    def attendance_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Attendance import Attendance as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def exam(self):
        self.exam_button = QPushButton('Exam')
        self.exam_button.setIcon(QIcon('Icons/016-examination.png'))
        self.exam_button.clicked.connect(self.exam_slot)
        self.exam_button.setFixedSize(self.button_width, self.button_height)
        self.exam_button.setStyleSheet(
        '''
        QPushButton {
            text-align: left;
            background-color: #262626;
            font-size: 15px;
            color: white;
            border-top: 1px solid rgb(255, 210, 230);
            border-bottom: 1px solid rgb(255, 210, 230);
            padding-left: 12px;
            padding-right: 12px; 
            }
        .QPushButton:hover {
            background-color: #232323;
            }
        '''
            )
        self.left_nav_layout.addWidget(self.exam_button)

    def exam_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets.Exam import Exam as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def right_layout(self):
        self.right_group = QGroupBox()
        self.right_group.setContentsMargins(0, 0, 0, 0)
        self.right_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                }
            ''')

        self.right_group_layout = QVBoxLayout()
        self.right_group_layout.setContentsMargins(0, 0, 0, 0)
        self.right_group_layout.setAlignment(Qt.AlignTop)

        self.right_group.setLayout(self.right_group_layout)

        self.body_layout.addWidget(self.right_group)

        self.top_right_bar()

    def top_right_bar(self):
        self.top_right_bar_layout = QHBoxLayout()
        self.top_right_bar_layout.setAlignment(Qt.AlignVCenter)
        self.top_right_bar_layout.setAlignment(Qt.AlignLeft)
        self.top_right_bar_layout.setContentsMargins(10, 5, 10, 5)
        self.top_right_bar_layout.setAlignment(Qt.AlignLeft)

        self.welcome_msg = QLabel(f'Welcome to {self.school_name}')
        self.welcome_msg.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 17px;
                font-family: Times New Roman;
                }
            '''
        )
        self.top_right_bar_layout.addWidget(self.welcome_msg)

        self.sp_width = 50

        self.spacer_ = QLabel()
        self.spacer_.setFixedWidth(self.sp_width)
        self.top_right_bar_layout.addWidget(self.spacer_)

        self.search_box = QLineEdit()
        self.search_box.setFixedHeight(30)
        self.search_box.setMaximumWidth(400)
        self.search_box.setPlaceholderText('search...')
        self.search_box.setStyleSheet(
            '''
            QLineEdit {
                background-color: rgb(255, 225, 210);
                font-size: 15px;
                padding: 5px;
                border-radius: 4px;
                }
            '''
        )
        self.top_right_bar_layout.addWidget(self.search_box)

        self.search = QPushButton('search')
        self.search.setFixedSize(80, 30)
        self.search.setStyleSheet(
            '''
            QPushButton {
                background-color: rgb(245, 215, 210);
                font-size: 15px;
                font-weight: bold;
                border: 0px;
                border-radius: 4px;
                }
            .QPushButton:hover {
                border: 1px solid cyan;
                }
            '''
        )
        self.top_right_bar_layout.addWidget(self.search)

        self.messages = QPushButton('Messages')
        self.messages.setMinimumSize(80, 30)
        self.messages.setStyleSheet(
            '''
                QPushButton {
                    background-color: rgb(245, 215, 210);
                    font-size: 13px;
                    border: 0px;
                    border-radius: 4px;
                    }
                .QPushButton:hover {
                    border: 1px solid cyan;
                    }
                '''
        )
        self.top_right_bar_layout.addWidget(self.messages)

        self.notifications = QPushButton('Notifications')
        self.notifications.setMinimumSize(80, 30)
        self.notifications.setStyleSheet(
            '''
                QPushButton {
                    background-color: rgb(245, 215, 210);
                    font-size: 13px;
                    border: 0px;
                    border-radius: 4px;
                    }
                .QPushButton:hover {
                    border: 1px solid cyan;
                    }
            '''
        )
        self.top_right_bar_layout.addWidget(self.notifications)

        self.top_right_bar_group = QGroupBox()
        self.top_right_bar_group.setAlignment(Qt.AlignLeft)
        self.top_right_bar_group.setAlignment(Qt.AlignVCenter)
        self.top_right_bar_group.setFixedHeight(50)
        self.top_right_bar_group.setContentsMargins(0, 0, 0, 0)
        self.top_right_bar_group.setStyleSheet(
            '''
            QGroupBox {
                padding: 3px;
                border-bottom: 1px solid rgb(255, 170, 135);
                }
            '''
        )
        self.top_right_bar_group.setLayout(self.top_right_bar_layout)

        self.right_group_layout.addWidget(self.top_right_bar_group)

        self.user_profile()

    def user_profile(self):
        self.user_layout = QHBoxLayout()
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setAlignment(Qt.AlignLeft)

        self.user_group = QGroupBox()
        self.user_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                }
            '''
        )
        self.user_group.setContentsMargins(0, 0, 0, 0)
        self.user_group.setMinimumWidth(150)
        self.user_group.setLayout(self.user_layout)

        self.user_left = QVBoxLayout()

        self.user_image = QLabel()
        self.user_image.setStyleSheet(
            '''
                QLabel {
                    background-color: rgb(255, 170, 135);
                    border-radius: 15px;                                          
                }
                '''
        )
        self.user_image.setMinimumSize(35, 30)
        self.user_layout.addWidget(self.user_image)

        self.user_layout.addLayout(self.user_left)

        self.user_right = QVBoxLayout()
        self.user_right.setSpacing(0)

        self.user_f_name = QLabel(self.first_in)
        self.user_f_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 11px;
                }
            '''
        )
        self.user_right.addWidget(self.user_f_name)

        self.user_l_name = QLabel(self.last_in)
        self.user_l_name.setStyleSheet(
            '''
            QLabel {
                font-size: 11px;
                }
            '''
        )
        self.user_right.addWidget(self.user_l_name)

        self.user_layout.addLayout(self.user_right)

        self.top_right_bar_layout.addWidget(self.user_group)

        self.right_board()

    def right_board(self):
        self.main_panel_width = 600
        self.main_panel_height = 300

        self.right_board_layout = QHBoxLayout()
        self.right_board_layout.setAlignment(Qt.AlignCenter)
        self.right_board_layout.setSpacing(15)

        self.right_board_group = QGroupBox()
        self.right_board_group.setLayout(self.right_board_layout)
        self.right_board_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: white;
                padding: 5px;
                }
            '''
        )

        self.right_group_layout.addWidget(self.right_board_group)

        self.main_panel()
        self.notice_board()
        self.calendar_board()
    
    def main_panel(self):
        self.main_panel_layout = QVBoxLayout()
        self.main_panel_layout.setSpacing(0)

        self.main_panel_group = QGroupBox('Dashboard')
        # self.main_panel_group.setMinimumSize(self.main_panel_width + 80, self.main_panel_height)
        self.main_panel_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.main_panel_group.setLayout(self.main_panel_layout)

        self.main_panel_scroll = QScrollArea()
        self.main_panel_scroll.setMaximumSize(self.main_panel_width + 100, self.main_panel_height + 350)
        self.main_panel_scroll.setContentsMargins(0, 0, 0, 0)
        self.main_panel_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.main_panel_scroll.setWidgetResizable(True)
        self.main_panel_scroll.setWidget(self.main_panel_group)

        self.right_board_layout.addWidget(self.main_panel_scroll)

    def notice_board(self):
        self.second = QVBoxLayout()
        self.second.setContentsMargins(0, 0, 0, 0)

        self.notice_board_layout = QVBoxLayout()
        self.notice_board_layout.setSpacing(0)
        self.notice_board_layout.setAlignment(Qt.AlignLeft)

        self.notice_board_group = QGroupBox('Notice Board')
        self.notice_board_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        # self.notice_board_group.setMinimumSize()
        self.notice_board_group.setAlignment(Qt.AlignLeft)
        self.notice_board_group.setLayout(self.notice_board_layout)

        self.notice_board_scroll = QScrollArea()
        self.notice_board_scroll.setMaximumSize(self.main_panel_width - 200, self.main_panel_height)
        self.notice_board_scroll.setContentsMargins(0, 0, 0, 0)
        self.notice_board_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.notice_board_scroll.setWidgetResizable(True)
        self.notice_board_scroll.setWidget(self.notice_board_group)

        self.second.addWidget(self.notice_board_scroll)

        self.right_board_layout.addLayout(self.second)

        self.notice_board_fetch()

    def notice_board_fetch(self):
        pass

    def calendar_board(self):
        self.calendar_layout = QVBoxLayout()
        self.calendar_layout.setSpacing(0)
        self.calendar_layout.setAlignment(Qt.AlignLeft)

        self.calendar_group = QGroupBox('Calendar')
        self.calendar_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        # self.calendar_group.setMinimumSize(self.main_panel_width - 200, self.main_panel_height)
        self.calendar_group.setAlignment(Qt.AlignLeft)
        self.calendar_group.setLayout(self.calendar_layout)

        self.calendar_scroll = QScrollArea()
        self.calendar_scroll.setMaximumSize(self.main_panel_width - 200, self.main_panel_height)
        self.calendar_scroll.setContentsMargins(0, 0, 0, 0)
        self.calendar_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.calendar_scroll.setWidgetResizable(True)
        self.calendar_scroll.setWidget(self.calendar_group)

        self.second.addWidget(self.calendar_scroll)

        self.calendar_fetch()

    def calendar_fetch(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = HomePage('New School','Mohammed', 'Al Ameen')
    manager.show()
    sys.exit(app.exec_())

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
import time


class TableDef(QGroupBox):
    colors = ['#ffccff', '#ffe6ff']

    def __init__(self, number, s_name, f_name, l_name, gender):
        QGroupBox.__init__(self)

        self.number = number
        self.s_name = s_name
        self.f_name = f_name
        self.l_name = l_name
        self.gender_ = gender

        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
                background-color: white;
                padding: 3px;
            }
            '''
        )

        self.setMaximumHeight(50)


        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(10)

        self.serial_num_width = 30
        self.serial_num_height = 50
        self.name_width = 120
        self.name_height = 50
        self.button_size = (40, 30)

        self.total_width = self.serial_num_width + (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel(str(self.number))
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(self.serial_num_width, self.serial_num_height)
        self.serial_num.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                border: 1px solid #ffccff;
            }
            '''
        )
        self.table_layout.addWidget(self.serial_num)

        self.surname = QLabel(self.s_name)
        self.surname.setAlignment(Qt.AlignLeft)
        self.surname.setMaximumSize(self.name_width, self.name_height)
        self.surname.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.surname)

        self.first_name = QLabel(self.f_name)
        self.first_name.setAlignment(Qt.AlignLeft)
        self.first_name.setMaximumSize(self.name_width, self.name_height)
        self.first_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.first_name)

        self.last_name = QLabel(self.l_name)
        self.last_name.setAlignment(Qt.AlignLeft)
        self.last_name.setMaximumSize(self.name_width, self.name_height)
        self.last_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.last_name)

        self.gender = QLabel(self.gender_)
        self.gender.setAlignment(Qt.AlignLeft)
        self.gender.setMaximumSize(self.serial_num_width + 20, self.serial_num_height)
        self.gender.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.gender)

        self.view_button = QLabel('View')
        self.view_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.view_button.setMaximumSize(self.button_size[0], self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.edit_button = QLabel('Edit')
        self.edit_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.edit_button.setMaximumSize(self.button_size[0], self.button_size[1])
        self.table_layout.addWidget(self.edit_button)

        self.delete_button = QLabel('Delete')
        self.delete_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_button.setMaximumSize(self.button_size[0] + 3, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setLayout(self.table_layout)


class Table(QGroupBox):
    colors = ['#ffccff', '#ffe6ff']

    def __init__(self, id_, number, s_name, f_name, l_name, gender, username, password, s_name_in, f_name_in, l_name_in, gender_in, username_in, pass1, pass2, image_in, image):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.number = number
        self.s_name = s_name
        self.f_name = f_name
        self.l_name = l_name
        self.gender_ = gender
        self.username = username
        self.password = password
        self.image = image

        self.s_name_in = s_name_in
        self.f_name_in = f_name_in
        self.l_name_in = l_name_in
        self.gender_in = gender_in
        self.username_in = username_in
        self.pass1 = pass1
        self.pass2 = pass2
        self.image_in = image_in

        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
                background-color: white;
                padding: 3px;
            }
            '''
        )

        self.setMaximumHeight(50)

        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(10)

        self.serial_num_width = 30
        self.serial_num_height = 50
        self.name_width = 120
        self.name_height = 50
        self.button_size = (40, 30)

        self.total_width = self.serial_num_width + (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel(str(self.number))
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(self.serial_num_width, self.serial_num_height)
        self.serial_num.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                border: 1px solid #ffccff;
            }
            '''
        )
        self.table_layout.addWidget(self.serial_num)

        self.surname = QLabel(self.s_name)
        self.surname.setAlignment(Qt.AlignLeft)
        self.surname.setMaximumSize(self.name_width, self.name_height)
        self.surname.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.surname)

        self.first_name = QLabel(self.f_name)
        self.first_name.setAlignment(Qt.AlignLeft)
        self.first_name.setMaximumSize(self.name_width, self.name_height)
        self.first_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.first_name)

        self.last_name = QLabel(self.l_name)
        self.last_name.setAlignment(Qt.AlignLeft)
        self.last_name.setMaximumSize(self.name_width, self.name_height)
        self.last_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.last_name)

        self.gender = QLabel(self.gender_)
        self.gender.setAlignment(Qt.AlignLeft)
        self.gender.setMaximumSize(self.serial_num_width + 20, self.serial_num_height)
        self.gender.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.gender)

        self.view_button = QPushButton()
        self.view_button.setIcon(QIcon('Icons/view.png'))
        self.view_button.clicked.connect(self.view_slot)
        self.view_button.setStyleSheet(
            '''
            QPushButton {
                border-radius: 3px;
                background-color: #ffccee;
                }
            .QPushButton:hover {
                border: 1px solid cyan;
                }
            '''
        )
        self.view_button.setMaximumSize(self.button_size[0], self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.edit_button = QPushButton()
        self.edit_button.setIcon(QIcon('Icons/edit.png'))
        self.edit_button.clicked.connect(self.edit_slot)
        self.edit_button.setStyleSheet(
            '''
            QPushButton {
                border-radius: 3px;
                background-color: #ff99bb;
                }
            .QPushButton:hover {
                border: 1px solid cyan;
                }
            '''
        )
        self.edit_button.setMaximumSize(self.button_size[0], self.button_size[1])
        self.table_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton()
        self.delete_button.setIcon(QIcon('Icons/recycle-bin.png'))
        self.delete_button.clicked.connect(self.delete_slot)
        self.delete_button.setStyleSheet(
            '''
            QPushButton {
                border-radius: 3px;
                background-color: #ff4d4d;
                }
            .QPushButton:hover {
                border: 1px solid cyan;
                }
            '''
        )
        self.delete_button.setMaximumSize(self.button_size[0], self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setLayout(self.table_layout)

        self.fetch_user_data()

    def fetch_user_data(self):
        pass

    def view_slot(self):
        pass

    def edit_slot(self):
        self.s_name_in.setText(self.s_name)
        self.f_name_in.setText(self.f_name)
        self.l_name_in.setText(self.l_name)
        self.gender_in.setCurrentText(self.gender_)
        self.username_in.setText(self.username)
        self.pass1.setText(self.password)
        self.pass2.setText(self.password)
        image = f'{self.image}.jpg'

        try:
            img = cv2.imread(image)
            standard_width = self.image_in.width()
            standard_height = self.image_in.height()

            if image.shape[0] > standard_width and image.shape[1] > standard_height:
                self.reshaped_image = cv2.resize(img, (standard_width, standard_height))
                self.temp_path = self.image_path
                cv2.imwrite(f'{self.temp_path}', self.reshaped_image)
                image = QPixmap(self.temp_path)
                self.image_in.setPixmap(image)
                # Actual Image = self.image_path
            else:
                img = QPixmap(image)
                self.image_in.setPixmap(img)
                cv2.imwrite(f'{self.image_path}', cv2.imread(self.image_path))
        except Exception as e:
            return str(e)

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool.DataBase import delete_teacher, get_teacher_by

            teacher = get_teacher_by(self.id_)[0]
            teacher = f'{teacher[1]} {teacher[2]} {teacher[3]}'            
            
            delete_teacher(self.id_)
            # self.id_ -= 1
            msg = f'{teacher} Has been Deleted!.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

            self.setHidden(True)
            self.setEnabled(False)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)


class Teachers(QWidget):
    def __init__(self, school_name, first='', last=''):
        QWidget.__init__(self)

        self.school_name = school_name
        self.first_in = first
        self.last_in = last
        self.setWindowTitle(self.school_name)

        self.window_layout = QVBoxLayout()
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setSpacing(0)
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
                padding: 0px;
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
            from Projects.SchoolManagement.HomePages.HomePage import HomePage as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
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
            msg = 'You\'re already on the Teachers page.'
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)
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

        self.user_f_name = QLabel(self.first_in)
        self.user_f_name.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 12px;
                }
            '''
        )
        self.user_right.addWidget(self.user_f_name)

        self.user_l_name = QLabel(self.last_in)
        self.user_l_name.setStyleSheet(
            '''
            QLabel {
                font-size: 12px;
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
        self.right_board_layout = QVBoxLayout()
        self.right_board_layout.setAlignment(Qt.AlignCenter)
        self.right_board_layout.setSpacing(15)

        self.right_board_group = QGroupBox()
        self.right_board_group.setLayout(self.right_board_layout)
        self.right_board_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: white;
                }
            '''
        )

        self.right_group_layout.addWidget(self.right_board_group)

        self.teachersPAGE()

    def teachersPAGE(self):
        self.scroll_width = 1150
        self.scroll_height = 850

        self.teachers_layout = QHBoxLayout()
        self.teachers_layout.setAlignment(Qt.AlignTop)
        self.teachers_layout.setContentsMargins(0, 0, 0, 0)
        # self.teachers_layout.setSpacing(0)

        self.teachers_group = QGroupBox('Teachers')
        self.teachers_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.teachers_group.setContentsMargins(0, 0, 0, 0)
        self.teachers_group.setLayout(self.teachers_layout)

        self.teachers_scroll = QScrollArea()
        self.teachers_scroll.setMaximumSize(self.scroll_width, self.scroll_height)
        self.teachers_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.teachers_scroll.setWidgetResizable(True)
        self.teachers_scroll.setWidget(self.teachers_group)

        self.right_board_layout.addWidget(self.teachers_scroll)

        self.teachersFORM()
        self.teachersTABLE()
        self.teachersREGISTRATION()

    def teachersFORM(self):
        self.teacher_image = QLabel()
        self.reg_surname = QLineEdit()
        self.reg_f_name = QLineEdit()
        self.reg_l_name = QLineEdit()
        self.reg_new_pass = QLineEdit()
        self.reg_gender = QComboBox()
        self.reg_confirm_pass = QLineEdit()
        self.reg_username = QLineEdit()
        self.admin_username = QLineEdit()
        self.admin_pass = QLineEdit()

    def teachersTABLE(self):
        self.table_layout = QVBoxLayout()
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(0)
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.table_layout.addWidget(TableDef('s/n', 'Surname', 'First name', 'Last name', 'Gender'))

        self.total_width = 15 + (120 * 3) + 15 + 270

        self.table_group = QGroupBox()
        self.table_group.setContentsMargins(0, 0, 0, 0)
        self.table_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding-left: 5px;
                padding-right: 5px;
                background-color: rgb(250, 215, 200); 
                }
            '''
        )
        self.table_group.setLayout(self.table_layout)

        self.table_scroll = QScrollArea()
        self.table_scroll.setMaximumWidth(self.total_width)
        self.table_scroll.setWidgetResizable(True)
        self.table_scroll.setWidget(self.table_group)
        self.table_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.table_layout.setAlignment(Qt.AlignTop)

        self.teachers_layout.addWidget(self.table_scroll)

        from Projects.SchoolManagement.PanelGadgets import Exam

        self.signal_slot = Exam.GetQuestions(30)
        self.signal_slot.countChanged.connect(self.fetch_teachers)
        self.signal_slot.run()
        
        self.image_path = ''

    def teachersREGISTRATION(self):
        self.reg_layout = QVBoxLayout()
        self.reg_layout.setAlignment(Qt.AlignTop)
        # self.reg_layout.setAlignment(Qt.AlignRight)
        # self.reg_layout.setContentsMargins(0, 0, 0, 0)
        # self.reg_layout.setSpacing(0)

        self.reg_group = QGroupBox()
        self.reg_group.setAlignment(Qt.AlignHCenter)
        self.reg_group.setContentsMargins(0, 0, 0, 0)
        self.reg_group.setLayout(self.reg_layout)
        self.reg_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding-top: 0;
                padding-left: 5px;
                padding-right: 5px;
                padding-bottom: 5px;
                background-color: rgb(250, 215, 200); 
            }
            '''
        )

        self.title_layout = QHBoxLayout()
        self.title_layout.setAlignment(Qt.AlignTop)

        self.reg_layout.addLayout(self.title_layout)

        self.title = f'{self.school_name} : Teachers\'s Form'

        self.form_title = QLabel(self.title)
        self.form_title.setWordWrap(True)
        self.form_title.setStyleSheet(
            '''
            QLabel {
                padding: 5px;
                background-color: #ff9933;
                font-family: Verdana;
                font-weight: bold;
                font-size: 20px;
                color: white;
                }
            '''
        )
        self.title_layout.addWidget(self.form_title)

        self.first_layout = QVBoxLayout()
        self.first_layout.setAlignment(Qt.AlignRight)
        self.first_layout.setContentsMargins(0, 0, 0, 0)

        self.reg_layout.addLayout(self.first_layout)

        self.image_width = 300
        self.image_height = 300
        self.name_size = (170, 30)

        self.teacher_image.setAlignment(Qt.AlignCenter)
        # self.teacher_image.setPixmap(QPixmap('10.jpg'))
        self.teacher_image.setStyleSheet(
            '''
            QLabel {
                border: 1px solid black;
                }
            '''
        )
        self.teacher_image.setFixedSize(120, 100)
        self.first_layout.addWidget(self.teacher_image)

        self.choose_image = QPushButton('choose image...')
        self.choose_image.clicked.connect(self.choose_image_slot)
        self.choose_image.setMaximumSize(120, 25)
        self.first_layout.addWidget(self.choose_image)

        self.second_layout = QHBoxLayout()
        # self.second_layout.setSpacing(0)
        self.second_layout.setContentsMargins(0, 0, 0, 0)

        self.reg_layout.addLayout(self.second_layout)

        self.reg_surname.setPlaceholderText('Surname')
        self.reg_surname.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 2px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_surname.setMaximumSize(self.name_size[0], self.name_size[1])
        self.second_layout.addWidget(self.reg_surname)

        self.reg_f_name.setPlaceholderText('First name')
        self.reg_f_name.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 2px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_f_name.setMaximumSize(self.name_size[0], self.name_size[1])
        self.second_layout.addWidget(self.reg_f_name)

        self.reg_l_name.setPlaceholderText('Last name')
        self.reg_l_name.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 2px;
                font-size: 13px;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_f_name.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 2px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_l_name.setMaximumSize(self.name_size[0], self.name_size[1])
        self.second_layout.addWidget(self.reg_l_name)

        self.third_layout = QHBoxLayout()
        # self.third_layout.setSpacing(0)
        self.third_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.third_layout)

        self.reg_new_pass.setPlaceholderText('New password')
        self.reg_new_pass.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 2px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_new_pass.setMaximumSize(self.name_size[0], self.name_size[1])
        self.reg_new_pass.setEchoMode(QLineEdit.Password)
        self.third_layout.addWidget(self.reg_new_pass)

        self.reg_gender_font = QFont('Verdana', 8)

        self.reg_gender.setFont(self.reg_gender_font)
        self.reg_gender.addItem('--gender--')
        self.reg_gender.addItem('Male')
        self.reg_gender.addItem('Female')
        self.reg_gender.setMaximumSize(self.name_size[0], self.name_size[1])
        self.third_layout.addWidget(self.reg_gender)

        self.reg_confirm_pass.setPlaceholderText('Confirm password')
        self.reg_confirm_pass.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 1px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.reg_confirm_pass.setMaximumSize(self.name_size[0], self.name_size[1])
        self.reg_confirm_pass.setEchoMode(QLineEdit.Password)
        self.third_layout.addWidget(self.reg_confirm_pass)

        self.fourth_layout = QHBoxLayout()
        self.fourth_layout.setAlignment(Qt.AlignCenter)
        self.fourth_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.fourth_layout)

        self.reg_username.setPlaceholderText('Username')
        self.reg_username.setMaximumSize(self.name_size[0], self.name_size[1])
        self.reg_username.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 1px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.fourth_layout.addWidget(self.reg_username)

        self.admin_layout = QHBoxLayout()
        self.admin_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.admin_layout)

        self.admin_username.setPlaceholderText('Admin Username')
        self.admin_username.setMaximumSize(self.name_size[0], self.name_size[1])
        self.admin_username.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 1px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.admin_layout.addWidget(self.admin_username)

        self.spacing = QLabel()
        self.spacing.setMaximumSize(self.name_size[0], self.name_size[1])
        self.admin_layout.addWidget(self.spacing)

        self.admin_pass.setPlaceholderText('Admin password')
        self.admin_pass.setStyleSheet(
            '''
            QLineEdit {
                border-radius: 1px;
                font-size: 13px;
                font-family: Verdana;
                /* font-style: italic; */
                padding: 5px;
                }
           '''
        )
        self.admin_pass.setMaximumSize(self.name_size[0], self.name_size[1])
        self.admin_pass.setEchoMode(QLineEdit.Password)
        self.admin_layout.addWidget(self.admin_pass)

        self.reg_layout.addWidget(self.spacing)

        self.last_layout = QHBoxLayout()
        self.last_layout.setAlignment(Qt.AlignCenter)
        self.last_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.last_layout)

        self.reg_button_size = (150, 30)

        self.reg_update_button = QPushButton('Update')
        self.reg_update_button.clicked.connect(self.reg_update_slot)
        self.reg_update_button.setFixedSize(self.reg_button_size[0], self.reg_button_size[1])
        self.reg_update_button.setStyleSheet(
            '''
            QPushButton {
                background-color: #ff8c1a;
                border: 0px;
                font-family: Verdana;
                border-radius: 2px;
                font-size: 14px;
                color: white;
                }
            .QPushButton:hover {
                background-color: #ff9933;
                }
            '''
        )
        self.last_layout.addWidget(self.reg_update_button)

        self.reg_scroll = QScrollArea()
        self.reg_scroll.setWidgetResizable(True)
        self.reg_scroll.setWidget(self.reg_group)
        self.reg_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )

        self.teachers_layout.addWidget(self.reg_scroll)

    def fetch_teachers(self):
        try:
            from Projects.SchoolManagement.DataBaseTool.DataBase import get_teacher_all
            # (self, number, s_name, f_name, l_name, gender, username, password, s_name_in, f_name_in, l_name_in, gender_in, username_in, pass1, pass2):
            all_teachers = get_teacher_all()
            self.id_index = 1

            if len(all_teachers) != 0 and all_teachers != 'NULL':
                for teacher in all_teachers:
                    id_ = self.id_index
                    surname = teacher[1]
                    f_name = teacher[2]
                    l_name = teacher[3]
                    gender = teacher[4]
                    username = teacher[5]
                    password = teacher[6]

                    self.table_layout.addWidget(Table(teacher[0], id_, surname, f_name, l_name, gender, username, password, self.reg_surname, self.reg_f_name, self.reg_l_name, self.reg_gender, self.reg_username, self.reg_new_pass, self.reg_confirm_pass, self.teacher_image, teacher[0]))
                    self.id_index += 1
            else:
                return('NULL')

        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)

    def refresh_teachers(self):
        try:
            from Projects.SchoolManagement.DataBaseTool.DataBase import get_teacher_all
            # (self, number, s_name, f_name, l_name, gender, username, password, s_name_in, f_name_in, l_name_in, gender_in, username_in, pass1, pass2):
            teacher = get_teacher_all()

            id_ = self.id_index
            surname = teacher[-1][1]
            f_name = teacher[-1][2]
            l_name = teacher[-1][3]
            gender = teacher[-1][4]
            username = teacher[-1][5]
            password = teacher[-1][6]
            image = teacher[-1][7]
            self.table_layout.addWidget(Table(id_, surname, f_name, l_name, gender, username, password, self.reg_surname, self.reg_f_name, self.reg_l_name, self.reg_gender, self.reg_username, self.reg_new_pass, self.reg_confirm_pass, self.teacher_image, teacher[-1][0]))
            print(teacher[-1][0])
            self.id_index += 1
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)

    def choose_image_slot(self):
        try:
            self.file_dialog_window = QFileDialog.getOpenFileName(self, 'Select image', 'C\\', 'Image (*.jpg *.png *.svg)')
            self.image_path = self.file_dialog_window[0]
            img = cv2.imread(self.image_path)
            standard_width = self.teacher_image.width()
            standard_height = self.teacher_image.height()

            if img.shape[0] > standard_width and img.shape[1] > standard_height:
                self.reshaped_image = cv2.resize(img, (standard_width, standard_height))
                self.temp_path = self.image_path + 'temp.png'
                cv2.imwrite(f'{self.temp_path}', self.reshaped_image)
                image = QPixmap(self.temp_path)
                self.teacher_image.setPixmap(image)
                # Actual Image = self.image_path
            else:
                image = QPixmap(self.image_path)
                self.teacher_image.setPixmap(image)
                cv2.imwrite(f'{self.image_path}', cv2.imread(self.image_path))
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)
    def clear_form_field(self):
        self.reg_surname.setText('')
        self.reg_f_name.setText('')
        self.reg_l_name.setText('')
        self.reg_new_pass.setText('')
        self.reg_gender.setCurrentText('--gender--')
        self.reg_confirm_pass.setText('')
        self.reg_username.setText('')
        self.admin_username.setText('')
        self.admin_pass.setText('')

    def reg_update_slot(self):
        try:
            reg_surname = self.reg_surname.text()
            reg_f_name = self.reg_f_name.text()
            reg_l_name = self.reg_l_name.text()
            reg_new_pass = self.reg_new_pass.text()
            reg_gender = self.reg_gender.currentText()
            reg_confirm_pass = self.reg_confirm_pass.text()
            reg_username = self.reg_username.text()
            admin_username = self.admin_username.text()
            admin_pass = self.admin_pass.text()

            if (len(reg_surname) and len(reg_f_name) and len(reg_username)) != 0:
                if reg_gender != '--gender--':
                    if (len(reg_new_pass) and len(reg_confirm_pass)) != 0:
                        if reg_new_pass == reg_confirm_pass:
                            if (len(admin_username) and len(admin_pass) != 0):
                                if admin_username and admin_pass:
                                    from Projects.SchoolManagement.DataBaseTool.DataBase import create_teacher, insert_teacher, get_teacher, get_admin_by
                                    from Projects.SchoolManagement.DataBaseTool import DataBase
                                    
                                    admin_usernames = get_admin_by('username')
                                    admin_passwords = get_admin_by('password')

                                    if admin_username in admin_usernames:
                                        admin_id = admin_usernames.index(admin_username)
                                        if admin_pass == admin_passwords[admin_id]:

                                            create_teacher()

                                            teachers_usernames = get_teacher('username')

                                            if reg_username in teachers_usernames:
                                                pseudo_id_ = teachers_usernames.index(reg_username)
                                                id_ = DataBase.get_teacher_all_id()[pseudo_id_]
                                                insert_teacher(id_, reg_surname, reg_f_name, reg_l_name, reg_gender, reg_username, reg_new_pass, admin_username, admin_pass, self.image_path)
                                                
                                                msg = 'Username already exist, please try another username.\nIf you are not trying to create a new account,\n i have updated your information.'
                                                message_box = QMessageBox()
                                                message_box.about(self, self.school_name, msg)
                                            else:
                                                teachers_ids = get_teacher('id')
                                                if len(teachers_ids) != 0:
                                                    id_ = int(teachers_ids[-1]) + 1
                                                    if self.image_path != '':
                                                        insert_teacher(id_, reg_surname, reg_f_name, reg_l_name, reg_gender, reg_username, reg_new_pass, admin_username, admin_pass, self.image_path)

                                                        msg = f'''Admin {admin_username} has successfully registered\n 
                                                        {reg_surname} {reg_f_name} {reg_l_name} as a Teacher.'''
                                                        message_box = QMessageBox()
                                                        message_box.about(self, self.school_name, msg)

                                                        self.refresh_teachers()
                                                        self.clear_form_field()
                                                    else:
                                                        insert_teacher(id_, reg_surname, reg_f_name, reg_l_name, reg_gender, reg_username, reg_new_pass, admin_username, admin_pass)

                                                        msg = f'''Admin {admin_username} has successfully registered\n 
                                                        {reg_surname} {reg_f_name} {reg_l_name} as a Teacher.'''
                                                        message_box = QMessageBox()
                                                        message_box.about(self, self.school_name, msg)

                                                        self.refresh_teachers()
                                                        self.clear_form_field()
                                                else:
                                                    if self.image_path != '':
                                                        insert_teacher(1, reg_surname, reg_f_name, reg_l_name, reg_gender, reg_username, reg_new_pass, admin_username, admin_pass, self.image_path)

                                                        msg = f'''Admin {admin_username} has successfully registered\n 
                                                        {reg_surname} {reg_f_name} {reg_l_name} as a Teacher.'''
                                                        message_box = QMessageBox()
                                                        message_box.about(self, self.school_name, msg)

                                                        self.refresh_teachers()
                                                        self.clear_form_field()
                                                    else:
                                                        insert_teacher(1, reg_surname, reg_f_name, reg_l_name, reg_gender, reg_username, reg_new_pass, admin_username, admin_pass)

                                                        msg = f'''Admin {admin_username} has successfully registered\n 
                                                        {reg_surname} {reg_f_name} {reg_l_name} as a Teacher.'''
                                                        message_box = QMessageBox()
                                                        message_box.about(self, self.school_name, msg)
                                                        self.clear_form_field()
                                        else:
                                            msg = 'Admin password authentification failed!.\n Try again'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)
                                    else:
                                        msg = 'Admin username does not exist!'
                                        message_box = QMessageBox()
                                        message_box.about(self, self.school_name, msg)
                                else:
                                    msg = 'Admin authentification failed due to incorrect login details!'
                                    message_box = QMessageBox()
                                    message_box.about(self, self.school_name, msg)
                            else:
                                msg = 'You need admin access to continue the registration\n please fill the required field(s).'
                                message_box = QMessageBox()
                                message_box.about(self, self.school_name, msg)
                        else:
                            msg = 'Password mismatch!'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)
                    else:
                        msg = 'You need to create a password\n please fill the required field(s).'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                else:
                    msg = 'You need to select your gender.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            else:
                msg = 'Please fill all fields to proceed.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     manager = Teachers('New School')
#     manager.show()
#     sys.exit(app.exec_())

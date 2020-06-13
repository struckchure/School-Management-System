from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class StudentTable(QGroupBox):
    def __init__(self, id_='', serial='', surname='', first_name='', last_name='', class_='', reg_number='', gender='',surname_in='', first_in='', last_in='', reg_num_in='', reg_pin_in='', class_in='', gender_in='', teacher_in=''):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.serial = serial
        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name
        self.reg_number = reg_number
        self.class_ = class_
        self.gender = gender

        self.surname_in = surname_in
        self.first_in = first_in
        self.last_in = last_in
        self.reg_num_in = reg_num_in
        self.reg_pin_in = reg_pin_in
        self.class_in = class_in
        self.gender_in = gender_in
        self.teacher_in = teacher_in

        self.table_layout = QGridLayout()
        self.table_layout.setSpacing(10)
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.table_layout)
        self.setMaximumHeight(50)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
                background-color: white;
                padding: 3px;
            }
            '''
        )
        self.fields()

    def fields(self):
        id_size = (30, 50)
        self.id_b = QLabel(str(self.id_))
        self.id_b.setAlignment(Qt.AlignCenter)
        self.id_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                border: 1px solid #ffccff;
            }
            '''
        )
        self.id_b.setMaximumSize(id_size[0], id_size[1])
        self.table_layout.addWidget(self.id_b, 0, 0)

        name_size = (120, 50)
        self.sur = QLabel(self.surname)
        self.sur.setAlignment(Qt.AlignLeft)
        self.sur.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.sur.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.sur, 0, 1)

        self.first = QLabel(self.first_name)
        self.first.setAlignment(Qt.AlignLeft)
        self.first.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.first.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.first, 0, 2)

        self.last = QLabel(self.last_name)
        self.last.setAlignment(Qt.AlignLeft)
        self.last.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.last.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.last, 0, 3)

        class_size = (60, 50)

        self.reg_b = QLabel(self.reg_number)
        self.reg_b.setAlignment(Qt.AlignLeft)
        self.reg_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.reg_b.setMaximumSize(class_size[0] + 15, class_size[1])
        self.table_layout.addWidget(self.reg_b, 0, 4)

        self.class_b = QLabel(self.class_)
        self.class_b.setAlignment(Qt.AlignLeft)
        self.class_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.class_b.setMaximumSize(class_size[0], class_size[1])
        self.table_layout.addWidget(self.class_b, 0, 5)

        gender_size = (85, 50)
        self.gender_b = QLabel(self.gender)
        self.gender_b.setAlignment(Qt.AlignLeft)
        self.gender_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.gender_b.setMaximumSize(gender_size[0], gender_size[1])
        self.table_layout.addWidget(self.gender_b, 0, 6)
        
        button_size = (40, 30)

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
        self.edit_button.setMaximumSize(button_size[0], button_size[1])
        self.table_layout.addWidget(self.edit_button, 0, 8)

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
        self.delete_button.setMaximumSize(button_size[0], button_size[1])
        self.table_layout.addWidget(self.delete_button, 0, 9)

    def edit_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            teacher = DataBase.get_class_teacher(self.class_)
            PIN = DataBase.get_school_students_by_id(self.serial)[-1]

            self.surname_in.setText(self.surname)
            self.first_in.setText(self.first_name)
            self.last_in.setText(self.last_name)
            self.class_in.setCurrentText(self.class_)
            self.gender_in.setCurrentText(self.gender)
            self.teacher_in.setCurrentText(teacher)
            self.reg_num_in.setText(self.reg_number)
            self.reg_pin_in.setText(str(PIN))
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            DataBase.delete_school_student(self.serial)
            
            self.setHidden(True)
            self.setEnabled(False)
        except Exception as e:
            raise e


class StudentTableDef(QGroupBox):
    def __init__(self, id_='s/n', surname='Surname', first_name='First name', last_name='Last name', reg_number='Reg Num', class_='Class', gender='Gender'):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name
        self.reg_number = reg_number
        self.class_ = class_
        self.gender = gender

        self.table_layout = QGridLayout()
        # self.table_layout.setAlignment(Qt.AlignLeft)
        self.table_layout.setSpacing(10)
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.table_layout)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
                background-color: white;
                padding: 3px;
            }
            '''
        )

        self.fields()

    def fields(self):
        id_size = (30, 50)
        self.id_b = QLabel(str(self.id_))
        self.id_b.setAlignment(Qt.AlignCenter)
        self.id_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                border: 1px solid #ffccff;
                font-size: 13px;
            }
            '''
        )
        self.id_b.setMaximumSize(id_size[0], id_size[1])
        self.table_layout.addWidget(self.id_b, 0, 0)

        name_size = (120, 50)
        self.sur = QLabel(self.surname)
        self.sur.setAlignment(Qt.AlignLeft)
        self.sur.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.sur.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.sur, 0, 1)

        self.first = QLabel(self.first_name)
        self.first.setAlignment(Qt.AlignLeft)
        self.first.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.first.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.first, 0, 2)

        self.last = QLabel(self.last_name)
        self.last.setAlignment(Qt.AlignLeft)
        self.last.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.last.setMaximumSize(name_size[0], name_size[1])
        self.table_layout.addWidget(self.last, 0, 3)

        class_size = (60, 50)

        self.reg_b = QLabel(self.reg_number)
        self.reg_b.setAlignment(Qt.AlignLeft)
        self.reg_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.reg_b.setMaximumSize(class_size[0] + 15, class_size[1])
        self.table_layout.addWidget(self.reg_b, 0, 4)

        self.class_b = QLabel(self.class_)
        self.class_b.setAlignment(Qt.AlignLeft)
        self.class_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.class_b.setMaximumSize(class_size[0], class_size[1])
        self.table_layout.addWidget(self.class_b, 0, 5)

        gender_size = (85, 50)
        self.gender_b = QLabel(self.gender)
        self.gender_b.setAlignment(Qt.AlignLeft)
        self.gender_b.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                }
            '''
        )
        self.gender_b.setMaximumSize(gender_size[0], gender_size[1])
        self.table_layout.addWidget(self.gender_b, 0, 6)
        
        button_size = (40, 30)

        self.edit_button = QLabel('Edit')
        self.edit_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.edit_button.setMaximumSize(button_size[0], button_size[1])
        self.table_layout.addWidget(self.edit_button, 0, 7)

        self.delete_button = QLabel('Delete')
        self.delete_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_button.setMaximumSize(button_size[0] + 3, button_size[1])
        self.table_layout.addWidget(self.delete_button, 0, 8)


class DistributeStudents(QThread):
    countChanged = pyqtSignal(int)
    def __init__(self, duration=100):
        QThread.__init__(self)
        self.duration = len(duration)

    def run(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            all_students = DataBase.get_school_students()
            all_students_copy = all_students
            while self.duration > 0:
                self.countChanged.emit(self.duration)
                self.duration -= 1
                break
        except Exception as e:
            raise e


class Students(QWidget):
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
            msg = 'You\'re already on the Student\'s page.'
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)
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
        # self.right_board_layout.setSpacing(15)

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

        self.studentsPAGE()

    def studentsPAGE(self):
        self.scroll_width = 1150
        self.scroll_height = 850
        self.students_layout = QVBoxLayout()
        self.students_layout.setContentsMargins(0, 0, 0, 0)
        self.students_layout.setSpacing(0)

        self.students_group = QGroupBox('Students')
        self.students_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.students_group.setContentsMargins(0, 0, 0, 0)
        self.students_group.setLayout(self.students_layout)

        self.students_scroll = QScrollArea()
        self.students_scroll.setMaximumSize(self.scroll_width, self.scroll_height)
        self.students_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.students_scroll.setWidgetResizable(True)
        self.students_scroll.setWidget(self.students_group)

        self.right_board_layout.addWidget(self.students_scroll)
        self.studentSPLIT()

    def studentSPLIT(self):
        self.split_layout = QHBoxLayout()
        self.split_layout.setContentsMargins(0, 0, 0, 0)
        self.split_layout.setSpacing(0)
        
        self.split_group = QGroupBox()
        self.split_group.setLayout(self.split_layout)
        self.split_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                }
            '''
        )

        self.split_scroll = QScrollArea()
        self.split_scroll.setMaximumSize(self.scroll_width, self.scroll_height)
        self.split_scroll.setWidget(self.split_group)
        self.split_scroll.setWidgetResizable(True)
        self.split_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.students_layout.addWidget(self.split_scroll)

        self.split_size = (self.scroll_width / 2, 600)

        self.studentTABLE()
        self.studentFORM()
        self.studentLEFT()

    def studentFORM(self):
        self.reg_image = QLabel()
        self.reg_surname = QLineEdit()
        self.reg_f_name = QLineEdit()
        self.reg_l_name = QLineEdit()
        self.reg_class = QComboBox()
        self.reg_number = QLineEdit()
        self.reg_gender = QComboBox()
        self.reg_PIN = QLineEdit()
        self.teacher_username = QComboBox()
        self.teacher_pass = QLineEdit()

    def serveTEACHERS(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            all_teachers = DataBase.get_teacher_names()
            if len(all_teachers) != 0:
                for teacher in all_teachers:
                    self.teacher_username.addItem(teacher)
        except Exception as e:
            # raise e
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)

    def serveCLASS(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            all_classes = DataBase.get_school_class()
            if len(all_classes) != 0:
                for class_ in all_classes:
                    self.reg_class.addItem(class_)
        except Exception as e:
            # raise e
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)

    def studentLEFT(self):
        self.reg_layout = QVBoxLayout()
        self.reg_layout.setAlignment(Qt.AlignTop)
        # self.reg_layout.setAlignment(Qt.AlignRight)
        # self.reg_layout.setContentsMargins(0, 0, 0, 0)
        # self.reg_layout.setSpacing(0)

        self.reg_group = QGroupBox()
        self.reg_group.setMaximumWidth(600)
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

        self.title = f'{self.school_name} : Student\'s Form'

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

        self.reg_image.setAlignment(Qt.AlignCenter)
        # self.reg_image.setPixmap(QPixmap('10.jpg'))
        self.reg_image.setStyleSheet(
            '''
            QLabel {
                border: 1px solid black;
                }
            '''
        )
        self.reg_image.setFixedSize(120, 100)
        self.first_layout.addWidget(self.reg_image)

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
        
        self.reg_gender_font = QFont('Verdana', 8)
        
        self.mid_third_layout = QHBoxLayout()
        self.mid_third_layout.setContentsMargins(0, 0, 0, 0)
        self.mid_third_layout.setAlignment(Qt.AlignCenter)
        self.reg_layout.addLayout(self.mid_third_layout)

        self.reg_class.setFont(self.reg_gender_font)
        self.reg_class.addItem('--class--')
        self.reg_class.currentIndexChanged.connect(self.select_teacher)
        self.reg_class.setMaximumSize(self.name_size[0], self.name_size[1])
        self.mid_third_layout.addWidget(self.reg_class)
        self.serveCLASS()

        self.third_layout = QHBoxLayout()
        # self.third_layout.setSpacing(0)
        self.third_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.third_layout)

        self.reg_number.setPlaceholderText('Reg Number')
        self.reg_number.setStyleSheet(
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
        self.reg_number.setMaximumSize(self.name_size[0], self.name_size[1])
        # self.reg_number.setEchoMode(QLineEdit.Password)
        self.third_layout.addWidget(self.reg_number)

        self.reg_gender.setFont(self.reg_gender_font)
        self.reg_gender.addItem('--gender--')
        self.reg_gender.addItem('Male')
        self.reg_gender.addItem('Female')
        self.reg_gender.setMaximumSize(self.name_size[0], self.name_size[1])
        self.third_layout.addWidget(self.reg_gender)

        self.reg_PIN.setPlaceholderText('PIN')
        self.reg_PIN.setStyleSheet(
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
        self.reg_PIN.setMaximumSize(self.name_size[0], self.name_size[1])
        # self.reg_PIN.setEchoMode(QLineEdit.Password)
        self.third_layout.addWidget(self.reg_PIN)

        self.fourth_layout = QHBoxLayout()
        self.fourth_layout.setAlignment(Qt.AlignCenter)
        self.fourth_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.fourth_layout)

        self.admin_layout = QHBoxLayout()
        self.admin_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.admin_layout)

        self.teacher_username.setFont(self.reg_gender_font)
        self.teacher_username.addItem('--Teacher username--')
        self.teacher_username.setMaximumSize(self.name_size[0], self.name_size[1])
        self.admin_layout.addWidget(self.teacher_username)
        self.serveTEACHERS()

        self.spacing = QLabel()
        self.spacing.setMaximumSize(self.name_size[0], self.name_size[1])

        self.auto_gen = QCheckBox('Auto Generate')
        # self.auto_gen.setWordWrap(True)
        # print(dir(self.auto_gen))
        # self.spacing.setMaximumSize(self.name_size[0], self.name_size[1])
        self.admin_layout.addWidget(self.auto_gen)

        self.teacher_pass.setPlaceholderText('Teacher password')
        self.teacher_pass.setStyleSheet(
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
        self.teacher_pass.setMaximumSize(self.name_size[0], self.name_size[1])
        self.teacher_pass.setEchoMode(QLineEdit.Password)
        self.admin_layout.addWidget(self.teacher_pass)

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

        self.split_layout.addWidget(self.reg_scroll)

        self.image_path = ''
        self.index = 1

    def select_teacher(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            if self.reg_class.currentText() != '--class--':
                teacher = DataBase.get_class_teacher(self.reg_class.currentText())
                self.teacher_username.setCurrentText(teacher)
            else:
                self.teacher_username.setCurrentText('--Teacher Username--')
        except Exception as e:
            raise e

    def choose_image_slot(self):
        try:
            import cv2

            self.file_dialog_window = QFileDialog.getOpenFileName(self, 'Select image', 'C\\', 'Image (*.jpg *.png *.svg)')
            self.image_path = self.file_dialog_window[0]
            img = cv2.imread(self.image_path)
            standard_width = self.reg_image.width()
            standard_height = self.reg_image.height()

            if img.shape[0] > standard_width and img.shape[1] > standard_height:
                self.reshaped_image = cv2.resize(img, (standard_width, standard_height))
                self.temp_path = self.image_path + 'temp.png'
                cv2.imwrite(f'{self.temp_path}', self.reshaped_image)
                image = QPixmap(self.temp_path)
                self.reg_image.setPixmap(image)
                # Actual Image = self.image_path
            else:
                image = QPixmap(self.image_path)
                self.reg_image.setPixmap(image)
                cv2.imwrite(f'{self.image_path}', cv2.imread(self.image_path))
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)

    def reg_pin(self):
        import random
        import time

        alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        clock = time.gmtime()
        year = clock.tm_year

        self.new_reg_number = f'{year}{random.choice(alphas).capitalize()}{random.choice(alphas).capitalize()}{random.choice(alphas).capitalize()}'
        self.new_reg_PIN = f'{random.randint(1000, 9999)}'

        return self.new_reg_number, self.new_reg_PIN
    def refresh(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase
            student = DataBase.get_school_students()[-1]
            self.table_layout_stud.addWidget(StudentTable(
                self.index,
                student[0], # id
                student[1], # surname
                student[2], # first_name
                student[3], # last_name
                student[4], # class
                student[5], # reg
                student[6], # gender
                self.reg_surname, 
                self.reg_f_name, 
                self.reg_l_name, 
                self.reg_number, 
                self.reg_PIN, 
                self.reg_class,
                self.reg_gender, 
                self.teacher_username)
            )
            self.index += 1
        except Exception as e:
            raise e

    def clear_from_field(self):
        self.reg_surname.setText('')
        self.reg_f_name.setText('')
        self.reg_l_name.setText('')
        self.reg_class.setCurrentText('--class--')
        self.reg_number.setText('')
        self.reg_gender.setCurrentText('--gender--')
        self.reg_PIN.setText('')
        self.teacher_username.setCurrentText('--Teacher username--')
        self.teacher_pass.setText('')
        self.auto_gen.setCheckState(False)

    def reg_update_slot(self):
        if self.auto_gen.isChecked() is True:
            try:
                from Projects.SchoolManagement.DataBaseTool import DataBase
                
                surname = self.reg_surname
                first_name = self.reg_f_name
                last_name = self.reg_l_name
                class_ = self.reg_class
                reg_num = self.reg_number
                gender = self.reg_gender
                pin = self.reg_PIN

                DataBase.create_school_students()

                if (len(first_name.text()) and len(surname.text())) != 0:
                    if (len(class_.currentText()) != '--class--'):
                        if (gender.currentText() != '--gender--'):
                            creds = self.reg_pin()
                            reg_num_new = creds[0]
                            reg_pin_new = creds[1]
                            
                            teachers = DataBase.get_teacher('username')
                            if (self.teacher_username.currentText() != '--Teacher Username--') and self.teacher_username.currentText() in teachers:
                                user_passwords = DataBase.get_teacher('password')
                                existing_pass = user_passwords[teachers.index(self.teacher_username.currentText())]
                                if self.teacher_pass.text() == existing_pass:
                                    all_reg_nums = DataBase.get_students_by_column('reg_num')
                                    if reg_num.text() in all_reg_nums:
                                        creds_ex = self.reg_pin()
                                        reg_num_new = creds_ex[0]
                                        reg_pin_new = creds_ex[1]

                                        if len(all_reg_nums) != 0:
                                            id_ = all_reg_nums.index(all_reg_nums[-1]) + 1
                                            DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                            
                                            msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)

                                            self.refresh()
                                            self.clear_from_field()
                                        else:
                                            id_ = 0
                                            DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                            
                                            msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)

                                            self.refresh()
                                            self.clear_from_field()
                                    else:
                                        if len(all_reg_nums) != 0:
                                            id_ = all_reg_nums.index(all_reg_nums[-1]) + 1
                                            DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                            
                                            msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)

                                            self.refresh()
                                            self.clear_from_field()
                                        else:
                                            id_ = 0
                                            DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                            
                                            msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)

                                            self.refresh()
                                            self.clear_from_field()
                                else:
                                    msg = f'{self.teacher_username.currentText()}, your password is incorrect.'
                                    message_box = QMessageBox()
                                    message_box.about(self, self.school_name, msg)
                            else:
                                msg = f'Please select your Username.'
                                message_box = QMessageBox()
                                message_box.about(self, self.school_name, msg)    
                        else:
                            msg = 'Please select your gender.'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)   
                    else:
                        msg = 'Please select a class.'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                else:
                    msg = 'All fields must be filled.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            except Exception as e:
                raise e
        else:
            try:
                from Projects.SchoolManagement.DataBaseTool import DataBase
                
                surname = self.reg_surname
                first_name = self.reg_f_name
                last_name = self.reg_l_name
                class_ = self.reg_class
                reg_num = self.reg_number
                gender = self.reg_gender
                pin = self.reg_PIN

                DataBase.create_school_students()
                if (len(first_name.text()) and len(surname.text())) != 0:
                    if (class_.currentText() != '--class--'):
                        if (len(reg_num.text()) != 0):
                            if (gender.currentText() != '--gender--'):
                                if (len(pin.text()) != 0):
                                    reg_num_new = reg_num.text()
                                    reg_pin_new = pin.text()
                                    
                                    teachers = DataBase.get_teacher('username')
                                    if (self.teacher_username.currentText() != '--Teacher Username--') and self.teacher_username.currentText() in teachers:
                                        user_passwords = DataBase.get_teacher('password')
                                        user_id = teachers.index(self.teacher_username.currentText())
                                        existing_pass = user_passwords[user_id]
                                        if self.teacher_pass.text() == existing_pass:
                                            all_reg_nums = DataBase.get_students_by_column('reg_num')
                                            # if reg_num.text() in all_reg_nums:
                                            #     msg = 'Reg Number already taken, please input a different Reg Number or select Auto Generation.'
                                            #     message_box = QMessageBox()
                                            #     message_box.about(self, self.school_name, msg)
                                            # else:
                                            if True:
                                                if len(all_reg_nums) != 0:
                                                    id_ = all_reg_nums.index(all_reg_nums[-1]) + 1
                                                    DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                                    
                                                    msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                                    message_box = QMessageBox()
                                                    message_box.about(self, self.school_name, msg)

                                                    self.refresh()
                                                else:
                                                    id_ = 0
                                                    DataBase.insert_school_students(id_, surname.text(), first_name.text(), last_name.text(), class_.currentText(), reg_num_new, gender.currentText(), reg_pin_new)
                                                    
                                                    msg = f'You\'ve successfully registered {reg_num_new} with PIN {reg_pin_new}.'
                                                    message_box = QMessageBox()
                                                    message_box.about(self, self.school_name, msg)

                                                    self.refresh()
                                        else:
                                            msg = f'{self.teacher_username.currentText()}, your password is incorrect.'
                                            message_box = QMessageBox()
                                            message_box.about(self, self.school_name, msg)
                                else:
                                    msg = 'Please choose your PIN.'
                                    message_box = QMessageBox()
                                    message_box.about(self, self.school_name, msg)
                            else:
                                msg = 'Please select your gender.'
                                message_box = QMessageBox()
                                message_box.about(self, self.school_name, msg)
                        else:
                            msg = 'Please provide your registration number.'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)    
                    else:
                        msg = 'Please select a class.'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                else:
                    msg = 'All fields must be filled.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            except Exception as e:
                raise e

    def studentTABLE(self):
        try:
            self.table_layout_stud = QVBoxLayout()
            self.table_layout_stud.setContentsMargins(0, 0, 0, 0)
            self.table_layout_stud.setAlignment(Qt.AlignTop)
            self.table_layout_stud.setSpacing(0)

            self.table_group_stud = QGroupBox()
            self.table_group_stud.setAlignment(Qt.AlignLeft)
            self.table_group_stud.setLayout(self.table_layout_stud)
            self.table_group_stud.setStyleSheet(
                '''
                QGroupBox {
                    border: 0px;
                    }
                '''
            )

            self.table_scroll_stud = QScrollArea()
            self.table_scroll_stud.setWidget(self.table_group_stud)
            self.table_scroll_stud.setWidgetResizable(True)

            self.split_layout.addWidget(self.table_scroll_stud)
            
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.table_layout_stud.addWidget(StudentTableDef())
            
            all_students = DataBase.get_school_students()

            self.calc = DistributeStudents(all_students)
            self.calc.countChanged.connect(self.onCountChanged)
            self.calc.start()
        except Exception as e:
            raise e

    def onCountChanged(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase
            
            all_students = DataBase.get_school_students()
            if len(all_students) != 0:
                all_students_copy = all_students
                for student in all_students_copy:
                    table = StudentTable()
                    self.table_layout_stud.addWidget(StudentTable(
                        self.index,
                        student[0], # id
                        student[1], # surname
                        student[2], # first_name
                        student[3], # last_name
                        student[4], # class
                        student[5], # reg
                        student[6], # gender
                        self.reg_surname, 
                        self.reg_f_name, 
                        self.reg_l_name, 
                        self.reg_number, 
                        self.reg_PIN, 
                        self.reg_class,
                        self.reg_gender, 
                        self.teacher_username))
                    self.index += 1
        except Exception as e:
            raise e


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     manager = Students()
#     manager.show()
#     sys.exit(app.exec_())

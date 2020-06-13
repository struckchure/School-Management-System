from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time


class TableDef(QGroupBox):
    colors = ['#ffccff', '#ffe6ff']

    def __init__(self):
        QGroupBox.__init__(self)

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
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 50
        self.name_width = 90
        self.name_height = 50
        self.number_width = 35
        self.button_size = (40, 30)

        self.total_width = self.serial_num_width + (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel('s/n')
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

        self.teacher_label = QLabel("Teacher")
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(self.name_width, self.name_height)
        self.teacher_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.teacher_label)

        self.class_label = QLabel("Class")
        self.class_label.setAlignment(Qt.AlignLeft)
        self.class_label.setMaximumSize(self.name_width + 30, self.name_height)
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.class_label)

        self.male_label = QLabel('M')
        self.male_label.setAlignment(Qt.AlignLeft)
        self.male_label.setMaximumSize(self.number_width, self.name_height)
        self.male_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.male_label)
        
        self.female_label = QLabel('F')
        self.female_label.setAlignment(Qt.AlignLeft)
        self.female_label.setMaximumSize(self.number_width, self.name_height)
        self.female_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.female_label)

        self.total = QLabel('Tt')
        self.total.setAlignment(Qt.AlignLeft)
        self.total.setMaximumSize(self.number_width, self.serial_num_height)
        self.total.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.total)

        self.subjects = QLabel('S')
        self.subjects.setAlignment(Qt.AlignLeft)
        self.subjects.setMaximumSize(self.number_width, self.serial_num_height)
        self.subjects.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subjects)

        self.edit_button = QLabel('Edit')
        # self.edit_button.setPixmap(QPixmap('Icons/edit.png'))
        self.edit_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.edit_button.setMaximumSize(self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.edit_button)

        self.delete_button = QLabel('Delete')
        # self.delete_button.setPixmap(QPixmap('Icons/recycle-bin.png'))
        self.delete_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_button.setMaximumSize(self.button_size[0] + 5, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setLayout(self.table_layout)


class Table(QGroupBox):
    colors = ['#ffccff', '#ffe6ff']

    def __init__(self, id_, number, class_, teacher, male, female, total_, subjects, class_in, teacher_in, subjects_in):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.number = number
        self.class_ = class_
        self.teacher = teacher
        self.male = male
        self.female = female
        self.total_ = total_
        self.subjects = subjects

        self.class_in = class_in
        self.teacher_in = teacher_in
        self.subjects_in = subjects_in

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
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 50
        self.name_width = 90
        self.name_height = 50
        self.number_width = 35
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

        self.teacher_label = QLabel(self.teacher)
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(self.name_width, self.name_height)
        self.teacher_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.teacher_label)

        self.class_label = QLabel(self.class_)
        self.class_label.setAlignment(Qt.AlignLeft)
        self.class_label.setMaximumSize(self.name_width + 30, self.name_height)
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.class_label)

        self.male_label = QLabel(self.male)
        self.male_label.setAlignment(Qt.AlignLeft)
        self.male_label.setMaximumSize(self.number_width, self.name_height)
        self.male_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.male_label)
        
        self.female_label = QLabel(self.female)
        self.female_label.setAlignment(Qt.AlignLeft)
        self.female_label.setMaximumSize(self.number_width, self.name_height)
        self.female_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.female_label)

        self.total = QLabel(self.total_)
        self.total.setAlignment(Qt.AlignLeft)
        self.total.setMaximumSize(self.number_width, self.serial_num_height)
        self.total.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.total)

        self.subjects_label = QLabel(self.subjects)
        self.subjects_label.setAlignment(Qt.AlignLeft)
        self.subjects_label.setMaximumSize(self.number_width, self.name_height)
        self.subjects_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subjects_label)

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
        try:
            pass
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def view_slot(self):
        try:
            pass
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def onCountChanged(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            all_subjects = DataBase.get_class_subject(self.class_)
            # i_box = 0
            if all_subjects:
                for i in range(0, len(all_subjects)):
                    self.subjects_in[i].setText(all_subjects[i])
                    # i_box += 1
        except Exception as e:
            raise e

    def edit_slot(self):
        try:
            from Projects.SchoolManagement.PanelGadgets import Exam
            from Projects.SchoolManagement.DataBaseTool import DataBase
            
            self.username = DataBase.get_school_class_teacher_by_id(str(self.id_))
            if len(self.username) != 0 and len(self.class_) != 0:
                self.class_in.setText(self.username)
                self.teacher_in.setText(self.class_)

            self.signal_slot = Exam.GetQuestions(30)
            self.signal_slot.countChanged.connect(self.onCountChanged)
            self.signal_slot.run()
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            DataBase.delete_class(self.class_)
            DataBase.delete_school_class(self.id_)

            self.setHidden(True)
            self.setEnabled(False)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)


class Class(QWidget):
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
            from Projects.SchoolManagement.PanelGadgets.Teachers import Teachers as Page

            self.main_group.setHidden(True)
            self.main_group.setEnabled(False)

            page = Page(self.school_name, self.first_in, self.last_in)
            self.window_layout.addWidget(page)
        except Exception as e:
            raise e

    def parents(self):
        self.parents_button = QPushButton('Parents')
        self.parents_button.setIcon(QIcon('Icons/image-150nw-422738920.jpg'))
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
        self.library_button.setIcon(QIcon('Icons/034-library.png'))
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
            msg = 'You\'re already on the Class page.'
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e

    def subjects(self):
        self.subjects_button = QPushButton('Subjects')
        self.subjects_button.setIcon(QIcon('Icons/book.png'))
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
        self.class_routine_button.setIcon(QIcon('Icons/040-timetable.png'))
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
        self.attendance_button.setIcon(QIcon('Icons/2123.png'))
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

        self.classPAGE()

    def classPAGE(self):
        self.scroll_width = 1150
        self.scroll_height = 850

        self.class_layout = QHBoxLayout()
        self.class_layout.setContentsMargins(0, 0, 0, 0)
        self.class_layout.setSpacing(0)

        self.class_group = QGroupBox('Class')
        self.class_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.class_group.setContentsMargins(0, 0, 0, 0)
        self.class_group.setLayout(self.class_layout)

        self.class_scroll = QScrollArea()
        self.class_scroll.setMaximumSize(self.scroll_width, self.scroll_height)
        self.class_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.class_scroll.setWidgetResizable(True)
        self.class_scroll.setWidget(self.class_group)

        self.right_board_layout.addWidget(self.class_scroll)

        self.classFORM()
        self.classTABLE()
        self.classREGISTRATION()

    def classFORM(self):
        self.reg_classname = QLineEdit()
        self.reg_f_name = QLineEdit()
        self.reg_l_name = QLineEdit()
        self.reg_new_pass = QLineEdit()
        self.reg_gender = QComboBox()
        self.reg_confirm_pass = QLineEdit()
        self.reg_username = QLineEdit()
        self.admin_username = QLineEdit()
        self.admin_pass = QLineEdit()

    def classTABLE(self):
        self.table_layout = QVBoxLayout()
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(0)
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.table_group = QGroupBox()
        self.table_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 0px;
                }
            '''
        )
        self.table_group.setLayout(self.table_layout)

        self.table_scroll = QScrollArea()
        self.table_scroll.setWidgetResizable(True)
        self.table_scroll.setMaximumSize(550, 700)
        self.table_scroll.setWidget(self.table_group)
        self.table_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )

        self.class_layout.addWidget(self.table_scroll)
        
        self.index_table_i = 1
        self.table_layout.addWidget(TableDef())

    def classREGISTRATION(self):
        self.reg_layout = QVBoxLayout()
        self.reg_layout.setAlignment(Qt.AlignTop)

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

        self.title = f'{self.school_name} : Class Registration Form'

        self.form_title = QLabel(self.title)
        self.form_title.setAlignment(Qt.AlignLeft)
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

        self.second_layout = QHBoxLayout()
        self.second_layout.setAlignment(Qt.AlignCenter)
        self.second_layout.setContentsMargins(0, 0, 0, 0)

        self.reg_layout.addLayout(self.second_layout)

        self.reg_classname.setPlaceholderText('Class name')
        self.reg_classname.setStyleSheet(
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
        self.reg_classname.setMaximumSize(self.name_size[0], self.name_size[1])
        self.second_layout.addWidget(self.reg_classname)

        self.third_layout = QHBoxLayout()
        self.third_layout.setAlignment(Qt.AlignCenter)
        # self.third_layout.setSpacing(0)
        self.third_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.third_layout)

        self.admin_layout = QHBoxLayout()
        self.admin_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.admin_layout)

        self.admin_username.setPlaceholderText('Teacher\'s Username')
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

        self.admin_pass.setPlaceholderText('Teacher\'s password')
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

        self.subjects_layout = QVBoxLayout()
        self.subjects_layout.setAlignment(Qt.AlignCenter)
        self.subjects_layout.setSpacing(10)

        self.max_column = 3
        self.current_row = 0

        self.subjects_grid = QGridLayout()
        self.subjects_grid.setSpacing(20)
        self.subjects_grid.setAlignment(Qt.AlignCenter)
        self.subjects_layout.addLayout(self.subjects_grid)

        self.subject_1 = QLineEdit()
        self.subject_1.setMaximumSize(200, 30)
        self.subject_1.setPlaceholderText(f'subject {1}')
        self.subject_1.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_1, 0, 0)

        self.subject_2 = QLineEdit()
        self.subject_2.setMaximumSize(200, 30)
        self.subject_2.setPlaceholderText(f'subject {2}')
        self.subject_2.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_2, 0, 1)        

        self.subject_3 = QLineEdit()
        self.subject_3.setMaximumSize(200, 30)
        self.subject_3.setPlaceholderText(f'subject {3}')
        self.subject_3.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_3, 0, 2)

        self.subject_4 = QLineEdit()
        self.subject_4.setMaximumSize(200, 30)
        self.subject_4.setPlaceholderText(f'subject {4}')
        self.subject_4.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_4, 1, 0)

        self.subject_5 = QLineEdit()
        self.subject_5.setMaximumSize(200, 30)
        self.subject_5.setPlaceholderText(f'subject {5}')
        self.subject_5.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_5, 1, 1)
        
        self.subject_6 = QLineEdit()
        self.subject_6.setMaximumSize(200, 30)
        self.subject_6.setPlaceholderText(f'subject {6}')
        self.subject_6.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_6, 1, 2)

        self.subject_7 = QLineEdit()
        self.subject_7.setMaximumSize(200, 30)
        self.subject_7.setPlaceholderText(f'subject {7}')
        self.subject_7.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_7, 2, 0)

        self.subject_8 = QLineEdit()
        self.subject_8.setMaximumSize(200, 30)
        self.subject_8.setPlaceholderText(f'subject {8}')
        self.subject_8.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_8, 2, 1)        

        self.subject_9 = QLineEdit()
        self.subject_9.setMaximumSize(200, 30)
        self.subject_9.setPlaceholderText(f'subject {9}')
        self.subject_9.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_9, 2, 2)

        self.subject_10 = QLineEdit()
        self.subject_10.setMaximumSize(200, 30)
        self.subject_10.setPlaceholderText(f'subject {10}')
        self.subject_10.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_10, 3, 0)

        self.subject_11 = QLineEdit()
        self.subject_11.setMaximumSize(200, 30)
        self.subject_11.setPlaceholderText(f'subject {11}')
        self.subject_11.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_11, 3, 1)
        
        self.subject_12 = QLineEdit()
        self.subject_12.setMaximumSize(200, 30)
        self.subject_12.setPlaceholderText(f'subject {12}')
        self.subject_12.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_12, 3, 2)

        self.subject_13 = QLineEdit()
        self.subject_13.setMaximumSize(200, 30)
        self.subject_13.setPlaceholderText(f'subject {13}')
        self.subject_13.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_13, 4, 0)

        self.subject_14 = QLineEdit()
        self.subject_14.setMaximumSize(200, 30)
        self.subject_14.setPlaceholderText(f'subject {14}')
        self.subject_14.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_14, 4, 1)
        
        self.subject_15 = QLineEdit()
        self.subject_15.setMaximumSize(200, 30)
        self.subject_15.setPlaceholderText(f'subject {15}')
        self.subject_15.setStyleSheet(
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
        self.subjects_grid.addWidget(self.subject_15, 4, 2)

        self.subjects_box = QGroupBox('Subjects')
        self.subjects_box.setLayout(self.subjects_layout)
        self.subjects_box.setStyleSheet(
            '''
            QGroupBox {
                border: 1px solid black;
                padding: 10px;
                }
            '''
        )

        self.subjects_scroll = QScrollArea()
        self.subjects_scroll.setMinimumSize(250, 400)
        self.subjects_scroll.setWidget(self.subjects_box)
        self.subjects_scroll.setWidgetResizable(True)
        self.subjects_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.reg_layout.addWidget(self.subjects_scroll)

        self.last_layout = QHBoxLayout()
        self.last_layout.setAlignment(Qt.AlignCenter)
        self.last_layout.setContentsMargins(0, 0, 0, 0)
        self.reg_layout.addLayout(self.last_layout)

        self.reg_button_size = (150, 30)

        self.reg_update_button = QPushButton('Register')
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

        self.class_layout.addWidget(self.reg_scroll)

        self.count = 1
        self.all_subjects = []

        self.run()

    def total_subjects(self):
        return 'NULL'

    def run(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            males = 0
            females = 0
            classes = DataBase.get_school_class_all()
            if len(classes) != 0:
                for class_ in classes:
                    class_name = class_[1]
                    subjects = DataBase.get_class_sub(class_name)
                    teacher_username = DataBase.get_teacher_username(class_[4])
                    self.table_layout.addWidget(Table(
                        class_[0], 
                        self.index_table_i,
                        class_name,
                        f'{teacher_username[0]} {teacher_username[1][0].capitalize()}.',
                        str(males),
                        str(females),
                        str(males + females),
                        str(len(subjects)),
                        self.admin_username,
                        self.reg_classname,
                        (
                            self.subject_1,
                            self.subject_2,
                            self.subject_3,
                            self.subject_4,
                            self.subject_5,
                            self.subject_6,
                            self.subject_7,
                            self.subject_8,
                            self.subject_9,
                            self.subject_10,
                            self.subject_11,
                            self.subject_12,
                            self.subject_13,
                            self.subject_14,
                            self.subject_15
                        )
                        )
                    )
                    self.index_table_i += 1
            else:
                msg = "No classes yet."
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)    
        except Exception as e:
            # msg = str(e)
            # message_box = QMessageBox()
            # message_box.about(self, self.school_name, msg)
            raise e

    def clear_form_field(self):
        self.admin_username.setText('')
        self.admin_pass.setText('')
        self.reg_classname.setText('')
        self.subject_1.setText('')
        self.subject_2.setText('')
        self.subject_3,setText('')
        self.subject_4.setText('')
        self.subject_5.setText('')
        self.subject_6.setText('')
        self.subject_7.setText('')
        self.subject_8.setText('')
        self.subject_9.setText('')
        self.subject_10.setText('')
        self.subject_11.setText('')
        self.subject_12.setText('')
        self.subject_13.setText('')
        self.subject_14.setText('')
        self.subject_15.setText('')

    def reg_update_slot(self):
        try:
            if len(self.admin_username.text()) != 0:
                if len(self.admin_pass.text()) != 0:
                    from Projects.SchoolManagement.DataBaseTool.DataBase import get_teacher, get_teacher_all
                    from Projects.SchoolManagement.DataBaseTool.DataBase import create_school_class, insert_school_class, get_school_class
                    from Projects.SchoolManagement.DataBaseTool.DataBase import create_class, insert_class, get_class, get_class_ids
                    from Projects.SchoolManagement.DataBaseTool import DataBase
                    teachers = get_teacher('username')
                    if self.admin_username.text() in teachers:
                        user_password = get_teacher('password')
                        if self.admin_pass.text() == user_password[teachers.index(self.admin_username.text())]:
                            self.teacher = get_teacher('surname')[teachers.index(self.admin_username.text())]
                            create_school_class()
                            id_ = get_class_ids()
                            class_names = get_school_class()

                            if self.reg_classname.text() in class_names:
                                self.update_class_id = DataBase.get_class_id(self.reg_classname.text())

                                insert_class(int(self.update_class_id), self.reg_classname.text(), self.admin_username.text(), self.admin_username.text(), self.subject_1.text(), self.subject_2.text(), self.subject_3.text(), self.subject_4.text(), self.subject_5.text(), self.subject_6.text(), self.subject_7.text(), self.subject_8.text(), self.subject_9.text(), self.subject_10.text(), self.subject_11.text(), self.subject_12.text(), self.subject_13.text(), self.subject_14.text(), self.subject_15.text())
                                insert_school_class(int(self.update_class_id), self.reg_classname.text(), self.total_subjects(), self.teacher, self.admin_username.text())
                                msg = 'Class name already exist. Can\'t add another class with an existing name\nSo i will update the class information instead.'
                                message_box = QMessageBox()
                                message_box.about(self, 'School Manager', msg)
                            else:
                                if len(id_) == 0:
                                    id_ = 0

                                    create_class(self.reg_classname.text())
                                    insert_class(int(id_), self.reg_classname.text(), self.admin_username.text(), self.admin_username.text(), self.subject_1.text(), self.subject_2.text(), self.subject_3.text(), self.subject_4.text(), self.subject_5.text(), self.subject_6.text(), self.subject_7.text(), self.subject_8.text(), self.subject_9.text(), self.subject_10.text(), self.subject_11.text(), self.subject_12.text(), self.subject_13.text(), self.subject_14.text(), self.subject_15.text())
                                    insert_school_class(int(id_), self.reg_classname.text(), self.total_subjects(), self.teacher, self.admin_username.text())
                                    
                                    msg = f'{self.reg_classname.text()} has been successfully registered.\nNB: Class name can not be changed.'
                                    message_box = QMessageBox()
                                    message_box.about(self, 'School Manager', msg)

                                    self.clear_form_field()
                                else:
                                    create_class(self.reg_classname.text())
                                    insert_class(int(id_[-1] + 1), self.reg_classname.text(), self.admin_username.text(), self.admin_username.text(), self.subject_1.text(), self.subject_2.text(), self.subject_3.text(), self.subject_4.text(), self.subject_5.text(), self.subject_6.text(), self.subject_7.text(), self.subject_8.text(), self.subject_9.text(), self.subject_10.text(), self.subject_11.text(), self.subject_12.text(), self.subject_13.text(), self.subject_14.text(), self.subject_15.text())
                                    insert_school_class(int(id_[-1] + 1), self.reg_classname.text(), self.total_subjects(), self.teacher, self.admin_username.text())
                                    
                                    msg = f'{self.reg_classname.text()} has been successfully registered.\nNB: Class name can not be changed.'
                                    message_box = QMessageBox()
                                    message_box.about(self, 'School Manager', msg)

                                    self.clear_form_field()
                        else:
                            msg = 'Incorrect password.'
                            message_box = QMessageBox()
                            message_box.about(self, 'School Manager', msg)
                    else:
                        msg = 'Username does not exist.'
                        message_box = QMessageBox()
                        message_box.about(self, 'School Manager', msg)    
                else:
                    msg = 'Please provide your password.'
                    message_box = QMessageBox()
                    message_box.about(self, 'School Manager', msg)
            else:
                msg = 'Enter a valid username.'
                message_box = QMessageBox()
                message_box.about(self, 'School Manager', msg)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)
            # raise e


clock = time.gmtime()


class AddUpdate(QThread):

    countChanged = pyqtSignal(int)
    count = 0

    begin = clock.tm_sec

    def __init__(self, subject):
        QThread.__init__(self)

        self.subject = subject
        self.time_limit = time_limit

    def run(self):
        count = self.count
        while count < self.time_limit:
            count += 1
            time.sleep(1)
            self.countChanged.emit(count)
            try:
                from Projects.SchoolManagement.DataBaseTool import create_class, insert_subject
            except Exception as e:
                msg = str(e)
                message_box = QMessageBox()
                message_box.about(self, 'School Manager', msg)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     manager = Class()
#     manager.show()
#     sys.exit(app.exec_())

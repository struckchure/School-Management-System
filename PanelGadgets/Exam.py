from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import datetime


class DistributeStudents(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, duration=100):
        QThread.__init__(self)
        self.duration = duration

    def run(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            all_students = DataBase.get_school_students()
            all_students_copy = all_students
            while self.duration > 0:
                self.countChanged.emit(self.duration)
                self.duration -= 1
        except Exception as e:
            raise e


class GetQuestions(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, duration):
        QThread.__init__(self)
        self.duration = duration

    def run(self):
        try:
            while self.duration > 0:
                self.countChanged.emit(self.duration)
                self.duration -= self.duration
        except Exception as e:
            raise e


class CheckTableDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
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
        self.button_size = (60, 30)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel('s/n')
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.subject_label = QLabel("Subject")
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.teacher_label = QLabel("Teacher")
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(
            self.name_width - 35, self.name_height)
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

        self.allocated_time = QLabel("AT")
        self.allocated_time.setAlignment(Qt.AlignLeft)
        self.allocated_time.setMaximumSize(self.number_width, self.name_height)
        self.allocated_time.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.allocated_time)

        self.upload_time = QLabel('ST')
        self.upload_time.setAlignment(Qt.AlignLeft)
        self.upload_time.setMaximumSize(
            self.number_width + 110, self.name_height)
        self.upload_time.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.upload_time)

        self.enable_label = QLabel('Enable')
        self.enable_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.enable_label.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.enable_label)

        self.disable_label = QLabel('Disable')
        self.disable_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.disable_label.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.disable_label)

        self.delete_label = QLabel('Delete')
        self.delete_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_label.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.delete_label)

        self.setLayout(self.table_layout)


class CheckTable(QGroupBox):
    def __init__(self, id_, number, class_, subject, teacher, schedule_time, allocated_time):
        QGroupBox.__init__(self)

        self.id_ = str(id_)
        self.number = str(number)
        self.class_ = class_
        self.subject = subject
        self.teacher = teacher
        self.schedule_time = schedule_time
        self.allocated_time = allocated_time

        self.setStyleSheet(
            '''
            QGroupBox {
                border-bottom: 1px solid #ffccff;
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
        self.button_size = (60, 30)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.id_ = id_
        self.number = number
        self.class_ = class_
        self.subject = subject
        self.teacher = teacher
        self.schedule_time = schedule_time
        self.allocated_time = allocated_time

        self.serial_num = QLabel(str(self.number))
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.subject_label = QLabel(self.subject)
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.teacher_label = QLabel(self.teacher)
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(
            self.name_width - 25, self.name_height)
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
        self.class_label.setMaximumSize(self.name_width + 35, self.name_height)
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.class_label)

        self.allocated_time = QLabel(self.allocated_time)
        self.allocated_time.setAlignment(Qt.AlignLeft)
        self.allocated_time.setMaximumSize(self.number_width, self.name_height)
        self.allocated_time.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.allocated_time)

        self.upload_time = QLabel(self.schedule_time)
        self.upload_time.setAlignment(Qt.AlignLeft)
        self.upload_time.setMaximumSize(
            self.number_width + 110, self.name_height)
        self.upload_time.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.upload_time)

        self.enable_label = QPushButton('Enable')
        self.enable_label.clicked.connect(self.enable_slot)
        self.enable_label.setStyleSheet(
            '''
            QPushButton {
                font-weight: bold;
                font-size: 13px;
                color: white;
                border-radius: 3px;
                background-color: rgb(80, 200, 80);
            }
            .QPushButton:hover {
                background-color: rgb(80, 230, 80);
            }
            '''
        )
        self.enable_label.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.enable_label)

        self.disable_label = QPushButton('Disable')
        self.disable_label.clicked.connect(self.disable_slot)
        self.disable_label.setStyleSheet(
            '''
            QPushButton {
                font-weight: bold;
                font-size: 13px;
                color: white;
                border-radius: 3px;
                background-color: rgb(200, 80, 80);
            }
            .QPushButton:hover {
                background-color: rgb(230, 80, 80);
            }
            '''
        )
        self.disable_label.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.disable_label)

        self.delete_label = QPushButton('Delete')
        self.delete_label.clicked.connect(self.delete_slot)
        self.delete_label.setStyleSheet(
            '''
            QPushButton {
                font-weight: bold;
                font-size: 13px;
                color: white;
                border-radius: 3px;
                background-color: rgb(150, 30, 80);
            }
            .QPushButton:hover {
                background-color: rgb(130, 30, 80);
            }
            '''
        )
        self.delete_label.setMaximumSize(
            self.button_size[0] - 10,  self.button_size[1])
        self.table_layout.addWidget(self.delete_label)

        self.setLayout(self.table_layout)

    def enable_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            DataBase.change_exam_status(self.class_, self.subject, 'True')

            msg = f'{self.subject} Exam for {self.class_} has been successfully enabled.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)
        except Exception as e:
            raise e

    def disable_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            DataBase.change_exam_status(self.class_, self.subject, 'False')

            msg = f'{self.subject} Exam for {self.class_} has been successfully disabled.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            DataBase.delete_exam_traces(self.class_, self.subject, self.id_)

            msg = f'{self.subject} Exam for {self.class_} has been successfully deleted.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

            self.setHidden(True)
            self.setEnabled(False)
        except Exception as e:
            raise e


class ResultTableDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 50
        self.name_width = 90
        self.name_height = 50
        self.number_width = 35
        self.button_size = (60, 30)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel('s/n')
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.class_label = QLabel('Class')
        self.class_label.setAlignment(Qt.AlignLeft)
        self.class_label.setMaximumSize(self.name_width + 35, self.name_height)
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.class_label)

        self.subject_label = QLabel('Subject')
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.teacher_label = QLabel('Teacher')
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(
            self.name_width - 25, self.name_height)
        self.teacher_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.teacher_label)

        self.view_button = QLabel('View')
        self.view_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.view_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.delete_button = QLabel('Delete')
        self.delete_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid #ffccff;
                border-left: 1px solid #ffccff;
                border-right: 1px solid #ffccff;
                border-bottom: 0px;
                padding-bottom: 5px;
            }
            '''
        )

        self.setMaximumSize(700, 40)
        self.setLayout(self.table_layout)


class ResultGrid(QGroupBox):
    def __init__(self, name):
        QGroupBox.__init__(self)

        self.name = name

        self.box_layout = QVBoxLayout()
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.box_layout.setSpacing(0)
        self.box_layout.setAlignment(Qt.AlignTop)

        self.box_layout.addWidget(StudentResultTableDef())

        self.setObjectName(f'grid_{self.name}')
        self.setLayout(self.box_layout)


class ResultTable(QGroupBox):
    def __init__(self, id_, number, class_, subject, teacher, stud_layout):
        QGroupBox.__init__(self)

        self.id_ = str(id_)
        self.number = str(number)
        self.class_ = class_
        self.subject = subject
        self.teacher = teacher
        self.stud_layout = stud_layout

        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 40
        self.name_width = 90
        self.name_height = 40
        self.number_width = 35
        self.button_size = (60, 30)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.id_ = id_
        self.number = number
        self.class_ = class_
        self.subject = subject
        self.teacher = teacher

        self.serial_num = QLabel(str(self.number))
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.class_label = QLabel(self.class_)
        self.class_label.setAlignment(Qt.AlignLeft)
        self.class_label.setMaximumSize(self.name_width + 35, self.name_height)
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.class_label)

        self.subject_label = QLabel(self.subject)
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.teacher_label = QLabel(self.teacher)
        self.teacher_label.setAlignment(Qt.AlignLeft)
        self.teacher_label.setMaximumSize(
            self.name_width - 25, self.name_height)
        self.teacher_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.teacher_label)

        self.view_button = QPushButton()
        self.view_button.clicked.connect(self.view_slot)
        self.view_button.setIcon(QIcon('Icons/view.png'))
        self.view_button.setStyleSheet(
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
        self.view_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.delete_button = QPushButton()
        self.delete_button.clicked.connect(self.delete_slot)
        self.delete_button.setIcon(QIcon('Icons/recycle-bin.png'))
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
        self.delete_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid #ffccff;
                border-left: 1px solid #ffccff;
                border-right: 1px solid #ffccff;
                border-bottom: 0px;
                padding-bottom: 5px;
            }
            '''
        )

        self.setMaximumSize(700, 40)
        self.setLayout(self.table_layout)

    def view_slot(self):
        try:
            self.stud_number = 1

            self.submitSEQ = GetQuestions(self.number)
            self.submitSEQ.countChanged.connect(self.view_signal)
            self.submitSEQ.run()
        except Exception as e:
            raise e

    def view_signal(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            name = f'{self.class_}_{self.subject}_{int(self.stud_layout[1].index(self.stud_layout[1][-1]) + 1)}'

            self.other = ResultGrid(name)

            self.stud_layout[0].addWidget(self.other, 0, 0)
            self.all_students_results = DataBase.get_student_exam_status_all(
                self.class_, self.subject)

            if len(self.all_students_results) != 0:
                for result in self.all_students_results:
                    self.other.box_layout.addWidget(StudentResultTable(
                        result[0],
                        self.stud_number,
                        result[1],
                        result[2],
                        result[3],
                        result[4]
                    )
                    )
                    self.stud_number += 1
            else:
                msg = f'No results for {self.class_} {self.subject} yet.'
                message_box = QMessageBox()
                message_box.about(self, 'Exam Manager', msg)
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            class_ = self.class_
            subject = self.subject

            if ' ' in subject:
                subject = subject.replace(' ', '_')
                table_name = f'{class_}_{subject}'
                table_name1 = f'{class_}_{subject}_Result'
            else:
                subject = subject.replace(' ', '_')
                table_name = f'{class_}_{subject}'
                table_name1 = f'{class_}_{subject}_Result'

            DataBase.drop_table(table_name)

            msg = f'{subject} Results for {class_} has been successfully deleted.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)
        except Exception as e:
            raise e


class StudentResultTableDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid #ffccff;
                border-left: 1px solid #ffccff;
                border-right: 1px solid #ffccff;
                border-bottom: 0px;
                padding-bottom: 5px;
            }
            '''
        )

        self.setMaximumHeight(40)

        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 40
        self.name_width = 90
        self.name_height = 40
        self.number_width = 35
        self.button_size = (60, 40)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.serial_num = QLabel('s/n')
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.reg_num_label = QLabel('Reg Number')
        self.reg_num_label.setAlignment(Qt.AlignLeft)
        self.reg_num_label.setMaximumSize(
            self.name_width + 15, self.name_height)
        self.reg_num_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.reg_num_label)

        self.subject_label = QLabel('Subject')
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.score_label = QLabel('Score')
        self.score_label.setAlignment(Qt.AlignLeft)
        self.score_label.setMaximumSize(self.name_width - 25, self.name_height)
        self.score_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.score_label)

        self.status_label = QLabel('Status')
        self.status_label.setAlignment(Qt.AlignLeft)
        self.status_label.setMaximumSize(
            self.name_width - 25, self.name_height)
        self.status_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.status_label)

        self.view_button = QLabel('View')
        self.view_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.view_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.delete_button = QLabel('Delete')
        self.delete_button.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.delete_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        self.setMaximumWidth(700)
        self.setLayout(self.table_layout)


class StudentResult(QDialog):
    def __init__(self, surname='', first_name='', last_name='', class_='', subject='', reg_num='', score='', status='', teacher=''):
        QDialog.__init__(self)

        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name
        self.class_ = class_
        self.subject = subject
        self.reg_num = reg_num
        self.score = score
        self.status = status
        self.teacher = teacher

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.setSpacing(5)
        self.dialog_layout.setAlignment(Qt.AlignCenter)

        self.initialization()

        self.setLayout(self.dialog_layout)
        self.setStyleSheet(
            '''
            QDialog {
                padding: 10px;
            }
            '''
        )
        self.setWindowTitle(f'{self.surname} {self.first_name} {self.last_name}')
        self.show()

    def initialization(self):
        self.topNAV()
        self.resultFORM()
        self.bottomLAYER()

    def topNAV(self):
        self.top_nav = QHBoxLayout()
        self.top_nav.setContentsMargins(0, 0, 0, 0)
        self.top_nav.setSpacing(0)
        self.top_nav.setAlignment(Qt.AlignTop)

        self.top_group = QGroupBox('Result')
        self.top_group.setLayout(self.top_nav)
        self.top_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 3px;
            }
            '''
        )

        self.dialog_layout.addWidget(self.top_group)

    def resultFORM(self):
        self.form_layout = QGridLayout()
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(6)
        self.form_layout.setAlignment(Qt.AlignTop)

        self.form_group = QGroupBox()
        self.form_group.setLayout(self.form_layout)
        self.form_group.setStyleSheet(
            '''
            QGroupBox {
                background-color: white;
                border: 1px solid black;
                padding: 5px;
            }
            '''
        )
        self.dialog_layout.addWidget(self.form_group)

        self.data_size = (350, 50)

        self.surname_box_label = QLabel('Surname')
        self.surname_box_label.setAlignment(Qt.AlignLeft)
        self.surname_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.surname_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.surname_box_label, 0, 0)

        self.first_name_box_label = QLabel('First Name')
        self.first_name_box_label.setAlignment(Qt.AlignLeft)
        self.first_name_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.first_name_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.first_name_box_label, 1, 0)

        self.last_name_box_label = QLabel('Last Name')
        self.last_name_box_label.setAlignment(Qt.AlignLeft)
        self.last_name_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.last_name_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.last_name_box_label, 2, 0)

        self.class_box_label = QLabel('Class')
        self.class_box_label.setAlignment(Qt.AlignLeft)
        self.class_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.class_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.class_box_label, 3, 0)

        self.subject_box_label = QLabel('Subject')
        self.subject_box_label.setAlignment(Qt.AlignLeft)
        self.subject_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.subject_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.subject_box_label, 4, 0)

        self.reg_num_box_label = QLabel('Registration Number')
        self.reg_num_box_label.setAlignment(Qt.AlignLeft)
        self.reg_num_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.reg_num_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.reg_num_box_label, 5, 0)

        self.score_box_label = QLabel('Score')
        self.score_box_label.setAlignment(Qt.AlignLeft)
        self.score_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.score_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.score_box_label, 6, 0)

        self.status_box_label = QLabel('Status')
        self.status_box_label.setAlignment(Qt.AlignLeft)
        self.status_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.status_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.status_box_label, 7, 0)

        self.teacher_box_label = QLabel('Teacher')
        self.teacher_box_label.setAlignment(Qt.AlignLeft)
        self.teacher_box_label.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.teacher_box_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.form_layout.addWidget(self.teacher_box_label, 8, 0)

        # Student data

        self.surname_box = QLabel(self.surname)
        self.surname_box.setAlignment(Qt.AlignLeft)
        self.surname_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.surname_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )
        self.form_layout.addWidget(self.surname_box, 0, 1)

        self.first_name_box = QLabel(self.first_name)
        self.first_name_box.setAlignment(Qt.AlignLeft)
        self.first_name_box.setMaximumSize(
            self.data_size[0], self.data_size[1])
        self.first_name_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )
        self.form_layout.addWidget(self.first_name_box, 1, 1)

        self.last_name_box = QLabel(self.last_name)
        self.last_name_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.last_name_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )
        self.form_layout.addWidget(self.last_name_box, 2, 1)

        self.class_box = QLabel(self.class_)
        self.class_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.class_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.class_box, 3, 1)

        self.subject_box = QLabel(self.subject)
        self.subject_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.subject_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.subject_box, 4, 1)

        self.reg_num_box = QLabel(self.reg_num)
        self.reg_num_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.reg_num_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.reg_num_box, 5, 1)

        self.score_box = QLabel(self.score)
        self.score_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.score_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.score_box, 6, 1)

        self.status_box = QLabel(self.status)
        self.status_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.status_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.status_box, 7, 1)

        self.teacher_box = QLabel(self.teacher)
        self.teacher_box.setMaximumSize(self.data_size[0], self.data_size[1])
        self.teacher_box.setStyleSheet(
            '''
            QLabel {
                font-size: 13px;
                font: Verdana;
            }
            '''
        )

        self.form_layout.addWidget(self.teacher_box, 8, 1)

    def bottomLAYER(self):
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(4)
        self.bottom_layout.setAlignment(Qt.AlignCenter)

        self.review_printer = QPushButton('Preview')
        self.review_printer.setMaximumSize(300, 40)
        self.review_printer.clicked.connect(self.review_printer_slot)
        self.bottom_layout.addWidget(self.review_printer)

        self.printer = QPushButton('Print Report')
        self.printer.setMaximumSize(300, 40)
        self.printer.clicked.connect(self.printer_slot)
        self.bottom_layout.addWidget(self.printer)

        self.bottom_group = QGroupBox()
        self.bottom_group.setLayout(self.bottom_layout)
        self.bottom_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
            }
            '''
        )

        self.dialog_layout.addWidget(self.bottom_group)

    def review_printer_slot(self):
        pass

    def printer_slot(self):
        pass


class StudentResultTable(QGroupBox):
    def __init__(self, id_, number, reg_num, subject, score, status):
        QGroupBox.__init__(self)

        self.id_ = str(id_)
        self.number = number
        self.reg_num = reg_num
        self.subject = subject
        self.score = score
        self.status = status

        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid #ffccff;
                border-left: 1px solid #ffccff;
                border-right: 1px solid #ffccff;
                border-bottom: 0px;
                padding-bottom: 5px;
            }
            '''
        )

        self.setMaximumHeight(40)

        self.table_layout = QHBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)
        self.table_layout.setSpacing(7)

        self.serial_num_width = 30
        self.serial_num_height = 40
        self.name_width = 90
        self.name_height = 40
        self.number_width = 35
        self.button_size = (60, 40)

        self.total_width = self.serial_num_width + \
            (self.name_width * 3) + self.serial_num_width + 10

        # Table headings

        self.id_ = id_
        self.reg_num = reg_num
        self.subject = subject
        self.score = score
        self.status = status

        self.serial_num = QLabel(str(self.number))
        self.serial_num.setAlignment(Qt.AlignCenter)
        self.serial_num.setMaximumSize(
            self.serial_num_width, self.serial_num_height)
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

        self.reg_num_label = QLabel(self.reg_num)
        self.reg_num_label.setAlignment(Qt.AlignLeft)
        self.reg_num_label.setMaximumSize(
            self.name_width + 15, self.name_height)
        self.reg_num_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.reg_num_label)

        self.subject_label = QLabel(self.subject.replace('_', ' '))
        self.subject_label.setAlignment(Qt.AlignLeft)
        self.subject_label.setMaximumSize(
            self.name_width + 50, self.name_height)
        self.subject_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject_label)

        self.score_label = QLabel(self.score)
        self.score_label.setAlignment(Qt.AlignLeft)
        self.score_label.setMaximumSize(self.name_width - 25, self.name_height)
        self.score_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.score_label)

        self.status_label = QLabel(self.status)
        self.status_label.setAlignment(Qt.AlignLeft)
        self.status_label.setMaximumSize(
            self.name_width - 25, self.name_height)
        self.status_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
            }
            '''
        )
        self.table_layout.addWidget(self.status_label)

        self.view_button = QPushButton()
        self.view_button.clicked.connect(self.view_slot)
        self.view_button.setIcon(QIcon('Icons/view.png'))
        self.view_button.setStyleSheet(
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
        self.view_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.view_button)

        self.delete_button = QPushButton()
        self.delete_button.clicked.connect(self.delete_slot)
        self.delete_button.setIcon(QIcon('Icons/recycle-bin.png'))
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
        self.delete_button.setMaximumSize(
            self.button_size[0] - 10, self.button_size[1])
        self.table_layout.addWidget(self.delete_button)

        w = (self.serial_num_width) + (self.name_width + 35) + (self.name_width +
                                                                50) + (self.name_width - 25) + ((self.button_size[0] - 10) * 2)

        self.setMaximumWidth(700)
        self.setLayout(self.table_layout)

    def view_slot(self):
        try:
            self.subject = self.subject.replace('_', ' ')
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.reg_num_index = DataBase.get_students_by_column(
                'reg_num').index(self.reg_num)
            self.class_ = DataBase.get_students_by_column('class')[
                self.reg_num_index]
            self.id_ = DataBase.get_students_by_column('id')[
                self.reg_num_index]

            self.teacher = DataBase.get_school_questions_by_cs(
                self.class_, self.subject)
            if self.teacher:
                self.teacher = DataBase.get_school_questions_by_cs(
                    self.class_, self.subject)[0][3]
                self.teacher_index = DataBase.get_teacher_names().index(self.teacher)
                self.teacher = f'{DataBase.get_teacher_all()[self.teacher_index][1]} {DataBase.get_teacher_all()[self.teacher_index][2]} {DataBase.get_teacher_all()[self.teacher_index][3]}'
                self.student_info = DataBase.get_school_students_by_id(
                    self.id_)

                self.student_result = StudentResult(
                    self.student_info[1],
                    self.student_info[2],
                    self.student_info[3],
                    self.student_info[4],
                    self.subject,
                    self.reg_num,
                    self.score,
                    self.status,
                    self.teacher
                )
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            msg = f'{self.subject} Results for {self.class_} has been successfully deleted.'
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)
        except Exception as e:
            raise e


class Question(QGroupBox):
    def __init__(self,  number,  question_layout):
        QGroupBox.__init__(self)
        self.question_name = number

        self.setObjectName(f'question_box_{number}')
        self.question_layout = question_layout

        width, height = 900, 1000

        # self.setLayout(self.question_layout)
        self.setMaximumSize(width, height)
        self.setStyleSheet(
            '''
            QGroupBox {
                background-color: white;
                padding:5px;
                }
            '''
        )

        self.initialization()

    def initialization(self):
        self.question_size = (400, 100)
        self.option_size = (220, 40)

        # question_name = question_1_a
        question_name = f'question_{self.question_name}'

        self.question_number = QLabel(f'Question {self.question_name}')
        self.question_number.setFixedSize(100, 40)
        self.question_layout.addWidget(self.question_number, 0, 0)

        self.question = QTextEdit()
        self.question.setFixedSize(
            self.question_size[0], self.question_size[1])
        self.question.setPlaceholderText('Question ...')
        self.question.setObjectName(f'question_{self.question_name}')
        self.question_layout.addWidget(self.question, 1, 0)

        self.question_image = QLabel()
        self.question_image.setObjectName(f'question_{self.question_name}_image')
        self.question_image.setStyleSheet(
            '''
            QLabel {
               border: 1px solid black;
            }
            '''
        )
        self.question_image.setFixedSize(200, 100)
        self.question_layout.addWidget(self.question_image, 1, 1)

        self.question_add_image = QPushButton()
        add_image_icon = QIcon('Icons/466501.png')
        add_image_icon.width, add_image_icon.height = 300, 200
        self.question_add_image.setIcon(add_image_icon)
        self.question_add_image.setFixedSize(40, 40)
        self.question_add_image.setObjectName(question_name)
        self.question_layout.addWidget(self.question_add_image, 1, 2)

        self.option_a = QTextEdit()
        self.option_a.setFixedSize(self.option_size[0], self.option_size[1])
        self.option_a.setPlaceholderText('Option A')
        self.option_a.setObjectName(f'question_{self.question_name}_a')
        self.question_layout.addWidget(self.option_a, 2, 0)

        self.option_b = QTextEdit()
        self.option_b.setFixedSize(self.option_size[0], self.option_size[1])
        self.option_b.setPlaceholderText('Option B')
        self.option_b.setObjectName(f'question_{self.question_name}_b')
        self.question_layout.addWidget(self.option_b, 3, 0)

        self.option_c = QTextEdit()
        self.option_c.setObjectName(f'question_{self.question_name}_c')
        self.option_c.setPlaceholderText('Option C')
        self.option_c.setFixedSize(self.option_size[0], self.option_size[1])
        self.question_layout.addWidget(self.option_c, 4, 0)

        self.option_d = QTextEdit()
        self.option_d.setFixedSize(self.option_size[0], self.option_size[1])
        self.option_d.setPlaceholderText('Option D')
        self.option_d.setObjectName(f'question_{self.question_name}_d')
        self.question_layout.addWidget(self.option_d, 5, 0)

        self.answer = QTextEdit()
        self.answer.setFixedSize(200, self.option_size[1])
        self.answer.setPlaceholderText('Answer')
        self.answer.setObjectName(f'question_{self.question_name}_answer')
        self.question_layout.addWidget(self.answer, 5, 1)


class QuestionSTART(QGridLayout):
    def __init__(self, id_, number, question, option_a, option_b, option_c, option_d, collector):
        QGridLayout.__init__(self)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        self.id_ = id_
        self.number = number
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d

        self.collector = collector

        self.initialization()

    def initialization(self):
        self.option_size = (500, 300)

        self.number_box = QLabel(f'Question {str(self.number)}')
        self.number_box.setAlignment(Qt.AlignCenter)
        self.number_box.setMaximumSize(700, 40)
        self.addWidget(self.number_box, 0, 0)

        self.question_box = QTextBrowser()
        self.question_box.setText(self.question)
        self.question_box.setAlignment(Qt.AlignLeft)
        self.question_box.setMaximumSize(700, 600)
        self.question_box.setObjectName(f'question_{self.number}')
        self.addWidget(self.question_box, 1, 0)

        self.option_a_box = QCheckBox(self.option_a)
        self.option_a_box.clicked.connect(self.option_a_slot)
        self.option_a_box.setMaximumSize(
            self.option_size[0], self.option_size[1])
        self.option_a_box.setObjectName(f'option_a_{self.number}')
        self.addWidget(self.option_a_box, 2, 0)

        self.option_b_box = QCheckBox(self.option_b)
        self.option_b_box.clicked.connect(self.option_b_slot)
        self.option_b_box.setMaximumSize(
            self.option_size[0], self.option_size[1])
        self.option_b_box.setObjectName(f'option_b_{self.number}')
        self.addWidget(self.option_b_box, 3, 0)

        self.option_c_box = QCheckBox(self.option_c)
        self.option_c_box.clicked.connect(self.option_c_slot)
        self.option_c_box.setMaximumSize(
            self.option_size[0], self.option_size[1])
        self.option_c_box.setObjectName(f'option_c_{self.number}')
        self.addWidget(self.option_c_box, 4, 0)

        self.option_d_box = QCheckBox(self.option_d)
        self.option_d_box.clicked.connect(self.option_d_slot)
        self.option_d_box.setMaximumSize(
            self.option_size[0], self.option_size[1])
        self.option_d_box.setObjectName(f'option_d_{self.number}')
        self.addWidget(self.option_d_box, 5, 0)

        self.line_seperator = QLabel(
            '___________________________________________________')
        self.line_seperator.setAlignment(Qt.AlignCenter)
        self.line_seperator.setMaximumHeight(35)
        self.addWidget(self.line_seperator, 6, 0)

    def option_a_slot(self):
        self.option_b_box.setChecked(False)
        self.option_c_box.setChecked(False)
        self.option_d_box.setChecked(False)

        if self.collector:
            try:
                self.collector[self.number -
                               1] = (self.number, self.option_a_box.text(), 'A')
            except IndexError:
                self.collector.insert(
                    self.number, (self.number, self.option_a_box.text(), 'A'))
            except Exception as e:
                raise e
        else:
            self.collector.insert(
                self.number, (self.number, self.option_a_box.text(), 'A'))

    def option_b_slot(self):
        self.option_a_box.setChecked(False)
        self.option_c_box.setChecked(False)
        self.option_d_box.setChecked(False)

        if self.collector:
            try:
                self.collector[self.number -
                               1] = (self.number, self.option_b_box.text(), 'B')
            except IndexError:
                self.collector.insert(
                    self.number, (self.number, self.option_b_box.text(), 'B'))
            except Exception as e:
                raise e
        else:
            self.collector.insert(
                self.number, (self.number, self.option_b_box.text(), 'B'))

    def option_c_slot(self):
        self.option_a_box.setChecked(False)
        self.option_b_box.setChecked(False)
        self.option_d_box.setChecked(False)

        if self.collector:
            try:
                self.collector[self.number -
                               1] = (self.number, self.option_c_box.text(), 'C')
            except IndexError:
                self.collector.insert(
                    self.number, (self.number, self.option_c_box.text(), 'C'))
            except Exception as e:
                raise e
        else:
            self.collector.insert(
                self.number, (self.number, self.option_c_box.text(), 'C'))

    def option_d_slot(self):
        self.option_a_box.setChecked(False)
        self.option_b_box.setChecked(False)
        self.option_c_box.setChecked(False)

        if self.collector:
            try:
                self.collector[self.number -
                               1] = (self.number, self.option_d_box.text(), 'D')
            except IndexError:
                self.collector.insert(
                    self.number, (self.number, self.option_d_box.text(), 'D'))
            except Exception as e:
                raise e
        else:
            self.collector.insert(
                self.number, (self.number, self.option_d_box.text(), 'D'))


class ExamSheet(QWidget):
    def __init__(self, class_, subject, teacher, upload_time, exam_time):
        QWidget.__init__(self)

        self.class_ = class_
        self.subject = subject
        self.teacher = teacher
        self.upload_time = upload_time
        self.exam_time = exam_time

        self.exam_size = (1500, 700)
        self.details_size = 750

        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.setMaximumWidth(1600)
        self.setLayout(self.scroll_layout)

        self.widget_layout = QVBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignTop)

        self.scroll_group = QGroupBox()
        self.scroll_group.setMaximumWidth(self.exam_size[0])
        self.scroll_group.setAutoFillBackground(True)
        self.scroll_group.autoFillBackground()
        self.scroll_group.setLayout(self.widget_layout)
        self.scroll_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 5px;
            }
            '''
        )

        self.scroll_scroll = QScrollArea()
        self.scroll_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )
        self.scroll_scroll.setMaximumWidth((self.details_size * 5))
        self.scroll_scroll.setWidget(self.scroll_group)
        self.scroll_scroll.setWidgetResizable(True)

        self.scroll_layout.addWidget(self.scroll_scroll)

        self.initialization()

    def initialization(self):
        self.topBAR()
        self.mainPAGE()

    def topBAR(self):
        self.top_bar_layout = QHBoxLayout()
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_layout.setSpacing(10)
        self.top_bar_layout.setAlignment(Qt.AlignTop)

        self.top_bar_group = QGroupBox()
        self.top_bar_group.setMaximumSize((self.details_size * 5) + 30, 30)
        self.top_bar_group.setLayout(self.top_bar_layout)
        self.top_bar_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: white;
                border-bottom: 1px solid rgb(255, 170, 135);
            }
            '''
        )

        self.class_name = QLabel(f'Class : {self.class_}')
        self.class_name.setMaximumWidth(self.details_size)
        self.class_name.setStyleSheet(
            '''
            QLabel {
                border-right: 1px solid black;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.class_name)

        self.subject_name = QLabel(f'Subject : {self.subject}')
        self.subject_name.setMaximumWidth(self.details_size)
        self.subject_name.setStyleSheet(
            '''
            QLabel {
                border-right: 1px solid black;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.subject_name)

        self.teacher_name = QLabel(f'Teacher : {self.teacher}')
        self.teacher_name.setMaximumWidth(self.details_size)
        self.teacher_name.setStyleSheet(
            '''
            QLabel {
                border-right: 1px solid black;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.teacher_name)

        self.created = QLabel(f'Scheduled Time : {self.upload_time}')
        self.created.setMaximumWidth(self.details_size)
        self.created.setStyleSheet(
            '''
            QLabel {
                border-right: 1px solid black;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.created)

        if self.exam_time != 0:
            self.time_ = QLabel(f'Time : {self.exam_time} minutes')
            self.time_.setMaximumWidth(self.details_size)
            self.time_.setStyleSheet(
                '''
                QLabel {
                    border-right: 1px solid black;
                }
                '''
            )
            self.top_bar_layout.addWidget(self.time_)
        else:
            self.exam_time = 60
            self.time_ = QLabel(f'Time : {self.exam_time} minutes')
            self.time_.setMaximumWidth(self.details_size)
            self.time_.setStyleSheet(
                '''
                QLabel {
                    border: 0px;
                }
                '''
            )
            self.top_bar_layout.addWidget(self.time_)

        self.widget_layout.addWidget(self.top_bar_group)

        self.extras_layout = QHBoxLayout()
        self.extras_layout.setSpacing(10)
        self.extras_layout.setAlignment(Qt.AlignCenter)
        self.extras_layout.setContentsMargins(0, 0, 0, 0)

        self.add_question_button = QPushButton('Add Question')
        self.add_question_button.setMaximumSize(self.details_size + 40, 25)
        self.add_question_button.clicked.connect(self.addQUESTIONS)
        self.add_question_button.setStyleSheet(
            '''
            QPushButton {
                background-color: rgb(245, 200, 100);
                padding: 4px;
                font-size: 13px;
                border: 0px;
                border-radius: 3px;
                }
            .QPushButton:hover {
                background-color: rgb(240, 195, 50);
                }
            '''
        )
        self.extras_layout.addWidget(self.add_question_button)

        self.submit_question_button = QPushButton('Submit')
        self.submit_question_button.clicked.connect(self.submitQUESTIONS)
        self.submit_question_button.setMaximumSize(self.details_size + 40, 25)
        self.submit_question_button.setStyleSheet(
            '''
            QPushButton {
                background-color: rgb(205, 160, 120);
                font-size: 13px;
                padding: 4px;
                border: 0px;
                border-radius: 3px;
                }
            .QPushButton:hover {
                background-color: rgb(200, 150, 100);
                }
            '''
        )
        self.extras_layout.addWidget(self.submit_question_button)

        self.extras_group = QGroupBox()
        self.extras_group.setMaximumHeight(30)
        self.extras_group.setStyleSheet(
            '''
            QGroupBox{
                border: 0px;
            }
            '''
        )
        self.extras_group.setLayout(self.extras_layout)

        self.widget_layout.addWidget(self.extras_group)

    def mainPAGE(self):
        self.main_page_layout = QVBoxLayout()
        self.main_page_layout.setSpacing(5)
        self.main_page_layout.setAlignment(Qt.AlignTop)
        self.main_page_layout.setContentsMargins(0, 0, 0, 0)

        self.main_page_size = (1100, 800)

        self.main_page_group = QGroupBox('10px Padding')
        self.main_page_group.setAlignment(Qt.AlignTop)
        self.main_page_group.setMaximumWidth(self.main_page_size[0])
        self.main_page_group.setLayout(self.main_page_layout)
        self.main_page_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 10px;
            }
            '''
        )

        self.main_page_scroll = QScrollArea()
        self.main_page_scroll.setWidget(self.main_page_group)
        self.main_page_scroll.setWidgetResizable(True)
        self.main_page_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.number = 1

        self.addQUESTIONS()

    def addQUESTIONS(self):
        try:
            self.question_layout = QGridLayout()
            self.question_layout.setObjectName(f'question_layout_{self.number}')
            self.question_layout.setSpacing(10)
            self.question_layout.setContentsMargins(0, 0, 0, 0)
            self.question_layout.setAlignment(Qt.AlignLeft)

            self.widget_layout.addLayout(self.question_layout)
            self.main_page_layout.addWidget(
                Question(self.number, self.question_layout))
            self.number += 1
        except Exception as e:
            print(str(e))

    def submitQUESTIONS(self):
        from Projects.SchoolManagement.DataBaseTool import DataBase

        DataBase.create_student_exam_status(self.class_, self.subject)

        self.submitSEQ = GetQuestions(self.number)
        self.submitSEQ.countChanged.connect(self.onCountChanged)
        self.submitSEQ.run()

    def onCountChanged(self):
        self.question_collection = []
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            question_name = f'{self.class_name}_{self.subject_name}'
            self.status = 'False'
            self.register_table = False

            for i in range(1, self.number):
                question = self.findChild(QTextEdit, f'question_{i}').toPlainText()
                option_a = self.findChild(QTextEdit, f'question_{i}_a').toPlainText()
                option_b = self.findChild(QTextEdit, f'question_{i}_b').toPlainText()
                option_c = self.findChild(QTextEdit, f'question_{i}_c').toPlainText()
                option_d = self.findChild(QTextEdit, f'question_{i}_d').toPlainText()
                answer = self.findChild(QTextEdit, f'question_{i}_answer').toPlainText()

                if (len(question) and len(option_a) and len(option_b) and len(option_c), len(option_d) and len(answer)) != 0:
                    DataBase.create_exam_questions(self.class_, self.subject)
                    DataBase.insert_exam_questions(
                        self.class_,
                        self.subject,
                        i, question,
                        option_a,
                        option_b,
                        option_c,
                        option_d,
                        answer
                    )
                    self.register_table = True
                    self.question_collection.append(
                        (
                            i,
                            question,
                            option_a,
                            option_b,
                            option_c,
                            option_d,
                            answer
                        )
                    )

            if self.register_table == True:
                DataBase.create_school_questions()
                DataBase.insert_school_questions(
                    self.class_,
                    self.subject,
                    self.teacher,
                    self.upload_time,
                    self.exam_time,
                    self.status
                )
        except Exception as e:
            raise e


class ExamCheck(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.exam_size = (1500, 700)
        self.details_size = 750

        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.setMaximumWidth(self.exam_size[1])
        self.setLayout(self.scroll_layout)

        self.widget_layout = QVBoxLayout()
        self.widget_layout.setSpacing(0)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignTop)

        self.scroll_group = QGroupBox()
        self.scroll_group.setMaximumWidth(self.exam_size[0])
        self.scroll_group.setAutoFillBackground(True)
        self.scroll_group.autoFillBackground()
        self.scroll_group.setLayout(self.widget_layout)
        self.scroll_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 5px;
            }
            '''
        )

        self.scroll_scroll = QScrollArea()
        self.scroll_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )
        self.scroll_scroll.setMaximumWidth((self.details_size * 5))
        self.scroll_scroll.setWidget(self.scroll_group)
        self.scroll_scroll.setWidgetResizable(True)

        self.scroll_layout.addWidget(self.scroll_scroll)

        self.initialization()

    def initialization(self):
        self.index_i = 1
        self.widget_layout.addWidget(CheckTableDef())

        from Projects.SchoolManagement.DataBaseTool import DataBase

        self.all_exams = DataBase.get_school_questions()

        self.submitSEQ = GetQuestions(len(self.all_exams))
        self.submitSEQ.countChanged.connect(self.distributeTABLE)
        self.submitSEQ.run()

    def distributeTABLE(self):
        # (6, 'AdvancedLevel', 'Data Science', 'MD', '1/1/00 12:00 AM', '60', 'False')
        try:
            if self.all_exams:
                for exam in self.all_exams:
                    self.widget_layout.addWidget(CheckTable(
                        exam[0], self.index_i, exam[1], exam[2], exam[3], exam[4], exam[5]))
        except Exception as e:
            raise e


class ExamCheckResult(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.exam_size = (2000, 700)
        self.details_size = 750

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(5)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.scroll_layout = QHBoxLayout()
        self.scroll_layout.setSpacing(0)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.scroll_group = QGroupBox('Exam : Results')
        self.scroll_group.setMaximumWidth(self.exam_size[0])
        self.scroll_group.setLayout(self.scroll_layout)
        self.scroll_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding-top: 17px;
                padding-left: 5px;
                padding-right: 5px;
            }
            '''
        )

        self.scroll_scroll = QScrollArea()
        self.scroll_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )
        self.scroll_scroll.setWidget(self.scroll_group)
        self.scroll_scroll.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll_scroll)

        self.setMaximumWidth(1600)
        self.setLayout(self.main_layout)

        self.initialization()

    def initialization(self):
        self.left_group_layout = QVBoxLayout()
        self.right_group_layout = QGridLayout()

        self.left_layout()
        self.right_layout()

    def left_layout(self):
        self.left_group_layout.setSpacing(0)
        self.left_group_layout.setContentsMargins(0, 0, 0, 0)
        self.left_group_layout.setAlignment(Qt.AlignTop)

        self.left_group = QGroupBox()
        self.left_group.setAlignment(Qt.AlignTop)
        self.left_group.setLayout(self.left_group_layout)
        self.left_group.setMaximumWidth(1300)
        self.left_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
            }
            '''
        )

        self.scroll_layout.addWidget(self.left_group)

        self.resultTABLE()

    def resultTABLE(self):
        self.table_left_layout = QVBoxLayout()
        self.table_left_layout.setContentsMargins(0, 0, 0, 0)
        self.table_left_layout.setSpacing(0)
        self.table_left_layout.setAlignment(Qt.AlignTop)

        self.table_left_group = QGroupBox()
        self.table_left_group.setLayout(self.table_left_layout)
        self.table_left_group.setMaximumWidth(1300)
        self.table_left_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
            }
            '''
        )

        self.table_left_scroll = QScrollArea()
        self.table_left_scroll.setWidget(self.table_left_group)
        self.table_left_scroll.setWidgetResizable(True)
        self.table_left_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.left_group_layout.addWidget(self.table_left_scroll)

        self.table_index = 1
        self.table_current = ['1']

        self.table_left_layout.addWidget(ResultTableDef())

        self.submitSEQ = GetQuestions(30)
        self.submitSEQ.countChanged.connect(self.begin_distribution)
        self.submitSEQ.run()

    def begin_distribution(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.all_class_avail_questions = DataBase.get_school_questions()
            if len(self.all_class_avail_questions) != 0:
                for result in self.all_class_avail_questions:
                    self.table_left_layout.addWidget(ResultTable(
                        result[0],
                        self.table_index,
                        result[1],
                        result[2],
                        result[3],
                        [
                            self.right_group_layout,
                            self.table_current
                        ]
                    )
                    )
                    self.table_index += 1
        except Exception as e:
            raise e

    def right_layout(self):
        self.right_group_layout.setSpacing(0)
        self.right_group_layout.setContentsMargins(0, 0, 0, 0)
        self.right_group_layout.setAlignment(Qt.AlignTop)

        self.right_group = QGroupBox()
        self.right_group.setAlignment(Qt.AlignTop)
        self.right_group.setLayout(self.right_group_layout)
        self.right_group.setMaximumWidth(1300)
        self.right_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                /* border: 1px solid black; */
            }
            '''
        )

        self.right_group_scroll = QScrollArea()
        self.right_group_scroll.setMaximumWidth(1600)
        self.right_group_scroll.setWidget(self.right_group)
        self.right_group_scroll.setWidgetResizable(True)
        self.right_group_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.scroll_layout.addWidget(self.right_group_scroll)


class ExamStart(QWidget):
    def __init__(self, reg_num='', class_='', subject='', teacher='', time_allocated='', side_nav='', top_nav='', m='', re_spawn=''):
        QWidget.__init__(self)

        self.reg_num = reg_num
        self.class_ = class_
        self.subject = subject
        self.teacher = teacher
        self.time_allocated = time_allocated
        self.side_nav = side_nav
        self.top_nav = top_nav
        self.m = m
        self.re_spawn = re_spawn

        self.exam_size = (1500, 700)
        self.details_size = 750

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(5)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.scroll_group = QGroupBox()
        self.scroll_group.setMaximumWidth(self.exam_size[0])
        self.scroll_group.setAutoFillBackground(True)
        self.scroll_group.autoFillBackground()
        self.scroll_group.setLayout(self.scroll_layout)
        self.scroll_group.setStyleSheet(
            '''
            QGroupBox {
                border: 1px solid black;
            }
            '''
        )

        self.main_layout.addWidget(self.scroll_group)

        self.setMaximumWidth(1600)
        self.setLayout(self.main_layout)

        self.initialization()

    def initialization(self):
        self.topBAR()
        self.distributeQUEStIONS()

    def topBAR(self):
        self.top_bar_layout = QHBoxLayout()
        self.top_bar_layout.setSpacing(0)
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_layout.setAlignment(Qt.AlignTop)

        self.box_size = (750, 70)

        self.reg_num_box = QLabel(f'Reg Number : {self.reg_num}')
        self.reg_num_box.setMaximumSize(self.box_size[0], self.box_size[1])
        self.reg_num_box.setAlignment(Qt.AlignCenter)
        self.reg_num_box.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                border: 1px solid #ffccff;
                font-weight: bold;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.reg_num_box)

        self.class_box = QLabel(f'Class : {self.class_}')
        self.class_box.setMaximumSize(self.box_size[0], self.box_size[1])
        self.class_box.setAlignment(Qt.AlignCenter)
        self.class_box.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                border: 1px solid #ffccff;
                font-weight: bold;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.class_box)

        self.subject_box = QLabel(f'Subject : {self.subject}')
        self.subject_box.setMaximumSize(self.box_size[0], self.box_size[1])
        self.subject_box.setAlignment(Qt.AlignCenter)
        self.subject_box.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                border: 1px solid #ffccff;
                font-weight: bold;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.subject_box)

        self.teacher_box = QLabel(f'Teacher : {self.teacher}')
        self.teacher_box.setMaximumSize(self.box_size[0], self.box_size[1])
        self.teacher_box.setAlignment(Qt.AlignCenter)
        self.teacher_box.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                border: 1px solid #ffccff;
                font-weight: bold;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.teacher_box)

        self.time_allocated_box = QLabel(f'Time : {self.time_allocated} minutes')
        self.time_allocated_box.setMaximumSize(
            self.box_size[0], self.box_size[1])
        self.time_allocated_box.setAlignment(Qt.AlignCenter)
        self.time_allocated_box.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                border: 1px solid #ffccff;
                font-weight: bold;
            }
            '''
        )
        self.top_bar_layout.addWidget(self.time_allocated_box)

        self.top_bar_group = QGroupBox()
        self.top_bar_group.setAlignment(Qt.AlignTop)
        self.top_bar_group.setMaximumSize(1800, self.box_size[1] - 20)
        self.top_bar_group.setLayout(self.top_bar_layout)
        self.top_bar_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: white;
            }
            '''
        )

        self.scroll_layout.addWidget(self.top_bar_group)

    def distributeQUEStIONS(self):
        self.question_main_layout = QVBoxLayout()
        self.question_main_layout.setSpacing(0)
        self.question_main_layout.setContentsMargins(0, 0, 0, 0)
        self.question_main_layout.setAlignment(Qt.AlignTop)

        self.tool_layout = QHBoxLayout()
        self.tool_layout.setContentsMargins(0, 0, 0, 0)
        self.tool_layout.setAlignment(Qt.AlignRight)
        self.tool_layout.setSpacing(5)

        self.calculator = QPushButton('Calculator')
        self.calculator.clicked.connect(self.calculator_slot)
        self.tool_layout.addWidget(self.calculator)

        self.submit = QPushButton('End Exam')
        self.submit.clicked.connect(self.submit_slot)
        self.tool_layout.addWidget(self.submit)

        self.timer = QLabel(f'{self.time_allocated} : 00')
        self.timer.setAlignment(Qt.AlignCenter)
        self.timer.setStyleSheet(
            '''
            QLabel {
                font-size: 14px;
                font: Verdana;
                border-radius: 3px;
                border: 1px solid black;
            }
            '''
        )
        self.tool_layout.addWidget(self.timer)

        self.question_main_layout.addLayout(self.tool_layout)

        self.question_layout = QVBoxLayout()
        self.question_layout.setAlignment(Qt.AlignCenter)
        # self.question_layout.setAlignment(Qt.AlignTop)
        self.question_layout.setSpacing(5)
        self.question_layout.setContentsMargins(0, 0, 0, 0)

        self.question_collector = []

        self.submitSEQ = GetQuestions(30)
        self.submitSEQ.countChanged.connect(self.begin_distribution)
        self.submitSEQ.run()

        self.question_group = QGroupBox()
        self.question_group.setLayout(self.question_layout)
        self.question_group.setMaximumWidth(1500)
        self.question_group.setStyleSheet(
            '''
            QGroupBox {
                border: 1px solid black;
                padding: 10px;
            }
            '''
        )

        self.question_scroll = QScrollArea()
        self.question_scroll.setWidget(self.question_group)
        self.question_scroll.setWidgetResizable(True)
        self.question_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.question_main_layout.addWidget(self.question_scroll)
        self.scroll_layout.addLayout(self.question_main_layout)

    def begin_distribution(self):
        class_ = self.class_
        subject = self.subject
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.current_question = DataBase.get_exam_questions(
                class_, subject)

            for i in self.current_question:
                self.question_layout.addLayout(QuestionSTART(
                    i[0], i[0], i[1], i[3], i[4], i[5], i[6], self.question_collector))
                self.question_collector.append(())
        except Exception as e:
            raise e

    def calculator_slot(self):
        pass

    def submit_slot(self):
        self.confirmation_layout = QGridLayout()
        self.confirmation_layout.setContentsMargins(10, 10, 10, 10)
        self.confirmation_layout.setAlignment(Qt.AlignCenter)
        self.confirmation_layout.setSpacing(5)

        self.confirmation_dialog = QDialog()
        self.confirmation_dialog.setWindowTitle('Exam Invigilator')
        self.confirmation_dialog.setLayout(self.confirmation_layout)

        self.msg_layout = QVBoxLayout()
        self.msg_layout.setAlignment(Qt.AlignCenter)
        self.confirmation_layout.addLayout(self.msg_layout, 0, 0)

        msg = 'Are you sure you want to End this exam. \nYour exam would be automatically submitted by clicking yes.'
        self.msg = QLabel(msg)
        self.msg_layout.addWidget(self.msg)

        self.yes = QPushButton('Yes')
        self.yes.setMaximumSize(200, 40)
        self.yes.clicked.connect(self.yes_slot)
        self.confirmation_layout.addWidget(self.yes, 1, 1)

        self.no = QPushButton('No')
        self.no.setMaximumSize(200, 40)
        self.no.clicked.connect(self.no_slot)
        self.confirmation_layout.addWidget(self.no, 1, 2)

        self.confirmation_dialog.show()

    def yes_slot(self):
        try:
            self.submit_final()
            self.confirmation_dialog.close()
        except Exception as e:
            raise e

    def no_slot(self):
        try:
            self.confirmation_dialog.close()
        except Exception as e:
            raise e

    def submit_final(self):
        try:
            self.submitCHD = GetQuestions(30)
            self.submitCHD.countChanged.connect(self.submit_child)
            self.submitCHD.run()
        except Exception as e:
            raise e

    def exam_mode_deactivate(self):
        self.side_nav.setEnabled(True)
        self.side_nav.setHidden(False)

        self.top_nav.setEnabled(True)
        self.top_nav.setHidden(False)

        self.m.showNormal()

        self.setHidden(True)
        self.setEnabled(False)

        self.re_spawn()

    def submit_child(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.score = 0
            self.exam_mode_deactivate()
            for i in range(0, len(self.question_collector)):
                if self.question_collector[i]:
                    student_ans = self.question_collector[i][1]
                    question_ans = self.current_question[i][-1]

                    if student_ans == question_ans:
                        self.score += 1

            self.score_percent = f'{round(((self.score / len(self.question_collector)) * 100), 2)} %'

            DataBase.update_exam_status(
                self.class_, self.reg_num, self.subject, self.score_percent, 'True')
        except Exception as e:
            raise e

    def timer_slot(self):
        pass


class Exam(QWidget):
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
        self.dash_board_button.setFixedSize(
            self.button_width, self.button_height)
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
        self.students_button.setFixedSize(
            self.button_width, self.button_height)
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
        self.subjects_button.setFixedSize(
            self.button_width, self.button_height)
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
        self.class_routine_button.setFixedSize(
            self.button_width, self.button_height)
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
        self.attendance_button.setFixedSize(
            self.button_width, self.button_height)
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
        self.right_board_group.setMaximumWidth(1900)
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

        self.examPAGE()
        self.examLOGIN()

    def examPAGE(self):
        self.scroll_width = 1900
        self.scroll_height = 850

        self.exam_layout = QVBoxLayout()
        self.exam_layout.setAlignment(Qt.AlignCenter)
        self.exam_layout.setContentsMargins(0, 0, 0, 0)
        self.exam_layout.setSpacing(10)

        self.exam_group = QGroupBox('Exam')
        self.exam_group.setMaximumWidth(self.scroll_width)
        self.exam_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.exam_group.setContentsMargins(0, 0, 0, 0)
        self.exam_group.setLayout(self.exam_layout)

        self.exam_scroll = QScrollArea()
        self.exam_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.exam_scroll.setWidgetResizable(True)
        self.exam_scroll.setWidget(self.exam_group)

        self.right_board_layout.addWidget(self.exam_scroll)

    def examLOGIN(self):
        self.carpet_layout = QVBoxLayout()
        self.carpet_layout.setContentsMargins(0, 0, 0, 0)
        self.carpet_layout.setAlignment(Qt.AlignCenter)
        self.carpet_layout.setAlignment(Qt.AlignTop)

        self.title_layer = QHBoxLayout()
        self.title_layer.setAlignment(Qt.AlignCenter)
        self.title_layer.setContentsMargins(0, 0, 0, 0)
        self.carpet_layout.addLayout(self.title_layer)

        self.top_layout = QGridLayout()
        self.top_layout.setAlignment(Qt.AlignCenter)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.setSpacing(10)

        self.title = f'{self.school_name} : Login'

        self.form_title = QLabel(self.title)
        self.form_title.setFixedSize(300, 40)
        self.form_title.setAlignment(Qt.AlignCenter)
        self.form_title.setStyleSheet(
            '''
            QLabel {
                padding: 5px;
                background-color: #ff9933;
                border-left: ;
                border-right: ;
                font-family: Verdana;
                font-weight: bold;
                font-size: 20px;
                color: white;
                }
            '''
        )
        self.title_layer.addWidget(self.form_title)

        self.name_size = (300, 30)

        self.username = QLineEdit()
        self.username.setStyleSheet(
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
        self.username.setMaximumSize(self.name_size[0], self.name_size[1])
        self.username.setPlaceholderText('Username')
        self.top_layout.addWidget(self.username, 1, 0)

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(
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
        self.password.setMaximumSize(self.name_size[0], self.name_size[1])
        self.password.setPlaceholderText('Password')
        self.top_layout.addWidget(self.password, 2, 0)

        self.reg_button_size = self.name_size

        self.reg_update_button = QPushButton('Login')
        self.reg_update_button.clicked.connect(self.reg_update_slot)
        self.reg_update_button.setFixedSize(
            self.reg_button_size[0], self.reg_button_size[1])
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
        self.top_layout.addWidget(self.reg_update_button, 3, 0)

        self.top_widget = QGroupBox()
        self.top_widget.setAlignment(Qt.AlignCenter)
        self.top_widget.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 5px;
                }
            '''
        )
        self.top_widget.setContentsMargins(0, 0, 0, 0)
        self.top_widget.setLayout(self.carpet_layout)

        self.carpet_layout.addLayout(self.top_layout)
        self.exam_layout.addWidget(self.top_widget)

    def reg_update_slot(self):
        try:
            if len(self.username.text()) != 0:
                if len(self.password.text()) != 0:
                    from Projects.SchoolManagement.DataBaseTool.DataBase import get_teacher, get_teacher_all

                    teachers = get_teacher('username')
                    if self.username.text() in teachers:
                        user_password = get_teacher('password')
                        if self.password.text() == user_password[teachers.index(self.username.text())]:
                            msg = 'Login successful.'
                            message_box = QMessageBox()
                            message_box.about(self, 'School Manager', msg)

                            all_teachers = get_teacher_all()
                            first_name = get_teacher_all(
                            )[teachers.index(self.username.text())][1]
                            last_name = get_teacher_all(
                            )[teachers.index(self.username.text())][2]

                            self.user_f_name.setText(first_name)
                            self.user_l_name.setText(last_name)

                            self.first_in = first_name
                            self.last_in = last_name

                            self.examUSER()
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

    def examUSER(self):
        self.exam_scroll.setHidden(True)
        self.exam_scroll.setEnabled(False)

        self.scroll_width = 1500
        self.scroll_height = 850

        self.user_layout = QVBoxLayout()
        self.user_layout.setAlignment(Qt.AlignCenter)
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setSpacing(10)

        self.user_group = QGroupBox('Exam')
        self.user_group.setMaximumWidth(self.scroll_width)
        self.user_group.setStyleSheet(
            '''
            QGroupBox {
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.user_group.setContentsMargins(0, 0, 0, 0)
        self.user_group.setLayout(self.user_layout)

        self.user_scroll = QScrollArea()
        self.user_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.user_scroll.setWidgetResizable(True)
        self.user_scroll.setWidget(self.user_group)

        self.right_board_layout.addWidget(self.user_scroll)
        self.examTOOLS()

    def examTOOLS(self):
        self.tool_grid_layout = QGridLayout()
        self.tool_grid_layout.setAlignment(Qt.AlignCenter)
        self.tool_grid_layout.setContentsMargins(0, 0, 0, 0)

        self.tool_size = (230, 150)

        self.set_exams = QPushButton('Set Exams')
        self.set_exams.clicked.connect(self.set_exams_slot)
        self.set_exams.setStyleSheet(
            '''
            QPushButton {
                background-color: #ff8c1a;
                border: 0px;
                font-family: Verdana;
                border-radius: 5px;
                font-size: 14px;
                color: white;
                }
            .QPushButton:hover {
                background-color: #ff9933;
                }
            '''
        )
        # self.set_exams.setIcon(QIcon('Icons/048.-drafting.png'))
        self.set_exams.setMinimumSize(self.tool_size[0], self.tool_size[1])
        self.tool_grid_layout.addWidget(self.set_exams, 0, 0)

        self.check_exams = QPushButton('Check Exams')
        self.check_exams.clicked.connect(self.check_exams_slot)
        self.check_exams.setStyleSheet(
            '''
            QPushButton {
                background-color: #ff8c1a;
                border: 0px;
                font-family: Verdana;
                border-radius: 5px;
                font-size: 14px;
                color: white;
                }
            .QPushButton:hover {
                background-color: #ff9933;
                }
            '''
        )
        # self.check_exams.setIcon(QIcon('Icons/001.-view.png'))
        self.check_exams.setMinimumSize(self.tool_size[0], self.tool_size[1])
        self.tool_grid_layout.addWidget(self.check_exams, 0, 1)

        self.results = QPushButton('Results')
        self.results.clicked.connect(self.results_slot)
        self.results.setStyleSheet(
            '''
            QPushButton {
                background-color: #ff8c1a;
                border: 0px;
                font-family: Verdana;
                border-radius: 5px;
                font-size: 14px;
                color: white;
                }
            .QPushButton:hover {
                background-color: #ff9933;
                }
            '''
        )
        # self.results.setIcon(QIcon('Icons/001.-ebook.png'))
        self.results.setMinimumSize(self.tool_size[0], self.tool_size[1])
        self.tool_grid_layout.addWidget(self.results, 1, 0)

        self.start_exam = QPushButton('Start Exam')
        self.start_exam.clicked.connect(self.start_exam_slot)
        self.start_exam.setStyleSheet(
            '''
            QPushButton {
                background-color: #ff8c1a;
                border: 0px;
                font-family: Verdana;
                border-radius: 5px;
                font-size: 14px;
                color: white;
                }
            .QPushButton:hover {
                background-color: #ff9933;
                }
            '''
        )
        # self.start_exam.setIcon(QIcon('Icons/466501.png'))
        self.start_exam.setMinimumSize(self.tool_size[0], self.tool_size[1])
        self.tool_grid_layout.addWidget(self.start_exam, 1, 1)

        self.tool_grid_group = QGroupBox()
        self.tool_grid_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.tool_grid_group.setContentsMargins(0, 0, 0, 0)
        self.tool_grid_group.setAlignment(Qt.AlignCenter)
        self.tool_grid_group.setLayout(self.tool_grid_layout)

        self.tool_grid_scroll = QScrollArea()
        self.tool_grid_scroll.setMaximumWidth(self.scroll_width + 100)
        self.tool_grid_scroll.setWidgetResizable(True)
        self.tool_grid_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )
        self.tool_grid_scroll.setWidget(self.tool_grid_group)

        self.user_layout.addWidget(self.tool_grid_scroll)

    def set_exams_slot(self):
        try:
            self.examFORM()
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def check_exams_slot(self):
        try:
            self.examCHECK()
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def start_exam_slot(self):
        try:
            self.examSTART()
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def results_slot(self):
        try:
            self.examCHECKRESULTS()
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

    def examFORM(self):
        self.user_scroll.setHidden(True)
        self.user_scroll.setEnabled(False)

        self.exam_form_layout = QGridLayout()
        self.exam_form_layout.setContentsMargins(0, 0, 0, 0)
        self.exam_form_layout.setAlignment(Qt.AlignCenter)

        self.title_form_layout = QVBoxLayout()
        self.title_form_layout.setContentsMargins(0, 0, 0, 0)
        self.title_form_layout.setAlignment(Qt.AlignCenter)
        self.exam_form_layout.addLayout(self.title_form_layout, 0, 0)

        self.form_title = QLabel('Exam Setup')
        self.form_title.setMaximumSize(300, 40)
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
        self.title_form_layout.addWidget(self.form_title)

        self.comboBox_font = QFont('Verdana', 8)

        self.exam_class = QComboBox()
        self.exam_class.setFont(self.comboBox_font)
        self.exam_class.addItem('--class--')
        self.exam_class.setMaximumSize(230, 30)
        self.exam_class_find_attached()
        self.exam_class.currentIndexChanged.connect(
            self.exam_subject_find_attached)
        self.exam_form_layout.addWidget(self.exam_class, 1, 0)

        self.exam_subject = QComboBox()
        self.exam_subject.addItem('--subject--')
        self.exam_subject.setFont(self.comboBox_font)
        self.exam_subject.setMaximumSize(230, 30)
        self.exam_form_layout.addWidget(self.exam_subject, 2, 0)

        self.time_allocated_start = QSpinBox()
        self.time_allocated_start.setMaximum(300)
        self.time_allocated_start.setMaximumSize(230, 30)
        self.exam_form_layout.addWidget(self.time_allocated_start, 3, 0)

        self.date_created = QDateTimeEdit()
        self.date_created.setMaximumSize(230, 35)
        self.exam_form_layout.addWidget(self.date_created, 4, 0)

        self.exam_teacher_username = QLineEdit()
        self.exam_teacher_username.setPlaceholderText('Username')
        self.exam_teacher_username.setStyleSheet(
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
        self.exam_teacher_username.setMaximumSize(230, 30)
        self.exam_form_layout.addWidget(self.exam_teacher_username, 5, 0)

        self.exam_teacher_password = QLineEdit()
        self.exam_teacher_password.setEchoMode(QLineEdit.Password)
        self.exam_teacher_password.setPlaceholderText('Password')
        self.exam_teacher_password.setStyleSheet(
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
        self.exam_teacher_password.setMaximumSize(230, 30)
        self.exam_form_layout.addWidget(self.exam_teacher_password, 6, 0)

        self.proceed_button = QPushButton('Proceed')
        self.proceed_button.clicked.connect(self.proceed_slot)
        self.proceed_button.setFixedSize(230, 30)
        self.proceed_button.setStyleSheet(
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
        self.exam_form_layout.addWidget(self.proceed_button, 7, 0)

        self.exam_form_group = QGroupBox('Exam: Set Exam')
        self.exam_form_group.setContentsMargins(0, 0, 0, 0)
        self.exam_form_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.exam_form_group.setLayout(self.exam_form_layout)

        self.exam_form_scroll = QScrollArea()
        self.exam_form_scroll.setWidget(self.exam_form_group)
        self.exam_form_scroll.setWidgetResizable(True)
        self.exam_form_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )

        self.right_board_layout.addWidget(self.exam_form_scroll)

    def exam_class_find_attached(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            items = DataBase.get_school_class()
            for item in items:
                if item:
                    self.exam_class.addItem(item)
        except Exception as e:
            raise e

    def exam_subject_find_attached(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            if self.exam_class.currentText() != '--class--':
                items = DataBase.get_class_sub(self.exam_class.currentText())
                self.exam_subject.clear()
                for item in items:
                    if item:
                        self.exam_subject.addItem(item)
        except Exception as e:
            raise e

    def proceed_slot(self):
        try:
            class_ = self.exam_class.currentText()
            subject = self.exam_subject.currentText()
            username = self.exam_teacher_username.text()
            password = self.exam_teacher_password.text()
            upload_time = self.date_created.text()
            exam_time = int(self.time_allocated_start.text())
            if class_ != '--class--' and subject != '--subject--':
                if (len(username) and len(password)) != 0:
                    from Projects.SchoolManagement.DataBaseTool import DataBase

                    teachers = DataBase.get_teacher('username')
                    if username in teachers:
                        user_passwords = DataBase.get_teacher('password')
                        if password == user_passwords[teachers.index(username)]:
                            msg = 'Login successful!!!'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)

                            self.exam_form_scroll.setHidden(True)
                            self.exam_form_scroll.setEnabled(False)

                            self.next_page = ExamSheet(
                                class_, subject, username, upload_time, exam_time)
                            self.right_board_layout.addWidget(self.next_page)
                        else:
                            msg = 'Login failed, Invalid Username or Password.'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)
                else:
                    msg = 'Please fill in your username and password for proper identification.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            else:
                msg = 'Please select class and subject.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e

    def examCHECK(self):
        self.form_size = (300, 40)

        self.user_scroll.setHidden(True)
        self.user_scroll.setEnabled(False)

        self.exam_check_layout = QGridLayout()
        self.exam_check_layout.setContentsMargins(0, 0, 0, 0)
        self.exam_check_layout.setAlignment(Qt.AlignCenter)

        self.title_check_layout = QVBoxLayout()
        self.title_check_layout.setContentsMargins(0, 0, 0, 0)
        self.title_check_layout.setAlignment(Qt.AlignCenter)
        self.exam_check_layout.addLayout(self.title_check_layout, 0, 0)

        self.form_title = QLabel('Login')
        self.form_title.setAlignment(Qt.AlignCenter)
        self.form_title.setMaximumSize(self.form_size[0], 40)
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
        self.title_check_layout.addWidget(self.form_title)

        self.exam_teacher_check_username = QLineEdit()
        self.exam_teacher_check_username.setPlaceholderText('Username')
        self.exam_teacher_check_username.setStyleSheet(
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
        self.exam_teacher_check_username.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_username, 1, 0)

        self.exam_teacher_check_password = QLineEdit()
        self.exam_teacher_check_password.setEchoMode(QLineEdit.Password)
        self.exam_teacher_check_password.setPlaceholderText('Password')
        self.exam_teacher_check_password.setStyleSheet(
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
        self.exam_teacher_check_password.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_password, 2, 0)

        self.proceed_check = QPushButton('Proceed')
        self.proceed_check.clicked.connect(self.check_proceed_slot)
        self.proceed_check.setFixedSize(self.form_size[0], 30)
        self.proceed_check.setStyleSheet(
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
        self.exam_check_layout.addWidget(self.proceed_check, 3, 0)

        self.exam_check_group = QGroupBox('Exam: Check Exams')
        self.exam_check_group.setMaximumWidth(1900)
        self.exam_check_group.setContentsMargins(0, 0, 0, 0)
        self.exam_check_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.exam_check_group.setLayout(self.exam_check_layout)

        self.exam_check_scroll = QScrollArea()
        self.exam_check_scroll.setWidget(self.exam_check_group)
        self.exam_check_scroll.setWidgetResizable(True)
        self.exam_check_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )

        self.right_board_layout.addWidget(self.exam_check_scroll)

    def check_proceed_slot(self):
        try:
            username = self.exam_teacher_check_username.text()
            password = self.exam_teacher_check_password.text()
            if (len(username) and len(password)) != 0:
                from Projects.SchoolManagement.DataBaseTool import DataBase

                teachers = DataBase.get_teacher('username')
                if username in teachers:
                    user_passwords = DataBase.get_teacher('password')
                    if password == user_passwords[teachers.index(username)]:
                        msg = 'Login successful!!!'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)

                        self.exam_check_scroll.setHidden(True)
                        self.exam_check_scroll.setEnabled(False)

                        self.next_page = ExamCheck()
                        self.right_board_layout.addWidget(self.next_page)
                    else:
                        msg = 'Login failed, Invalid Username or Password.'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
            else:
                msg = 'Please fill in your username and password for proper identification.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e

    def examCHECKRESULTS(self):
        self.form_size = (300, 40)

        self.user_scroll.setHidden(True)
        self.user_scroll.setEnabled(False)

        self.exam_check_layout = QGridLayout()
        self.exam_check_layout.setContentsMargins(0, 0, 0, 0)
        self.exam_check_layout.setAlignment(Qt.AlignCenter)

        self.title_check_layout = QVBoxLayout()
        self.title_check_layout.setContentsMargins(0, 0, 0, 0)
        self.title_check_layout.setAlignment(Qt.AlignCenter)
        self.exam_check_layout.addLayout(self.title_check_layout, 0, 0)

        self.form_title = QLabel('Login')
        self.form_title.setAlignment(Qt.AlignCenter)
        self.form_title.setMaximumSize(self.form_size[0], 40)
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
        self.title_check_layout.addWidget(self.form_title)

        self.exam_teacher_check_username = QLineEdit()
        self.exam_teacher_check_username.setPlaceholderText('Username')
        self.exam_teacher_check_username.setStyleSheet(
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
        self.exam_teacher_check_username.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_username, 1, 0)

        self.exam_teacher_check_password = QLineEdit()
        self.exam_teacher_check_password.setEchoMode(QLineEdit.Password)
        self.exam_teacher_check_password.setPlaceholderText('Password')
        self.exam_teacher_check_password.setStyleSheet(
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
        self.exam_teacher_check_password.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_password, 2, 0)

        self.proceed_check = QPushButton('Proceed')
        self.proceed_check.clicked.connect(self.check_form_slot)
        self.proceed_check.setFixedSize(self.form_size[0], 30)
        self.proceed_check.setStyleSheet(
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
        self.exam_check_layout.addWidget(self.proceed_check, 3, 0)

        self.exam_check_group = QGroupBox('Exam: Check Results')
        self.exam_check_group.setMaximumWidth(1500)
        self.exam_check_group.setContentsMargins(0, 0, 0, 0)
        self.exam_check_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.exam_check_group.setLayout(self.exam_check_layout)

        self.exam_check_scroll = QScrollArea()
        self.exam_check_scroll.setWidget(self.exam_check_group)
        self.exam_check_scroll.setWidgetResizable(True)
        self.exam_check_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )

        self.right_board_layout.addWidget(self.exam_check_scroll)

    def check_form_slot(self):
        try:
            username = self.exam_teacher_check_username.text()
            password = self.exam_teacher_check_password.text()
            if (len(username) and len(password)) != 0:
                from Projects.SchoolManagement.DataBaseTool import DataBase

                teachers = DataBase.get_teacher('username')
                if username in teachers:
                    user_passwords = DataBase.get_teacher('password')
                    if password == user_passwords[teachers.index(username)]:
                        msg = 'Login successful!!!'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)

                        self.exam_check_scroll.setHidden(True)
                        self.exam_check_scroll.setEnabled(False)

                        self.next_page = ExamCheckResult()
                        self.right_board_layout.addWidget(self.next_page)
                    else:
                        msg = 'Login failed, Invalid Username or Password.'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                else:
                    msg = 'Login failed, Invalid Username or Password.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            else:
                msg = 'Please fill in your username and password for proper identification.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e

    def examSTART(self):
        self.form_size = (300, 40)

        self.user_scroll.setHidden(True)
        self.user_scroll.setEnabled(False)

        self.exam_check_layout = QGridLayout()
        self.exam_check_layout.setContentsMargins(0, 0, 0, 0)
        self.exam_check_layout.setAlignment(Qt.AlignCenter)

        self.title_check_layout = QVBoxLayout()
        self.title_check_layout.setContentsMargins(0, 0, 0, 0)
        self.title_check_layout.setAlignment(Qt.AlignCenter)
        self.exam_check_layout.addLayout(self.title_check_layout, 0, 0)

        self.form_title = QLabel('Exam Login')
        self.form_title.setAlignment(Qt.AlignCenter)
        self.form_title.setMaximumSize(self.form_size[0], 40)
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
        self.title_check_layout.addWidget(self.form_title)

        self.exam_teacher_check_username = QLineEdit()
        self.exam_teacher_check_username.setPlaceholderText('Reg Number')
        self.exam_teacher_check_username.setStyleSheet(
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
        self.exam_teacher_check_username.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_username, 1, 0)

        self.exam_teacher_check_password = QLineEdit()
        self.exam_teacher_check_password.setEchoMode(QLineEdit.Password)
        self.exam_teacher_check_password.setPlaceholderText('PIN')
        self.exam_teacher_check_password.setStyleSheet(
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
        self.exam_teacher_check_password.setMaximumSize(self.form_size[0], 30)
        self.exam_check_layout.addWidget(
            self.exam_teacher_check_password, 2, 0)

        self.proceed_check = QPushButton('Login')
        self.proceed_check.clicked.connect(self.check_start_slot)
        self.proceed_check.setFixedSize(self.form_size[0], 30)
        self.proceed_check.setStyleSheet(
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
        self.exam_check_layout.addWidget(self.proceed_check, 3, 0)

        self.exam_check_group = QGroupBox('Exam: Start Exams')
        self.exam_check_group.setContentsMargins(0, 0, 0, 0)
        self.exam_check_group.setStyleSheet(
            '''
            QGroupBox {
                border: 3px solid rgb(240, 210, 190);
                border-top: 30px solid rgb(240, 210, 190);
                background-color: rgb(250, 215, 200); 
                font-size: 17px;
                }
            '''
        )
        self.exam_check_group.setLayout(self.exam_check_layout)

        self.exam_check_scroll = QScrollArea()
        self.exam_check_scroll.setWidget(self.exam_check_group)
        self.exam_check_scroll.setWidgetResizable(True)
        self.exam_check_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                padding: 0px;
                }
            '''
        )

        self.right_board_layout.addWidget(self.exam_check_scroll)

    def exam_mode(self):
        self.left_scroll.setHidden(True)
        self.left_scroll.setEnabled(False)

        self.top_right_bar_group.setHidden(True)
        self.top_right_bar_group.setEnabled(False)

        self.showFullScreen()

    def check_start_slot(self):
        self.submitSEQ = GetQuestions(30)
        self.submitSEQ.countChanged.connect(self.check_start_signal)
        self.submitSEQ.run()

    def check_start_signal(self):
        try:
            reg_num = self.exam_teacher_check_username.text()
            pin = self.exam_teacher_check_password.text()
            if (len(reg_num) and len(pin)) != 0:
                from Projects.SchoolManagement.DataBaseTool import DataBase
                import time

                all_reg_nums = DataBase.get_students_by_column('reg_num')
                all_pins = DataBase.get_students_by_column('pin')
                all_classes = DataBase.get_students_by_column('class')

                if reg_num in all_reg_nums:
                    database_pin = all_pins[all_reg_nums.index(reg_num)]
                    if pin == database_pin:
                        class_ = all_classes[all_reg_nums.index(reg_num)]
                        class_id = DataBase.get_class_id(class_)
                        self.all_class_avail_questions = DataBase.get_school_questions_avail(
                            class_)

                        for exam in self.all_class_avail_questions:
                            subject = DataBase.get_school_questions_by_cs(class_, exam)[
                                0][2]
                            teacher = DataBase.get_school_questions_by_cs(class_, exam)[
                                0][3]
                            schedule_time = DataBase.get_school_questions_by_cs(class_, exam)[
                                0][4]
                            time_allocated = DataBase.get_school_questions_by_cs(class_, exam)[
                                0][5]
                            availability = DataBase.get_school_questions_by_cs(class_, exam)[
                                0][6]

                            print(subject, schedule_time, availability)
                            self.next_page = ExamStart(
                                reg_num, class_, subject, teacher, time_allocated, self.left_scroll, self.top_right_bar_group, self, self.examSTART)

                            if availability == 'True':
                                clock = time.gmtime()

                                year = int(str(clock.tm_year)[2:])
                                month = clock.tm_mon
                                day = clock.tm_mday
                                hour = clock.tm_hour + 1
                                minute = clock.tm_min

                                schedule_time_split = schedule_time.split('/')
                                st_month = int(schedule_time_split[0])
                                st_day = int(schedule_time_split[1]) - 1

                                # schedule_time_split = schedule_time_split[0].split(' ')

                                schedule_time_split = schedule_time.split('/')
                                st_year = int(
                                    schedule_time_split[-1].split(' ')[0])

                                st_hour = int(
                                    schedule_time_split[-1].split(' ')[1].split(':')[0])
                                if st_hour < 12:
                                    st_hour += 12
                                else:
                                    st_hour = int(st_hour)
                                st_min = int(
                                    schedule_time_split[-1].split(' ')[1].split(':')[1])
                                st_meridian = schedule_time_split[-1].split(
                                    ' ')[-1]

                                self.student_exam_status = DataBase.get_student_exam_status_by(
                                    class_, reg_num, subject)
                                print(self.student_exam_status)
                                if len(self.student_exam_status) != 0:
                                    if self.student_exam_status[0][-1] == 'False':
                                        print((year, st_year),
                                              (month, st_month), (day, st_day))
                                        if (
                                            (year >= st_year) and
                                            (month >= st_month) and
                                            (day >= st_day)
                                        ):
                                            self.exam_check_scroll.setHidden(
                                                True)
                                            self.exam_check_scroll.setEnabled(
                                                False)

                                            msg = f'''You\'re exam about to begin {subject} Exam.\n Avoid any form of maltpractice, Good luck {reg_num}. \n \n- Invigilator'''
                                            message_box = QMessageBox()
                                            message_box.about(
                                                self, self.school_name, msg)

                                            DataBase.insert_student_exam_status(
                                                class_, reg_num, subject, '0 %', 'True')

                                            self.right_board_layout.addWidget(
                                                self.next_page)
                                            self.exam_mode()
                                            break
                                        else:
                                            msg = 'Your exam isn\'t ready yet.\n Please check back later.'
                                            message_box = QMessageBox()
                                            message_box.about(
                                                self, self.school_name, msg)
                                    else:
                                        msg = f'{subject} Exam is not available for {reg_num}. \nContact Exam Invigilator for more information on this.'
                                        message_box = QMessageBox()
                                        message_box.about(
                                            self, 'Exam Manager', msg)
                                else:
                                    DataBase.insert_student_exam_status(
                                        class_, reg_num, subject, '0 %', 'False')
                                    if (
                                        (year >= st_year) and
                                        (month >= st_month) and
                                        (day >= st_day)
                                    ):
                                        self.exam_check_scroll.setHidden(True)
                                        self.exam_check_scroll.setEnabled(
                                            False)

                                        msg = f'''You\'re exam about to begin {subject} Exam.\n Avoid any form of maltpractice, Good luck {reg_num}. \n \n- Invigilator'''
                                        message_box = QMessageBox()
                                        message_box.about(
                                            self, self.school_name, msg)

                                        DataBase.insert_student_exam_status(
                                            class_, reg_num, subject, '0 %', 'True')

                                        self.right_board_layout.addWidget(
                                            self.next_page)
                                        self.exam_mode()
                                        break
                                    else:
                                        msg = 'Your exam isn\'t ready yet.\n Please check back later.'
                                        message_box = QMessageBox()
                                        message_box.about(
                                            self, self.school_name, msg)
                            else:
                                msg = 'Your exam isn\'t ready yet.\n Please check back later.'
                                message_box = QMessageBox()
                                message_box.about(self, self.school_name, msg)
                    else:
                        msg = 'Invalid credentials.\n please check your credentials and try again.'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                else:
                    msg = 'Invalid credentials.\n please check your credentials and try again.'
                    message_box = QMessageBox()
                    message_box.about(self, self.school_name, msg)
            else:
                msg = 'Please fill in your username and password for proper identification.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            raise e


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     manager = Exam()
#     manager.show()
#     sys.exit(app.exec_())

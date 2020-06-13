from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


class TableDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.table_layout = QGridLayout()
        self.table_layout.setSpacing(0)
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)

        self.table_height = 300

        self.setMaximumHeight(self.table_height - 200)
        self.setLayout(self.table_layout)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid black;
                border-left: 1px solid black;
                border-right: 1px solid black;
                border-bottom: none;
            }
            '''
        )

        self.initialization()

    def initialization(self):
        self.subject = QLabel('Subject')
        self.subject.setFixedWidth(350)
        self.subject.setAlignment(Qt.AlignLeft)
        self.subject.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                font: Verdana;
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 0px;
                border-right: 0px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject, 0, 0)

        self.exam_size = (300, self.table_height)

        self.ca1 = QLabel('C.A. (20 %)')
        self.ca1.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.ca1.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.ca1.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.ca1, 0, 1)

        self.ca2 = QLabel('C.A. (20 %)')
        self.ca2.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.ca2.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.ca2.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.ca2, 0, 2)

        self.exam = QLabel('Exam (60 %)')
        self.exam.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.exam.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.exam.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.exam, 0, 3)

        self.total = QLabel('Total (100 %)')
        self.total.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.total.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.total.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.total, 0, 4)

        self.grade = QLabel('Grade')
        self.grade.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.grade.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.grade.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.grade, 0, 5)

        self.position_ = QLabel('Position')
        self.position_.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
            }
            '''
        )
        self.position_.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.position_.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.position_, 0, 6)

        self.t_students = QLabel('No. of Students')
        self.t_students.setStyleSheet(
            '''
            QLabel { 
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.t_students.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.t_students.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.t_students, 0, 7)

        self.class_avg = QLabel('Class Average')
        self.class_avg.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.class_avg.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.class_avg.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.class_avg, 0, 8)

        self.remarks = QLabel('Remarks')
        self.remarks.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-right: 0px;
                border-left: 1px solid black;
                }
            '''
        )
        self.remarks.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.remarks.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.remarks, 0, 9)


class Table(QGroupBox):
    def __init__(self, subject_name='Subject', scores=[20, 20, 60], position_val='1', class_avg_val='55'):
        QGroupBox.__init__(self)

        self.subject_name = subject_name
        self.ca1_score = scores[0]
        self.ca2_score = scores[1]
        self.exam_score = scores[2]
        self.position_val = position_val
        self.class_avg_val = class_avg_val

        self.table_layout = QGridLayout()
        self.table_layout.setSpacing(0)
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setAlignment(Qt.AlignTop)

        self.table_height = 300

        self.setMaximumHeight(self.table_height - 200)
        self.setLayout(self.table_layout)
        self.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid black;
                border-left: 1px solid black;
                border-right: 1px solid black;
                border-bottom: none;
            }
            '''
        )

        self.initialization()
        
        # self.subject_name
        # self.ca1_score
        # self.ca2_score
        # self.exam_sccore
        # self.position_val
        # self.total_students
        # self.class_avg_val

    def initialization(self):
        self.subject = QLabel(self.subject_name)
        self.subject.setFixedWidth(350)
        self.subject.setAlignment(Qt.AlignLeft)
        self.subject.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 13px;
                font: Verdana;
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 0px;
                border-right: 0px;
            }
            '''
        )
        self.table_layout.addWidget(self.subject, 0, 0)

        self.exam_size = (300, self.table_height)

        self.ca1 = QLineEdit()
        self.ca1.setText(str(self.ca1_score))
        self.ca1.setStyleSheet(
            '''
            QLineEdit {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.ca1.setMaximumSize((self.exam_size[0] - 90) // 2, self.exam_size[1])
        self.ca1.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.ca1, 0, 1)

        self.ca2 = QLineEdit()
        self.ca2.setText(str(self.ca2_score))
        self.ca2.setStyleSheet(
            '''
            QLineEdit {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.ca2.setMaximumSize((self.exam_size[0] - 90) // 2, self.exam_size[1])
        self.ca2.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.ca2, 0, 2)

        self.exam = QLineEdit()
        self.exam.setText(str(self.exam_score))
        self.exam.setStyleSheet(
            '''
            QLineEdit {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.exam.setMaximumSize((self.exam_size[0] - 90) // 2, self.exam_size[1])
        self.exam.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.exam, 0, 3)

        self.total = QLabel(f'{round(((self.ca1_score + self.ca2_score + self.exam_score) / 100) * 100, 2)}  %')
        self.total.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.total.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.total.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.total, 0, 4)

        self.grade = QLabel('A1')
        self.grade.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.grade.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.grade.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.grade, 0, 5)

        self.position_ = QLabel(self.position_val)
        self.position_.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
            }
            '''
        )
        self.position_.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.position_.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.position_, 0, 6)

        self.t_students = QLabel('27')
        self.t_students.setStyleSheet(
            '''
            QLabel { 
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.t_students.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.t_students.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.t_students, 0, 7)

        self.class_avg = QLabel('90 %')
        self.class_avg.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 0px;
                }
            '''
        )
        self.class_avg.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.class_avg.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.class_avg, 0, 8)

        self.remarks = QLabel('Excellent')
        self.remarks.setStyleSheet(
            '''
            QLabel {
                border-top: 0px;
                border-bottom: 1px solid black;
                border-right: 0px;
                border-left: 1px solid black;
                }
            '''
        )
        self.remarks.setMaximumSize(self.exam_size[0], self.exam_size[1])
        self.remarks.setAlignment(Qt.AlignCenter)
        self.table_layout.addWidget(self.remarks, 0, 9)


class StudentReportAVG(QDialog):
    def __init__(self, reg_num):
        QDialog.__init__(self)

        self.reg_num = reg_num

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.showOFF()

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.dialog_layout.setSpacing(0)
        self.dialog_layout.setAlignment(Qt.AlignTop)

        self.dialog_group = QGroupBox()
        self.dialog_group.setLayout(self.dialog_layout)
        self.dialog_group.setStyleSheet(
            '''
            QGroupBox {
                border-top: 1px solid black;
                padding-top: 20px;
                padding-left: 15px;
                padding-right: 15px;
                padding-right: 15px;
            }
            '''
        )

        self.dialog_scroll = QScrollArea()
        self.dialog_scroll.setWidget(self.dialog_group)
        self.dialog_scroll.setWidgetResizable(True)
        self.dialog_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
            }
            '''
        )

        self.main_layout.addWidget(self.dialog_scroll)

        self.setStyleSheet(
            '''
            QDialog {
                background-color: 0px;
            }
            '''
        )
        self.setLayout(self.main_layout)

        self.initialization()
        self.showMaximized()

    def initialization(self):
        self.getSTUDENT()
        self.heading()
        self.topLAYOUT()
        self.resultTABLE()
        self.studentSUMMARY()
        self.extraSUMMARY()
        self.managementCOMMENTS()

    def getSTUDENT(self):
        try:
            from Projects.SchoolManagement.DataBaseTool import DataBase

            self.student_details = DataBase.get_school_students_by_id(
                DataBase.get_students_by_column('id')[
                    DataBase.get_students_by_column('reg_num').index(self.reg_num)
                ]
            )

            self.id_ = self.student_details[0]
            self.sur_name = self.student_details[1]
            self.f_name = self.student_details[2]
            self.l_name = self.student_details[3]
            self.class_ = self.student_details[4]
            self.reg_num = self.student_details[5]
            self.gender = self.student_details[6]
            self.pin = self.student_details[7]

            print(self.student_details)
        except Exception as e:
            raise e

    def showOFF(self):
    	self.show_layout = QHBoxLayout()
    	self.show_layout.setAlignment(Qt.AlignLeft)
    	self.show_layout.setSpacing(0)
    	self.show_layout.setContentsMargins(0, 0, 0, 0)

    	self.developers_label = QLabel('A.S. Tech School Management System (S.M.S.)')
    	self.developers_label.setMaximumHeight(40)
    	self.developers_label.setStyleSheet(
    		'''
    		QLabel {
    			padding: 5px;
    			font: Verdana;
    			font-size: 13px;
    			border-bottom: 1px solid black;
    		}
    		'''
    	)

    	self.show_layout.addWidget(self.developers_label)

    	self.main_layout.addLayout(self.show_layout)

    # school logo, school name, school address, result title, student image
    def heading(self):
        self.heading_layout = QHBoxLayout()
        self.heading_layout.setSpacing(5)
        self.heading_layout.setAlignment(Qt.AlignCenter)

        self.heading_group = QGroupBox()
        self.heading_group.setMaximumHeight(170)
        self.heading_group.setLayout(self.heading_layout)
        self.heading_group.setStyleSheet(
        	'''
        	QGroupBox {
        		border-bottom: 1px solid black;
        	}
        	'''
        )

        self.dialog_layout.addWidget(self.heading_group)

        self.headingLOGO()
        self.pageTITLE()

    def headingLOGO(self):
    	self.logo_layout = QVBoxLayout()
    	self.logo_layout.setAlignment(Qt.AlignCenter)
    	self.logo_layout.setContentsMargins(0, 0, 0, 0)
    	self.logo_layout.setSpacing(0)

    	self.file_name = f'Icons/005-science.png'
    	sized = cv2.resize(cv2.imread(self.file_name), (230, 120))
    	self.file_name_read = cv2.imwrite(self.file_name + 'temp.png', sized)
    	self.logo_file = QPixmap(self.file_name + 'temp.png')

    	self.logo = QLabel()
    	self.logo.setStyleSheet(
    		'''
    		QLabel {
    			padding: 0px;
    		}
    		'''
    	)
    	self.logo.setMaximumSize(400, 400)
    	self.logo.setPixmap(self.logo_file)
    	self.logo.setAlignment(Qt.AlignCenter)
    	self.logo_layout.addWidget(self.logo)

    	self.heading_layout.addLayout(self.logo_layout)

    def pageTITLE(self):
    	self.title_layout = QVBoxLayout()
    	self.title_layout.setSpacing(5)
    	self.title_layout.setContentsMargins(0, 0, 0, 0)
    	self.title_layout.setAlignment(Qt.AlignCenter)

    	self.school_name = QLabel('School name')
    	self.school_name.setFixedWidth(500)
    	self.school_name.setAlignment(Qt.AlignCenter)
    	self.school_name.setStyleSheet(
    		'''
    		QLabel {
    			font-size: 20px;
    			font-weight: bold;
    			font: Verdana;
    		}
    		'''
    	)
    	self.title_layout.addWidget(self.school_name)	

    	self.school_address = QLabel('School address')
    	self.school_address.setMaximumWidth(700)
    	self.school_address.setAlignment(Qt.AlignCenter)
    	self.school_address.setStyleSheet(
    		'''
    		QLabel {
    			font-size: 15px;
    			font: Verdana;
    		}
    		'''
    	)
    	self.school_address.setMaximumHeight(60)
    	self.title_layout.addWidget(self.school_address)

    	self.spacer_height = 30

    	self.spacer_item = QLabel()
    	self.spacer_item.setFixedHeight(self.spacer_height)
    	self.title_layout.addWidget(self.spacer_item)

    	self.school_report_title = QLabel('School report')
    	self.school_address.setFixedWidth(500)
    	self.school_report_title.setAlignment(Qt.AlignCenter)
    	self.school_report_title.setStyleSheet(
    		'''
    		QLabel {
    			font-size: 17px;
    			font: Verdana;
    		}
    		'''
    	)
    	self.title_layout.addWidget(self.school_report_title)

    	self.title_layout.addWidget(self.spacer_item)

    	self.title_group = QGroupBox()
    	self.title_group.setLayout(self.title_layout)
    	self.title_group.setStyleSheet(
    		'''
    		QGroupBox {
    			border: 0px;
    		}
    		'''
    	)

    	self.heading_layout.addWidget(self.title_group)

    	self.student_image_layout = QVBoxLayout()
    	self.student_image_layout.setAlignment(Qt.AlignCenter)
    	self.student_image_layout.setSpacing(0)
    	self.student_image_layout.setContentsMargins(0, 0, 0, 0)

    	self.student_image_file = 'Icons/013-diploma.png'
    	sized = cv2.resize(cv2.imread(self.student_image_file), (230, 120))
    	# self.student_image_file_read = cv2.imwrite(self.student_image_file + 'temp.png', self.student_image_file)
    	self.student_image_file = QPixmap(self.student_image_file)

    	self.student_image = QLabel()
    	self.student_image.setStyleSheet(
    		'''
    		QLabel {
    			padding: 0px;
    		}
    		'''
    	)
    	self.student_image.setMaximumSize(400, 400)
    	self.student_image.setPixmap(self.student_image_file)
    	self.student_image.setAlignment(Qt.AlignCenter)

    	self.student_image_layout.addWidget(self.student_image)

    	self.student_image_group = QGroupBox()
    	self.student_image_group.setMaximumWidth(400)
    	self.student_image_group.setLayout(self.student_image_layout)
    	self.student_image_group.setStyleSheet(
    		'''
    		QGroupBox {
    			border: 0px;
    		}
    		'''
    	)

    	self.heading_layout.addWidget(self.student_image_group)


    # student name, class, term/semester, total students in class, student's average
    def topLAYOUT(self):
        self.top_layout = QGridLayout()
        self.top_layout.setSpacing(3)
        self.top_layout.setAlignment(Qt.AlignLeft)

        self.name_height = 50

        self.student_label = QLabel('NAME : ')
        self.student_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 15px;
                font: Verdana;
            }
            '''
        )
        self.student_label.setMaximumSize(150, self.name_height)
        self.top_layout.addWidget(self.student_label, 0, 0)

        self.student_box = QLabel('Idris Elba')
        self.student_box.setMaximumSize(350, self.name_height)
        self.top_layout.addWidget(self.student_box, 0, 1)
        
        self.class_label = QLabel('CLASS : ')
        self.class_label.setStyleSheet(
            '''
            QLabel {
                font-weight: bold;
                font-size: 15px;
                font: Verdana;
            }
            '''
        )
        self.class_label.setMaximumSize(150, self.name_height)
        self.top_layout.addWidget(self.class_label, 1, 0)

        self.class_box = QLabel('AdvancedLevel')
        self.class_box.setMaximumSize(350, self.name_height)
        self.top_layout.addWidget(self.class_box, 1, 1)

        self.top_group = QGroupBox()
        self.top_group.setLayout(self.top_layout)
        self.top_group.setMaximumHeight(80)
        self.top_group.setStyleSheet(
            '''
            QGroupBox {
                border: none;
            }
            '''
        )

        self.dialog_layout.addWidget(self.top_group)

    # subject, 1st C.A.(20 %), 2nd C.A.(20 %), Exam(60 %), Total (100 %)
    # Grade, Position, Highest in class subject, lowest in class subject, class average, remarks
    def resultTABLE(self):
        self.result_table_layout = QVBoxLayout()
        self.result_table_layout.setSpacing(0)
        self.result_table_layout.setAlignment(Qt.AlignTop)
        self.result_table_layout.setContentsMargins(0, 0, 0, 0)

        self.result_table_layout.addWidget(TableDef())
        self.result_table_layout.addWidget(Table())
        self.result_table_layout.addWidget(Table())

        self.result_table_group = QGroupBox()
        self.result_table_group.setLayout(self.result_table_layout)
        self.result_table_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 0px;
            }
            '''
        )

        self.dialog_layout.addWidget(self.result_table_group)

    '''
        keys to grade
        Affective domain : Rating (
            Punctuality, Perseverance, Attendance, Reliability, Neatness, Politeness, Honesty, Relationship with others
        )
        Psychomotor : Rating (
            Handwriting, Games, Sports, Drawing & Painting, Crafts, Musical Skills
        )
        Keys to rating
    '''
    def studentSUMMARY(self):
        pass

    # Minimum subjects, Maximum Marks Obtainable, NUmber of Subjects Taken, Total Marks Obtained
    def extraSUMMARY(self):
        pass

    '''
        Class teacher remarks and signature
        Principal's comment
        Next session begins 
    '''
    def managementCOMMENTS(self):
        pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = StudentReportAVG('2020UCI')
	window.show()
	sys.exit(app.exec_())

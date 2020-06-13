from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class AdminLoginPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.window_layout = QVBoxLayout()
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setSpacing(0)
        self.setLayout(self.window_layout)
        self.showMaximized()

        self.initialization()

    def initialization(self):
        self.database = False
        try:
            from Projects.SchoolManagement.DataBaseTool.DataBase import get_school, get_school_logo

            self.school_name = get_school()
            self.school_logo = get_school_logo()

            self.setWindowTitle(self.school_name)

            self.database = True
        except Exception as e:
            self.school_name = 'SMS'
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'School Manager', msg)

        self.create_main_layout()

    def create_main_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_group = QGroupBox()
        self.main_group.setAlignment(Qt.AlignCenter)
        self.main_group.setContentsMargins(0, 0, 0, 0)
        self.main_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 0px;
                background-image: url(bg2.jpg);
                background-repeat: no-repeat;
                background-position: center;
                }
            '''
        )
        self.main_group.setLayout(self.main_layout)

        self.window_layout.addWidget(self.main_group)

        self.adminFORM()
        self.adminLOGIN()

    def adminFORM(self):
        self.admin_username = QLineEdit()
        self.admin_pass = QLineEdit()

    def adminLOGIN(self):
        self.login_layout = QVBoxLayout()
        self.login_layout.setAlignment(Qt.AlignCenter)
        # self.login_layout.setAlignment(Qt.AlignRight)
        # self.login_layout.setContentsMargins(0, 0, 0, 0)
        # self.login_layout.setSpacing(0)

        self.login_group = QGroupBox()
        self.login_group.setAlignment(Qt.AlignCenter)
        self.login_group.setContentsMargins(0, 0, 0, 0)
        self.login_group.setLayout(self.login_layout)
        self.login_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                padding: 0px;
                background-image: url(bg2.jpg);
                background-repeat: no-repeat;
                background-position: center;
                }
            '''
        )

        self.title_layout = QHBoxLayout()
        self.title_layout.setAlignment(Qt.AlignCenter)

        self.login_layout.addLayout(self.title_layout)

        self.title = f'{self.school_name} : Admin Login'

        self.form_title = QLabel(self.title)
        self.form_title.setMaximumSize(700, 50)
        self.form_title.setAlignment(Qt.AlignCenter)
        self.form_title.setWordWrap(True)
        self.form_title.setStyleSheet(
            '''
            QLabel {
                padding: 5px;
                background-color: #ff9933;
                font-family: Verdana;
                font-weight: bold;
                font-size: 17px;
                text-align: center;
                color: white;
                }
            '''
        )
        self.main_layout.addWidget(self.form_title)

        self.image_width = 300
        self.image_height = 300
        self.name_size = (170, 30)

        self.admin_layout = QVBoxLayout()
        self.admin_layout.setAlignment(Qt.AlignCenter)
        self.login_layout.addLayout(self.admin_layout)

        self.admin_username.setPlaceholderText('Username')
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

        self.admin_pass.setPlaceholderText('Password')
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

        self.login_layout.addWidget(self.spacing)

        self.last_layout = QHBoxLayout()
        self.last_layout.setAlignment(Qt.AlignCenter)
        self.last_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.addLayout(self.last_layout)

        self.login_button_size = (150, 30)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login_slot)
        self.login_button.setFixedSize(self.login_button_size[0], self.login_button_size[1])
        self.login_button.setStyleSheet(
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
        self.last_layout.addWidget(self.login_button)

        self.login_scroll = QScrollArea()
        self.login_scroll.setAlignment(Qt.AlignCenter)
        self.login_scroll.setMaximumSize(700, 500)
        self.login_scroll.setWidgetResizable(True)
        self.login_scroll.setWidget(self.login_group)
        self.login_scroll.setStyleSheet(
            '''
            QScrollArea {
                border: 0px;
                }
            '''
        )

        self.main_layout.addWidget(self.login_scroll)

    def login_slot(self):
        admin_username = self.admin_username.text()
        admin_password = self.admin_pass.text()
        try:
            if len(admin_username) and len(admin_password) != 0:
                from Projects.SchoolManagement.DataBaseTool.DataBase import get_admin, get_admin_image
                from Projects.SchoolManagement.HomePages.HomePage import HomePage as Page

                auth = get_admin()
                # image = get_admin_image()
                for person in auth:
                    username = person[4]
                    password = person[5]
                    if admin_username == username:
                        if admin_password == password:
                            page = Page(self.school_name, person[1], person[2])

                            self.main_group.setHidden(True)
                            self.main_group.setEnabled(False)

                            self.window_layout.addWidget(page)
                            msg = 'Login successful!'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)
                            break
                        else:
                            msg = 'Incorrect password!'
                            message_box = QMessageBox()
                            message_box.about(self, self.school_name, msg)
                            break
                    else:
                        msg = 'User does not exist!'
                        message_box = QMessageBox()
                        message_box.about(self, self.school_name, msg)
                        break
            else:
                self.admin_username.setStyleSheet(
                    '''
                    QLineEdit {
                        border-radius: 1px;
                        font-size: 13px;
                        border: 1px solid red;
                        font-family: Verdana;
                        /* font-style: italic; */
                        padding: 5px;
                    }
                    '''
                )
                self.admin_pass.setStyleSheet(
                    '''
                    QLineEdit {
                        border-radius: 1px;
                        font-size: 13px;
                        border: 1px solid red;
                        font-family: Verdana;
                        /* font-style: italic; */
                        padding: 5px;
                    }
                    '''
                )
                msg = 'Please enter a valid username and password.'
                message_box = QMessageBox()
                message_box.about(self, self.school_name, msg)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, self.school_name, msg)


if __name__ == '__main__':
    app = ApplicationContext()
    manager = AdminLoginPage()
    manager.show()
    exit_code = app.app.exec_()
    sys.exit(exit_code)

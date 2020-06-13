from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import cv2


class SchoolRegistration(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('School Management System')
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.window_layout)

        self.initialization()

    def initialization(self):
        self.main_layout()

    def main_layout(self):
        self.main_group_layout = QVBoxLayout()
        self.main_group_layout.setContentsMargins(0, 50, 0, 0)
        self.main_group_layout.setAlignment(Qt.AlignTop)
        self.main_group_layout.setAlignment(Qt.AlignHCenter)

        self.form_title = QLabel('SMS: School Registration')
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
        self.main_group_layout.addWidget(self.form_title)

        self.main_group = QGroupBox()
        self.main_group.setFixedSize(750, 550)
        self.main_group.setStyleSheet(
            '''
            QGroupBox {
                border: 0px;
                background-color: #223335;
                background-image: url(bg2.jpg);
                }
            '''
        )
        self.main_group.setContentsMargins(0, 0, 0, 0)
        self.main_group.setLayout(self.main_group_layout)

        self.window_layout.addWidget(self.main_group)

        self.form_layout()

    def form_layout(self):
        self.form_grid = QGridLayout()
        self.form_grid.setAlignment(Qt.AlignTop)

        self.image_width = 200
        self.image_height = 100

        self.school_image = QLabel('Complete the registration to add image')
        self.school_image.setAlignment(Qt.AlignCenter)
        # self.school_image.setStyleSheet(
        #     '''
        #     QLabel {
        #         background-color: white;
        #         border: 2px solid black;
        #         }
        #     '''
        # )
        self.school_image.setFixedSize(self.image_width, self.image_height)
        self.form_grid.addWidget(self.school_image, 0, 1)

        school_name = QLabel('School name')
        school_name.setAlignment(Qt.AlignCenter)
        school_name.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(school_name, 3, 1)

        self.school_name = QLineEdit()
        self.school_name.setFixedWidth(200)
        self.school_name.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.school_name, 4, 1)

        surname = QLabel('Surname')
        surname.setAlignment(Qt.AlignCenter)
        surname.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(surname, 5, 0)

        self.surname = QLineEdit()
        self.surname.setFixedWidth(200)
        self.surname.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.surname, 6, 0)

        first_name = QLabel('First name')
        first_name.setAlignment(Qt.AlignCenter)
        first_name.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(first_name, 5, 1)

        self.first_name = QLineEdit()
        self.first_name.setFixedWidth(200)
        self.first_name.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.first_name, 6, 1)

        last_name = QLabel('Last name')
        last_name.setAlignment(Qt.AlignCenter)
        last_name.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(last_name, 5, 2)

        self.last_name = QLineEdit()
        self.last_name.setFixedWidth(200)
        self.last_name.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.last_name, 6, 2)

        new_password = QLabel('New Password')
        new_password.setAlignment(Qt.AlignCenter)
        new_password.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(new_password, 7, 0)

        self.new_password = QLineEdit()
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setFixedWidth(200)
        self.new_password.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.new_password, 8, 0)

        username = QLabel('Username')
        username.setAlignment(Qt.AlignCenter)
        username.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(username, 7, 1)

        self.username = QLineEdit()
        self.username.setFixedWidth(200)
        self.username.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.username, 8, 1)

        confirm_password = QLabel('Confirm Password')
        confirm_password.setAlignment(Qt.AlignCenter)
        confirm_password.setStyleSheet(
            '''
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(confirm_password, 7, 2)

        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setFixedWidth(200)
        self.confirm_password.setStyleSheet(
            '''
            QLineEdit {
                padding: 3px;
                border-radius: 3px;
                color: black;
                font-size: 15px;
                }
            '''
        )
        self.form_grid.addWidget(self.confirm_password, 8, 2)

        self.select_image = QPushButton('Choose image')
        self.select_image.setStyleSheet(
            '''
            QPushButton {
                background-color: green;
                color: white;
                border: 0px;
                font-size: 13px;
                font-weight: bold
                }
            '''
        )
        self.select_image.setFixedSize(200, 25)
        self.select_image.clicked.connect(self.select_image_dialog)
        self.form_grid.addWidget(self.select_image, 1, 1)

        pseudo = QLabel()
        pseudo.setFixedHeight(30)
        self.form_grid.addWidget(pseudo, 9, 1)

        self.register = QPushButton('Register')
        self.register.clicked.connect(self.register_slot)
        self.register.setFixedSize(200, 35)
        self.register.setStyleSheet(
            '''
            QPushButton {
                font-weight: bold;
                font-size: 13px;
                border-radius: 3px;
                color: white;
                background-color: #00DD00;
                }
            '''
        )
        self.form_grid.addWidget(self.register, 10, 1)

        self.main_group_layout.addLayout(self.form_grid)

        self.image_path = ''

    def register_slot(self):
        try:
            school_name = self.school_name.text()
            admin_s_name = self.surname.text()
            admin_f_name = self.first_name.text()
            admin_l_name = self.last_name.text()
            admin_username = self.username.text()
            new_pass = self.new_password.text()
            confirm_pass = self.confirm_password.text()

            if len(school_name) != 0:
                if (len(admin_f_name) or len(admin_l_name) and len(admin_s_name)) != 0:
                    if (len(admin_username) and len(new_pass) and len(confirm_pass)) != 0:
                        if new_pass == confirm_pass:
                            try:
                                from Projects.SchoolManagement.HomePages.HomePage import HomePage as Page
                                from Projects.SchoolManagement.DataBaseTool.DataBase import create_school, insert_school, create_admin, insert_admin, create_server_db

                                create_school(school_name)
                                insert_school(school_name)
                                create_server_db(school_name)
                                create_admin()
                                if len(self.image_path) != 0:
                                    insert_admin(0, admin_s_name, admin_f_name, admin_l_name, admin_username, confirm_pass, self.image_path)
                                else:
                                    insert_admin(0, admin_s_name, admin_f_name, admin_l_name, admin_username, confirm_pass)

                                self.main_group.setHidden(True)
                                self.main_group.setEnabled(False)
                                self.setWindowTitle(school_name)

                                page = Page(school_name, admin_s_name, admin_f_name)
                                self.window_layout.addWidget(page)

                                msg = f'You have registered \n {school_name} \n With admin {admin_s_name} {admin_f_name} {admin_l_name}'
                                message_box = QMessageBox()
                                message_box.about(self, 'School Manager', msg)
                            except Exception as e:
                                raise e
                        else:
                            msg = f'Incorrect password.'
                            message_box = QMessageBox()
                            message_box.about(self, 'School Manager', msg)
                    else:
                        msg = f'Please fill the admin username and password.'
                        message_box = QMessageBox()
                        message_box.about(self, 'School Manager', msg)
                else:
                    msg = f'Fill the Admin details too.'
                    message_box = QMessageBox()
                    message_box.about(self, 'School Manager', msg)
            else:
                msg = f'Please enter your school name.'
                message_box = QMessageBox()
                message_box.about(self, 'School Manager', msg)
        except Exception as e:
            msg = str(e)
            message_box = QMessageBox()
            message_box.about(self, 'Error!', msg)

    def select_image_dialog(self):
        self.file_dialog_window = QFileDialog.getOpenFileName(self, 'Select image', 'C\\', 'Image (*.jpg *.png *.svg)')
        self.image_path = self.file_dialog_window[0]
        img = cv2.imread(self.image_path)
        standard_width = self.school_image.width() - 10
        standard_height = self.school_image.height() - 15

        if img.shape[0] > standard_width and img.shape[1] > standard_height:
            self.reshaped_image = cv2.resize(img, (standard_width, standard_height))
            # saved image is with school name
            cv2.imwrite(f'{self.image_path}', self.reshaped_image)
            image = QPixmap(self.image_path)
            self.school_image.setPixmap(image)
        else:
            image = QPixmap(self.image_path)
            self.school_image.setPixmap(image)
            cv2.imwrite(f'{self.image_path}', cv2.imread(self.image_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SchoolRegistration()
    window.show()
    sys.exit(app.exec_())

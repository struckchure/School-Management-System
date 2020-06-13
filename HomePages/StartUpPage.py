from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

TIME_LIMIT = 100

clock = time.gmtime()


class External(QThread):

    countChanged = pyqtSignal(int)
    count = 0

    def __init__(self, time_limit=100):
        QThread.__init__(self)
        self.time_limit = time_limit

    def run(self):
        count = self.count
        while count < self.time_limit:
            count += 1
            time.sleep(1)
            self.countChanged.emit(count)

class StartUp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.window_layout)

        self.initialization()

    def initialization(self):
        self.body_layout()

    def body_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        # self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.logo_src = QPixmap('school.png')

        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        # self.logo.setFixedSize(300, 250)
        self.logo.setPixmap(self.logo_src)
        self.main_layout.addWidget(self.logo)

        self.progressBar = QProgressBar()
        self.progressBar.setFixedHeight(10)
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet(
            '''
            QProgressBar {
                text-align: center;
                font-family: Franklin Gothic;
                color: white;
                background-color: #004400;
                font-weight: bold;
                }
            '''
        )
        self.progressBar.setMaximum(10)
        self.main_layout.addWidget(self.progressBar)

        self.button = QPushButton('Sht')
        self.button.clicked.connect(self.window_size)
        self.main_layout.addWidget(self.button)

        self.button1 = QPushButton('Sht1')
        self.button1.clicked.connect(self.window_size1)
        self.main_layout.addWidget(self.button1)

        self.main_group = QGroupBox()
        self.main_group.setLayout(self.main_layout)
        # self.main_group.setContentsMargins(0, 0, 0, 0)

        self.window_layout.addWidget(self.main_group)

        self.counter()

    def window_size(self):
        self.setFixedSize(500, 500)

    def window_size1(self):
        self.setMaximumSize(1405, 700)
        self.showMaximized()

    def counter(self):
        self.calc = External(10)
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progressBar.setValue(value)


app = QApplication(sys.argv)
window = StartUp()
window.show()
sys.exit(app.exec_())

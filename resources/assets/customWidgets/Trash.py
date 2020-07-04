class SideBarUser(QGroupBox):
    def __init__(self, imagePath='resources/assets/images/icons/039-physics.png', user='John Doe'):
        super(SideBarUser, self).__init__()

        self.imagePath = imagePath
        self.user = user

        self.itemLayout = QVBoxLayout()
        self.itemLayout.setContentsMargins(0, 0, 0, 0)
        self.itemLayout.setAlignment(Qt.AlignCenter)

        qss = open('resources/assets/qss/boostrap.qss').read()

        self.setStyleSheet(qss)
        self.setLayout(self.itemLayout)
        self.setObjectName('sideBarUser')

        self.initialization()

    def initialization(self):
        # self.imageSet()
        self.userInfoSet()

    def imageSet(self):
        self.imageLayout = QVBoxLayout()
        self.imageLayout.setAlignment(Qt.AlignCenter)

        self.imagePixmap = QPixmap(self.imagePath)
        self.userImage = QLabel()
        self.userImage.setPixmap(self.imagePixmap)
        self.userImage.setAlignment(Qt.AlignCenter)
        self.userImage.setObjectName('userImage')
        self.userImage.setMaximumSize(80, 80)
        self.userImage.setStyleSheet(
            '''
                QLabel#userImage {
                    border: 2px solid #DAA5A5;
                    border-radius: 40px;
                }
            '''
        )

        self.itemLayout.addWidget(self.userImage, stretch=0, alignment=Qt.AlignCenter)

    def userInfoSet(self):
        self.infoLayout = QVBoxLayout()
        self.infoLayout.setAlignment(Qt.AlignCenter)

        self.userInfo = QLabel(self.user.get_full_name())
        self.userInfo.setAlignment(Qt.AlignLeft)
        self.userInfo.setObjectName('userInfo')
        self.userInfo.setMaximumSize(200, 50)

        self.itemLayout.addWidget(self.userInfo, stretch=0, alignment=Qt.AlignCenter)
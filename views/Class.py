from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# Custom Modules Imports

from views import utils
from resources.assets.customWidgets import customWidgets
from views import pageConfigurations
from Home import models


class AllClasses(QtWidgets.QGroupBox):
    def __init__(
        self,
        stackedWidget
        ):
        super(AllClasses, self).__init__()

        self.stackedWidget = stackedWidget

        self.groupLayout = QtWidgets.QGridLayout()
        self.groupLayout.setContentsMargins(0, 0, 0, 0)
        self.groupLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.groupLayout.setSpacing(20)

        self.pageCrumb = customWidgets.PageCrumb('Class / All Classes /')
        self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

        self.setObjectName('noBorderBox')
        self.setLayout(self.groupLayout)

        self.initialization()
    
    def initialization(self):
        pass


class AddClass(QtWidgets.QGroupBox):
    def __init__(
        self,
        stackedWidget
        ):
        super(AddClass, self).__init__()

        self.stackedWidget = stackedWidget

        self.groupLayout = QtWidgets.QGridLayout()
        self.groupLayout.setContentsMargins(0, 0, 0, 0)
        self.groupLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.groupLayout.setSpacing(20)

        self.pageCrumb = customWidgets.PageCrumb('Class / Add Class /')
        self.groupLayout.addWidget(self.pageCrumb, 0, 0, 1, 4)

        self.setObjectName('noBorderBox')
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setLayout(self.groupLayout)

        self.initialization()
    
    def initialization(self):
        self.page()
        
    def page(self):
        cardWidth = 1800
        cardHeight = 900

        self.formCard = customWidgets.CardBasic(
			accent='rgba(0, 0, 0, 0)',
			width=cardWidth,
			height=cardHeight,
		)

        self.formCardContent = customWidgets.CardContent()

        self.formCard.cardLayout.addWidget(self.formCardContent)
        self.groupLayout.addWidget(self.formCard)

        self.classForm()
            
    def classForm(self):
        all_teachers = list(models.User.objects.all().filter(is_teacher=True).values_list('username', flat=True))

        self.form = customWidgets.Form(
            fields={
                'fields': [
                    customWidgets.TextInput(
                        'Class name',
                        'SSS 1',
                        required=True
                    ),
                    customWidgets.ComboInput(
                        'Class Teacher',
                        'JD',
                        items=all_teachers,
                        required=True
                    )
                ],
                'fieldNames': [
                    'Class name',
                    'Teacher'
                ],
                'fieldGrids': [
                    (0, 0, 1, 1),
                    (0, 1, 1, 1)
                ],
                'buttonGrid': (1, 0, 1, 2),
                'buttonSize': (350, 45)
            },
            buttonText='Create',
            grid=False,
            spacing=2
        )

        self.form.onSubmit(self.submit)

        self.formCardContent.addWidget(self.form)
    
    def submit(self):
        all_classes = models.Class.objects.values_list(flat=True)
        formValues = self.form.submitEvent()

        if formValues[0] not in all_classes:
            pass
        else:
            pass

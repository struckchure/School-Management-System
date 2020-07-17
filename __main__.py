#!/usr/bin/env python3
import os
import sys


try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
except Exception as e:
    print(e)

from PyQt5.QtWidgets import QApplication
from viewManagers.mainWindowManager import mainWindow
from views import utils


def main():
	try:
		theme = utils.readQSS()

		app = QApplication(sys.argv)
		window = mainWindow()
		window.setStyleSheet(theme)
		window.show()

		sys.exit(app.exec_())
	except KeyboardInterrupt:
		sys.exit()


if __name__ == '__main__':
	main()

#!/usr/bin/env python3

import os
import signal
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from lib import MainWidget


def signit_handler(*args):

   QApplication.quit()


def main():

   app = QApplication([])

   app.setOrganizationName('SDU LSP')
   app.setOrganizationDomain('mmmi.sdu.dk')
   app.setApplicationName('Linux Task Menu')

   signal.signal(signal.SIGINT, signit_handler)
   timer = QTimer()
   timer.start(500)
   timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.

   mw = MainWidget()
   mw.show()

   sys.exit(app.exec())


if __name__ == '__main__':
   main()

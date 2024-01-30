# main widget

from PySide6.QtWidgets import QWidget

from .desktop_file import DesktopFile


class MainWidget(QWidget):

   def __init__(self, exeName):

      super().__init__()

      self.file = DesktopFile.findOrCreate(exeName)
      self.file.write()

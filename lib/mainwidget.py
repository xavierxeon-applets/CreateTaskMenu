# main widget
from .desktop_file import DesktopFile
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QFileDialog

from ._qt_tools import updateUI


class MainWidget(QWidget):

   def __init__(self):

      super().__init__()

      updateUI('mainwidget.ui')
      from .ui_mainwidget import Ui_MainWidget

      self.ui = Ui_MainWidget()
      self.ui.setupUi(self)

      self.ui.exeSelectButton.clicked.connect(self._selectExe)
      self.ui.iconSelectButton.clicked.connect(self._selectIcon)
      self.ui.createButton.clicked.connect(self._createEntry)

      self.ui.nameEdit.setText('UE5 Editor')
      self.ui.exeEdit.setText('/media/veracrypt1/Devel/UE5/Engine/Binaries/Linux/UnrealEditor')
      self.ui.iconEdit.setText('/media/veracrypt1/Devel/UE5/Engine/Content/Editor/Slate/About/UnrealLogo.svg')

      self._setIconPreview()

   def _selectExe(self):

      exeFileName = QFileDialog.getOpenFileName(self, 'Executable')
      exeFileName = exeFileName[0]
      if not exeFileName:
         return

      self.ui.exeEdit.setText(exeFileName)

   def _selectIcon(self):

      print('select icon', self.ui.iconEdit.text())

   def _setIconPreview(self):

      self.ui.iconPreview.setText('')

      pixmap = QPixmap(self.ui.iconEdit.text()).scaled(48, 48)
      self.ui.iconPreview.setPixmap(pixmap)

   def _createEntry(self):

      exeFileName = self.ui.exeEdit.text()
      iconFileName = self.ui.iconEdit.text()
      print('create entry', exeFileName, iconFileName)
      # self.file = DesktopFile.findOrCreate(exeName)
      # self.file.write()

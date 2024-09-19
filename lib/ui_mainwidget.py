# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QToolButton, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(582, 160)
        self.gridLayout = QGridLayout(MainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.iconInfo = QLabel(MainWidget)
        self.iconInfo.setObjectName(u"iconInfo")

        self.gridLayout.addWidget(self.iconInfo, 2, 0, 1, 1)

        self.iconSelectButton = QToolButton(MainWidget)
        self.iconSelectButton.setObjectName(u"iconSelectButton")

        self.gridLayout.addWidget(self.iconSelectButton, 2, 2, 1, 1)

        self.createButton = QCommandLinkButton(MainWidget)
        self.createButton.setObjectName(u"createButton")

        self.gridLayout.addWidget(self.createButton, 3, 1, 1, 2)

        self.exeSelectButton = QToolButton(MainWidget)
        self.exeSelectButton.setObjectName(u"exeSelectButton")

        self.gridLayout.addWidget(self.exeSelectButton, 1, 2, 1, 1)

        self.exeInfo = QLabel(MainWidget)
        self.exeInfo.setObjectName(u"exeInfo")

        self.gridLayout.addWidget(self.exeInfo, 1, 0, 1, 1)

        self.iconEdit = QLineEdit(MainWidget)
        self.iconEdit.setObjectName(u"iconEdit")

        self.gridLayout.addWidget(self.iconEdit, 2, 1, 1, 1)

        self.iconPreview = QLabel(MainWidget)
        self.iconPreview.setObjectName(u"iconPreview")

        self.gridLayout.addWidget(self.iconPreview, 3, 0, 1, 1)

        self.exeEdit = QLineEdit(MainWidget)
        self.exeEdit.setObjectName(u"exeEdit")

        self.gridLayout.addWidget(self.exeEdit, 1, 1, 1, 1)

        self.nameInfo = QLabel(MainWidget)
        self.nameInfo.setObjectName(u"nameInfo")

        self.gridLayout.addWidget(self.nameInfo, 0, 0, 1, 1)

        self.nameEdit = QLineEdit(MainWidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Desktop Entry", None))
        self.iconInfo.setText(QCoreApplication.translate("MainWidget", u"Icon", None))
        self.iconSelectButton.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.createButton.setText(QCoreApplication.translate("MainWidget", u"Create Desktop Entry", None))
        self.exeSelectButton.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.exeInfo.setText(QCoreApplication.translate("MainWidget", u"Executable", None))
        self.iconPreview.setText(QCoreApplication.translate("MainWidget", u"TextLabel", None))
        self.nameInfo.setText(QCoreApplication.translate("MainWidget", u"Name", None))
    # retranslateUi


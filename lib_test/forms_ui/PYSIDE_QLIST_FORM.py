# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLIST_FORM.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(291, 207)
        font = QFont()
        font.setFamilies([u"Roboto Black"])
        Dialog.setFont(font)
        Dialog.setWindowTitle(u"LIST FORM")
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Dialog.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        Dialog.setWindowFilePath(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tx_newitem = QLineEdit(Dialog)
        self.tx_newitem.setObjectName(u"tx_newitem")
        self.tx_newitem.setMinimumSize(QSize(221, 41))
        self.tx_newitem.setMaximumSize(QSize(16777215, 41))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(12)
        self.tx_newitem.setFont(font1)
#if QT_CONFIG(tooltip)
        self.tx_newitem.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tx_newitem.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tx_newitem.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tx_newitem.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tx_newitem.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.tx_newitem.setInputMask(u"")
        self.tx_newitem.setText(u"")
        self.tx_newitem.setPlaceholderText(u"")

        self.gridLayout.addWidget(self.tx_newitem, 0, 0, 1, 1)

        self.lst_items = QListWidget(Dialog)
        self.lst_items.setObjectName(u"lst_items")
        self.lst_items.setMinimumSize(QSize(221, 0))
        self.lst_items.setFont(font1)
#if QT_CONFIG(tooltip)
        self.lst_items.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lst_items.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lst_items.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.lst_items.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.lst_items.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lst_items.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.lst_items.setAlternatingRowColors(True)
        self.lst_items.setProperty("isWrapping", False)
        self.lst_items.setViewMode(QListView.ListMode)
        self.lst_items.setUniformItemSizes(False)
        self.lst_items.setWordWrap(False)
        self.lst_items.setSelectionRectVisible(False)

        self.gridLayout.addWidget(self.lst_items, 1, 0, 4, 1)

        self.btn_del = QPushButton(Dialog)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(41, 41))
        self.btn_del.setMaximumSize(QSize(41, 41))
        font2 = QFont()
        font2.setFamilies([u"Roboto Black"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.btn_del.setFont(font2)
#if QT_CONFIG(tooltip)
        self.btn_del.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_del.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_del.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_del.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_del.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_del.setText(u"-")
#if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.btn_del, 1, 1, 1, 1)

        self.btn_add = QPushButton(Dialog)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(41, 41))
        self.btn_add.setMaximumSize(QSize(41, 41))
        self.btn_add.setFont(font2)
#if QT_CONFIG(tooltip)
        self.btn_add.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_add.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_add.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_add.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_add.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_add.setText(u"+")
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.btn_add, 0, 1, 1, 1)

        self.btn_up = QPushButton(Dialog)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setMinimumSize(QSize(41, 41))
        self.btn_up.setMaximumSize(QSize(41, 41))
        font3 = QFont()
        font3.setFamilies([u"Roboto Black"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.btn_up.setFont(font3)
#if QT_CONFIG(tooltip)
        self.btn_up.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_up.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_up.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_up.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_up.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_up.setText(u"U")
#if QT_CONFIG(shortcut)
        self.btn_up.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.btn_up, 2, 1, 1, 1)

        self.btn_down = QPushButton(Dialog)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setMinimumSize(QSize(41, 41))
        self.btn_down.setMaximumSize(QSize(41, 41))
        self.btn_down.setFont(font3)
#if QT_CONFIG(tooltip)
        self.btn_down.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_down.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_down.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_down.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_down.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_down.setText(u"D")
#if QT_CONFIG(shortcut)
        self.btn_down.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.btn_down, 3, 1, 1, 1)

        QWidget.setTabOrder(self.tx_newitem, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.lst_items)
        QWidget.setTabOrder(self.lst_items, self.btn_del)
        QWidget.setTabOrder(self.btn_del, self.btn_up)
        QWidget.setTabOrder(self.btn_up, self.btn_down)

        self.retranslateUi(Dialog)
        self.btn_del.clicked.connect(self.lst_items.clearSelection)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        pass
    # retranslateUi


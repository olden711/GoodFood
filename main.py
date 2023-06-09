# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adapt_3.3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from site_parser import get_content, get_info_from_link
from functools import partial
from urllib.request import urlopen, Request
from PIL import Image


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(480, 640)
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.324, x2:1, y2:0, stop:0 rgba(138, 243, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 442, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn1.setFlat(True)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_3.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn2.setFlat(True)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_3.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn3.setFlat(True)
        self.btn3.setObjectName("btn3")
        self.verticalLayout_3.addWidget(self.btn3)
        self.btn4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn4.setFlat(True)
        self.btn4.setObjectName("btn4")
        self.verticalLayout_3.addWidget(self.btn4)
        self.btn5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn5.setFlat(True)
        self.btn5.setObjectName("btn5")
        self.verticalLayout_3.addWidget(self.btn5)
        self.btn6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn6.setFlat(True)
        self.btn6.setObjectName("btn6")
        self.verticalLayout_3.addWidget(self.btn6)
        self.btn7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn7.setFlat(True)
        self.btn7.setObjectName("btn7")
        self.verticalLayout_3.addWidget(self.btn7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.groupBox)
        self.exit_btn = QtWidgets.QPushButton(self.page)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.exit_btn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn, 0, QtCore.Qt.AlignBottom)
        StackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0.949045, stop:0 rgba(168, 255, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 460, 564))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 46))
        self.label.setMaximumSize(QtCore.QSize(450, 50))
        self.label.setBaseSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5.addLayout(self.verticalLayout_9)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.btn_back_to_first_page = QtWidgets.QPushButton(self.page_2)
        self.btn_back_to_first_page.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_back_to_first_page.setFont(font)
        self.btn_back_to_first_page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn_back_to_first_page.setObjectName("btn_back_to_first_page")
        self.verticalLayout_4.addWidget(self.btn_back_to_first_page, 0, QtCore.Qt.AlignBottom)
        StackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0.949045, stop:0 rgba(168, 255, 120, 255), stop:1 rgba(255, 255, 255, 255));")
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 460, 564))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.addWidget(self.scrollArea_3)
        self.btn_back_to_2_screen = QtWidgets.QPushButton(self.page_3)
        self.btn_back_to_2_screen.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_back_to_2_screen.setFont(font)
        self.btn_back_to_2_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0 rgba(221, 23, 250, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btn_back_to_2_screen.setObjectName("btn_back_to_2_screen")
        self.verticalLayout_6.addWidget(self.btn_back_to_2_screen, 0, QtCore.Qt.AlignBottom)
        StackedWidget.addWidget(self.page_3)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)


        # connection buttons with function

        self.btn1.clicked.connect(lambda: self.show_items(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.show_items(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.show_items(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.show_items(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.show_items(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.show_items(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.show_items(self.btn7.text()))

        self.btn_back_to_first_page.clicked.connect(self.back_on_first_page)

        self.btn_back_to_2_screen.clicked.connect(self.back_to_second_page)

        self.exit_btn.clicked.connect(self.exit_app)

        
    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "Правильная кухня"))
        self.groupBox.setTitle(_translate("StackedWidget", "Меню"))
        self.btn1.setText(_translate("StackedWidget", "Салаты"))
        self.btn2.setText(_translate("StackedWidget", "Выпечка"))
        self.btn3.setText(_translate("StackedWidget", "Супы"))
        self.btn4.setText(_translate("StackedWidget", "Гарниры"))
        self.btn5.setText(_translate("StackedWidget", "Напитки"))
        self.btn6.setText(_translate("StackedWidget", "Десерты"))
        self.btn7.setText(_translate("StackedWidget", "Перекусы"))
        self.exit_btn.setText(_translate("StackedWidget", "Выход"))
        self.label.setText(_translate("StackedWidget", "Список рецептов"))
        self.btn_back_to_first_page.setText(_translate("StackedWidget", "Назад"))
        self.label_2.setText(_translate("StackedWidget", "Описание рецепта"))
        self.btn_back_to_2_screen.setText(_translate("StackedWidget", "Назад"))

    def show_items(self, txt):
        StackedWidget.setCurrentIndex(1)
        receips = get_content(txt)
        for i in range(len(receips)):

            self.my_btn = QPushButton()
            self.my_btn.setMinimumSize(QtCore.QSize(0, 50))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setWeight(QFont.Bold)
            self.my_btn.setFont(font)
            self.my_btn.setText(str(receips[i]['title']))
            self.verticalLayout_9.addWidget(self.my_btn)
            self.my_btn.clicked.connect(
                partial(self.show_content, receips[i]['title'], receips[i]['url']))

        

    def show_content(self, title, url):

        #this function display content that consider in response
        StackedWidget.setCurrentIndex(2)
        _translate = QtCore.QCoreApplication.translate
        self.verticalLayout_7.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        
        if len(title)>50:
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_2.setFont(font)


        
        self.label_2.setText(_translate("StackedWidget", title))
        self.label_2.setWordWrap(True)

        #image of reciept
        self.img_label = QLabel()
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)

        #ingridients of reciept
        self.ingridients_label = QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ingridients_label.setFont(font)
        self.ingridients_label.setWordWrap(True)

        #text of receipt
        self.receipt_text_label = QLabel()
        self.receipt_text_label.setMaximumSize(QtCore.QSize(420, 16777215))
        self.receipt_text_label.setMinimumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.receipt_text_label.setFont(font)
        self.receipt_text_label.setWordWrap(True)
        
        img = get_info_from_link(url)[0]
        ing = ''
        rec = ''
        
        for i in get_info_from_link(url)[1]:
            ing+=i
            ing+='\n'

        for i in get_info_from_link(url)[2].split('.'):
            rec+=i.strip()
            rec+='\n'

        
        
        try:
            self.verticalLayout_7.addWidget(self.img_label)
            self.verticalLayout_7.addWidget(self.ingridients_label)
            self.verticalLayout_7.addWidget(self.receipt_text_label)
            req = Request(url=img, headers={'User-Agent': 'Mozilla/5.0'})
            image = Image.open(urlopen(req))
            image = image.resize((320,205),Image.ANTIALIAS)
            image = image.save('cashed_img.jpg')
            self.pixmap = QPixmap('cashed_img.jpg')
            self.img_label.setPixmap(self.pixmap)

            self.ingridients_label.setText(ing)
            self.receipt_text_label.setText(rec)
        
        except:
            #error label
            self.ingridients_label.setText('Something went wrong.')
            self.ingridients_label.setAlignment(QtCore.Qt.AlignCenter)

    def back_to_second_page(self):
        # removing previous created buttons

        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)
        
        
        
        StackedWidget.setCurrentIndex(1)
        

    def back_on_first_page(self):
        # removing prewious created buttons

        for i in reversed(range(self.verticalLayout_9.count())):
            self.verticalLayout_9.itemAt(i).widget().setParent(None)
        
        StackedWidget.setCurrentIndex(0)

    def exit_app(self):
        sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pachong

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1344, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 130, 791, 89))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:rgb(85, 170, 255);\n"
"\n"
"font: 16pt \"Adobe Devanagari\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(220, 210, 791, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setStyleSheet("color:rgb(85, 170, 255);\n"
"font: 16pt \"Adobe Devanagari\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_2.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1110, 660, 211, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1150, 610, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(538, 30, 241, 51))
        self.textBrowser.setStyleSheet("color:rgb(255, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(550, 430, 211, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 530, 1271, 71))
        self.textEdit_3.setStyleSheet("font: 14pt \"Adobe Devanagari\";\n"
"color:rgb(255, 0, 0)")
        self.textEdit_3.setObjectName("textEdit_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 300, 831, 89))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color:rgb(85, 170, 255);\n"
"font: 16pt \"Adobe Devanagari\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1344, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.textEdit.clear)
        self.pushButton_2.clicked.connect(self.textEdit_2.clear)
        self.pushButton_2.clicked.connect(self.textEdit_3.clear)
        self.pushButton_2.clicked.connect(self.textEdit_4.clear)

        self.pushButton_3.clicked.connect(self.geturl)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def geturl(self):
      try:
        url=self.textEdit.toPlainText()
        times=self.textEdit_2.toPlainText()
        path=self.textEdit_4.toPlainText()
        pachong.get_allurl(url,times,path)
        self.textEdit_3.setText("爬取完毕，请到存储路径处查看！")
      except:
          self.textEdit_3.setText("爬取失败！")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "请输入爬取的网址："))
        self.label_3.setText(_translate("MainWindow", "请输入爬取的层次："))
        self.label.setText(_translate("MainWindow", "作者：丁森濠  版本：v2.0"))
        self.pushButton.setText(_translate("MainWindow", "关闭应用"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">简单爬虫</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "开始爬取"))
        self.pushButton_2.setText(_translate("MainWindow", "清空文字"))
        self.label_4.setText(_translate("MainWindow", "请输入文件存储路径："))


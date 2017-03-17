# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\app\WX-VS-PQ\vs_main.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1360, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1360, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.step1GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.step1GroupBox.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.step1GroupBox.setObjectName("step1GroupBox")
        self.countrySelect = QtWidgets.QComboBox(self.step1GroupBox)
        self.countrySelect.setGeometry(QtCore.QRect(10, 20, 111, 22))
        self.countrySelect.setObjectName("countrySelect")
        self.countrySelect.addItem("")
        self.countryButton = QtWidgets.QPushButton(self.step1GroupBox)
        self.countryButton.setGeometry(QtCore.QRect(130, 20, 51, 23))
        self.countryButton.setObjectName("countryButton")
        self.step2GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.step2GroupBox.setGeometry(QtCore.QRect(10, 70, 191, 81))
        self.step2GroupBox.setObjectName("step2GroupBox")
        self.sourceInput = QtWidgets.QLineEdit(self.step2GroupBox)
        self.sourceInput.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.sourceInput.setObjectName("sourceInput")
        self.sourceButton = QtWidgets.QPushButton(self.step2GroupBox)
        self.sourceButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.sourceButton.setObjectName("sourceButton")
        self.step3GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.step3GroupBox.setGeometry(QtCore.QRect(10, 160, 191, 51))
        self.step3GroupBox.setObjectName("step3GroupBox")
        self.startButton = QtWidgets.QPushButton(self.step3GroupBox)
        self.startButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.startButton.setObjectName("startButton")
        self.logText = QtWidgets.QTextBrowser(self.centralwidget)
        self.logText.setGeometry(QtCore.QRect(10, 220, 191, 431))
        self.logText.setObjectName("logText")
        self.browserWebView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.browserWebView.setGeometry(QtCore.QRect(210, 0, 1151, 651))
        self.browserWebView.setProperty("url", QtCore.QUrl("http://www.lulutrip.com/"))
        self.browserWebView.setObjectName("browserWebView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 23))
        self.menubar.setObjectName("menubar")
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.setObjectName("helpMenu")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.helpMenu.addAction(self.actionAbout)
        self.fileMenu.addAction(self.actionExit)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.countrySelect, self.countryButton)
        MainWindow.setTabOrder(self.countryButton, self.sourceInput)
        MainWindow.setTabOrder(self.sourceInput, self.sourceButton)
        MainWindow.setTabOrder(self.sourceButton, self.startButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我行签证提交助手 - Demo Version"))
        self.step1GroupBox.setTitle(_translate("MainWindow", "第一步: 选择国家"))
        self.countrySelect.setItemText(0, _translate("MainWindow", "美国", "USA"))
        self.countryButton.setText(_translate("MainWindow", "确定"))
        self.step2GroupBox.setTitle(_translate("MainWindow", "第二步: 填写数据源"))
        self.sourceButton.setText(_translate("MainWindow", "读取数据"))
        self.step3GroupBox.setTitle(_translate("MainWindow", "第三步: 开始填表"))
        self.startButton.setText(_translate("MainWindow", "开始填表"))
        self.logText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">程序初始化完成</p></body></html>"))
        self.helpMenu.setTitle(_translate("MainWindow", "帮助"))
        self.fileMenu.setTitle(_translate("MainWindow", "文件"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl, QFile, QIODevice

import urllib.request, json

from Ui_vs_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.data = ''
        self.country = ''
        self.usa_urls = [
            QUrl('https://ceac.state.gov/genniv/default.aspx'), 
            QUrl('https://ceac.state.gov/GenNIV/Common/ConfirmApplicationID.aspx?node=SecureQuestion'), 
            QUrl('https://ceac.state.gov/GenNIV/General/complete/complete_personal.aspx?node=Personal1'), 
            QUrl('https://ceac.state.gov/GenNIV/General/complete/complete_personalcont.aspx?node=Personal2'), 
            QUrl('https://ceac.state.gov/GenNIV/General/complete/complete_contact.aspx?node=AddressPhone'), 
            QUrl('https://ceac.state.gov/GenNIV/General/complete/Passport_Visa_Info.aspx?node=PptVisa')
        ]
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError

    @pyqtSlot()
    def on_countryButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.country = self.countrySelect.currentText()
        self.showLog(u'国家已选择：'+self.country)
        self.browserWebView.page().urlChanged.connect(self.onUrlChanged)
        if self.country == '美国':
            self.browserWebView.page().load(self.usa_urls[0])
            self.browserWebView.page().loadStarted.connect(self.onUSALoadStarted)
        
    def showLog(self, log):
        self.logText.append(log)
        
    def loadFile(self, filename):
        file = QFile()
        file.setFileName("./js/"+filename)
        file.open(QIODevice.ReadOnly)
        code = file.readAll()
        file.close()
        return "".join(str(line) for line in code)
        
    @pyqtSlot()
    def onUSALoadStarted(self):
        self.browserWebView.page().loadStarted.disconnect()
        self.showLog(u'正在连接美国大使馆页面')
        self.browserWebView.page().loadFinished.connect(self.onUSALoadFinished)
        #self.browserWebView.page().loadFinished.connect(self.onUSALoadFinishedMonitor)
        
    @pyqtSlot("bool")
    def onUSALoadFinished(self, status):
        self.browserWebView.page().loadFinished.disconnect()
        if status is True:
            self.showLog(u'已跳转至美国大使馆页面')
            code = self.loadFile('vs_usa_0.js')
            self.browserWebView.page().runJavaScript(code)
            #self.browserWebView.page().runJavaScript("document.getElementById('ctl00_SiteContentPlaceHolder_ucLocation_ddlLocation').value='BEJ';")
            self.showLog(u'<p style=\'color:orange\'>[请注意]已为您选择<strong>北京领区</strong>，请填写图形验证码，然后完成至个人信息页面</p>')
            
            
    @pyqtSlot()
    def onUrlChanged(self):
        self.browserWebView.page().loadFinished.connect(self.onLoadFinishedMonitor)

    @pyqtSlot("bool")
    def onLoadFinishedMonitor(self, status):
        self.browserWebView.page().loadFinished.disconnect(self.onLoadFinishedMonitor)
        if status is True:
            # 美国签证检测获得的申请编号
            if self.browserWebView.page().url() == self.usa_urls[1]:
                self.browserWebView.page().runJavaScript("document.getElementById('ctl00_SiteContentPlaceHolder_lblBarcode').innerHTML",  self.logUSANumber)
                
    def logUSANumber(self, number):
        self.showLog(u'[请注意]您的申请编号是[<strong style=\'color:green\'>'+number+'</strong>]，请牢记')

    @pyqtSlot()
    def on_sourceButton_clicked(self):
        """
        Slot documentation goes here.
        """
        url = self.sourceInput.text()
        if url == '':
            self.showLog(u'<p style=\'color:red\'>[错误]请填写数据源网址</p>')
            return
        print(url)
        try:
            response = urllib.request.urlopen(url)
            self.data = json.loads(response.read().decode())
        except:
            self.showLog(u'<p style=\'color:red\'>[错误]您填写的数据源网址不正确</p>')
            return
        self.showLog(u'[提示]您已载入[<strong style=\'color:green\'>'+self.data['p1_03']+'</strong>]的用户资料')

    @pyqtSlot()
    def on_startButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if not self.country:
            self.showLog(u'<p style=\'color:red\'>[错误]您还没有选择签证国家</p>')
            return
        if not self.data:
            self.showLog(u'<p style=\'color:red\'>[错误]您还没有载入数据源</p>')
            return
        if self.country == "美国":
            if self.browserWebView.page().url() == self.usa_urls[2]:
                self.startUSAProcess()
            else:
                self.showLog(u'<p style=\'color:red\'>[错误]请操作至个人信息填写页 (Personal Information 1)</p>')
                return
            
    def startUSAProcess(self):
        #self.browserWebView.page().loadFinished.disconnect(self.onUSAProcessingMonitor)
        self.showLog(u'正在为您填写Personal1')
        self.browserWebView.page().loadFinished.connect(self.onUSAProcessingMonitor)
        self.browserWebView.page().runJavaScript('var wx_data = \''+json.dumps(self.data)+'\'')
        code = self.loadFile('vs_usa_1.js')
        self.browserWebView.page().runJavaScript(code)
        
            
    @pyqtSlot("bool")
    def onUSAProcessingMonitor(self, status):
        # 检测美国签证当前页面
        if status is True:
            print(self.browserWebView.page().url())
            if self.browserWebView.page().url() == self.usa_urls[3]:
                self.showLog(u'正在为您填写Personal2')
                self.browserWebView.page().runJavaScript('var wx_data = \''+json.dumps(self.data)+'\'')
                code = self.loadFile('vs_usa_2.js')
                self.browserWebView.page().runJavaScript(code)
            
            if self.browserWebView.page().url() == self.usa_urls[4]:
                self.showLog(u'正在为您填写Address and Phone')
                self.browserWebView.page().runJavaScript('var wx_data = \''+json.dumps(self.data)+'\'')
                code = self.loadFile('vs_usa_3.js')
                self.browserWebView.page().runJavaScript(code)
                
            if self.browserWebView.page().url() == self.usa_urls[5]:
                self.browserWebView.page().loadFinished.disconnect(self.onUSAProcessingMonitor)
                self.showLog(u'<p style=\'color:blue\'>[提示]演示已完成，感谢您的使用，请浏览已填写的页面查看是否信息已正确填入</p>')
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

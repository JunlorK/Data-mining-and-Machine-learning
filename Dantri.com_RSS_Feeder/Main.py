# -*- coding: utf8 -*-
'''
Created on Mar 29, 2016

@author: JuniorK
'''
from PyQt4 import QtGui,QtCore
from RSS_Feeder_GUI import Ui_MainWindow
import RSS_Feeder
import sys
from msilib.schema import ComboBox
class MainForm(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.textEdit.setPlainText("http://dantri.com.vn/giai-tri/sao-viet.rss")
        self.pushButton.clicked.connect(self.pushButton_click)
        self.pushButton_2.clicked.connect(self.pushButton_2_click)
        self.pushButton_3.clicked.connect(self.pushButton_3_click)
        self.label_2.setText('')
        self.comboBox.currentIndexChanged.connect(self.comboBox_valueChange)
    def comboBox_valueChange(self):
        print self.comboBox.currentText()
    def pushButton_click(self):
        self.comboBox.clear()
        list_link= RSS_Feeder.get_link(str(self.textEdit.toPlainText()))
        for link in list_link:
            self.comboBox.addItem(link)
    def pushButton_2_click(self):
        self.textEdit_2.setPlainText(RSS_Feeder.get_content(str(self.comboBox.currentText())).decode("utf-8"))    
    def pushButton_3_click(self):
        if str(self.comboBox.currentText())!='' and self.lineEdit.text()!='':            
            self.textEdit_2.setPlainText(RSS_Feeder.get_content(str(self.comboBox.currentText())).decode("utf-8"))
            content= unicode(self.textEdit_2.toPlainText())
            self.label_2.setText(str(content.count(unicode(self.lineEdit.text()))))
            #highlight content
            cursor = self.textEdit_2.textCursor()
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
            # Setup the regex engine
            pattern = unicode(self.lineEdit.text())
            regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            index = regex.indexIn(self.textEdit_2.toPlainText(), pos)
            while (index != -1):
                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
                cursor.mergeCharFormat(format)
                # Move to the next match
                pos = index + regex.matchedLength()
                index = regex.indexIn(self.textEdit_2.toPlainText(), pos) 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainApp=MainForm()
    MainApp.show()
    sys.exit(app.exec_())

        
    
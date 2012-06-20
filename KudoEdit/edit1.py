# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/kunj/.spyder2/.temp.py
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
import datetime, os


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        saveclick = QAction('Save', self)        
        saveclick.setShortcut('Ctrl+S')
        saveclick.setStatusTip('Save')
        saveclick.triggered.connect(self.savefile)
        
        exitclick = QtGui.QAction('Exit', self)        
        exitclick.setShortcut('Ctrl+Q')
        exitclick.setStatusTip('Exit')
        exitclick.triggered.connect(QtGui.qApp.quit)
        
        newclick = QtGui.QAction('New', self)        
        newclick.setShortcut('Ctrl+N')
        newclick.setStatusTip('New File')
        newclick.triggered.connect(self.newfile)
    
        openclick = QtGui.QAction('Open', self)        
        openclick.setShortcut('Ctrl+O')
        openclick.setStatusTip('Open')
        openclick.triggered.connect(self.openfile)

        saveasclick = QtGui.QAction('SaveAs', self)        
        saveasclick.setStatusTip('Save As')
        saveasclick.triggered.connect(self.save_asfile)
        
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newclick)
        fileMenu.addAction(saveclick)
        fileMenu.addAction(exitclick)
        fileMenu.addAction(openclick)
        fileMenu.addAction(saveasclick)
        
        self.showMaximized()        
        self.show()
                
    def savefile(self):
        f=open(self.filename, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()
                
    def save_asfile(self):
        filename = QFileDialog.getSaveFileName(self,"Save File",os.getcwd())
        self.filename=filename
        print filename
        f=open(filename, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()
        
    def openfile(self):
        filename = QFileDialog.getOpenFileName(self,"Open File",os.getcwd())
        print filename
        f=open(filename, 'r')
        text=f.read()
        f.close()
        self.textEdit.setText(text)
        self.show()
    
    def newfile(self):
        filename = open('filename_temp','w')

    def savetext(self):
        text=self.textEdit.toPlainText()
        if text:
            now = datetime.datetime.now()
            now1=str(now)[:19]
            savefile=open(now1+'.txt','w')
            savefile.write(text)
            
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     

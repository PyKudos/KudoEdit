# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/kunj/.spyder2/.temp.py
"""
import sys
from PyQt4 import QtGui
import datetime

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        exitclick = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)        
        exitclick.setShortcut('Ctrl+Q')
        exitclick.setStatusTip('Exit')
        exitclick.triggered.connect(QtGui.qApp.quit)
        
        saveclick = QtGui.QAction(QtGui.QIcon('save.png'), '&Save', self)        
        saveclick.setShortcut('Ctrl+S')
        saveclick.setStatusTip('Save')
        saveclick.triggered.connect(self.savetext)
        
        #newclick = QtGui.QAction(QtGui.QIcon('new.png'), '&New', self)        
        #newclick.setShortcut('Ctrl+N')
        #newclick.setStatusTip('New File')
        #newclick.triggered.connect(self.newfile())
    
       #exitclick = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
       # exitclick.setShortcut('Ctrl+Q')
       # exitclick.setStatusTip('Exit application')
       # exitclick.triggered.connect(QtGui.qApp.quit)
        
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitclick)
        fileMenu.addAction(saveclick)
        #fileMenu.addAction(newclick)
        self.showMaximized()        
        self.show()        

         #QString fileName = QFileDialog.getOpenFileName(this, tr("Open File"),"/home",tr("Images (*.png *.xpm *.jpg)"));
    #def newfile(self):
        #filename = open('filename','w')
    
    def savetext(self):
        text=self.textEdit.toPlainText()
        if text:
            now = datetime.datetime.now()
            now1=str(now)[:19]
            savefile=open(now1+'.txt','w')
            savefile.write(text)
    
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

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
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:15:32 2012

@author: kunj
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
import os

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.filename = None
        self.initUI()
        
    def initUI(self):
        self.italic_flag = True
        saveclick = QAction('Save', self)        
        saveclick.setShortcut('Ctrl+S')
        saveclick.setStatusTip('Save')
        saveclick.triggered.connect(self.savefile)
        
        exitclick = QAction('Exit', self)        
        exitclick.setShortcut('Ctrl+Q')
        exitclick.setStatusTip('Exit')
        exitclick.triggered.connect(QtGui.qApp.quit)
        
        newclick = QAction('New', self)        
        newclick.setShortcut('Ctrl+N')
        newclick.setStatusTip('New File')
        newclick.triggered.connect(self.newfile)
    
        openclick = QAction('Open', self)        
        openclick.setShortcut('Ctrl+O')
        openclick.setStatusTip('Open')
        openclick.triggered.connect(self.openfile)

        saveasclick = QAction('SaveAs', self)        
        saveasclick.setStatusTip('Save As')
        saveasclick.triggered.connect(self.save_asfile)
        
        copyclick = QAction('Copy', self)        
        copyclick.setShortcut('Ctrl+C')
        copyclick.setStatusTip('Copy')
        copyclick.triggered.connect(self.copy)
        
        pasteclick = QAction('Paste', self)        
        pasteclick.setShortcut('Ctrl+V')
        pasteclick.setStatusTip('Paste')
        pasteclick.triggered.connect(self.paste)
        """
        printclick = QAction('Print', self)        
        printclick.setShortcut('Ctrl+P')
        printclick.setStatusTip('Print')
        printclick.triggered.connect(self.printfile)
        """
        
        italicclick = QAction('Italic', self)        
        italicclick.setStatusTip('Italic')
        italicclick.triggered.connect(self.italic)

        
        tab = QTextEdit()
        self.tab_widget = QTabWidget()
        
        layout = QVBoxLayout(tab)
        self.tab_widget.addTab(tab,"untitled*")
        self.setCentralWidget(self.tab_widget)

        self.statusBar()
        
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newclick)
        fileMenu.addAction(openclick)
        fileMenu.addAction(saveclick)
        fileMenu.addAction(saveasclick)
        #fileMenu.addAction(printclick)
        fileMenu.addAction(exitclick)
    
        editMenu = menubar.addMenu('Edit')
        editMenu.addAction(copyclick)
        editMenu.addAction(pasteclick)
        
        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(italicclick)
        
        self.showMaximized()        
        self.show()
    
    def keyReleaseEvent(self, e):
        tab_index = self.tab_widget.currentIndex()
        tabText = self.tab_widget.tabText(tab_index)
        self.tab_widget.tabBar().setTabTextColor(tab_index, 
                                                 QColor(255,0,0))
        if tabText != "untitled*" and tabText[-1] != "*":
            tabText = tabText+"*"
            self.tab_widget.setTabText(tab_index,tabText)
    """
    def printfile(self):
        #print_cmd = 'lp -d NetPrinter filename'
        text=self.textEdit.toPlainText()
        os.popen(str(text))
        #self.textEdit.print_(os.printer)
    """
    def copy(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        textEdit.copy()
        
    def paste(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        textEdit.paste()
    
    def italic(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        textEdit.setFontItalic(self.italic_flag)
        self.italic_flag = not self.italic_flag
                
    def savefile(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        filename = self.tab_widget.tabText(tab_index)
        if filename == "untitled*":
            self.save_asfile()
            return
        if filename[-1] == "*":
            filename = filename[:-1]
        f=open(filename, 'w')
        f.write(textEdit.toPlainText())
        f.close()
        self.tab_widget.setTabText(tab_index,filename)
        self.tab_widget.tabBar().setTabTextColor(tab_index, QColor(0,0,0))
        
    def save_asfile(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        filename = QFileDialog.getSaveFileName(self,"Save File",os.getcwd())
        print filename
        f=open(filename, 'w')
        f.write(textEdit.toPlainText())
        f.close()
        self.tab_widget.tabBar().setTabTextColor(tab_index, QColor(0,0,0))
        self.tab_widget.setTabText(tab_index,filename.split("/")[-1])
        
    def openfile(self):
        filename = QFileDialog.getOpenFileName(self,"Open File",os.getcwd())
        self.filename = filename
        print filename
        f=open(filename, 'r')
        text=f.read()
        f.close()
        textEdit = QTextEdit()
        textEdit.setText(text)
        self.tab_widget.addTab(textEdit,self.filename.split("/")[-1])
        self.show()
    
    def newfile(self):
        tab = QTextEdit()
        layout = QVBoxLayout(tab)
        self.tab_widget.addTab(tab,"untitled*")
        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 
                                    'Message', 
                                    "Are you sure you want to quit?", 
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def KudoEdit():
    
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
    
KudoEdit()
 

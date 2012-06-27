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
        self.italic_flag = False
        self.underline_flag = False
        self.path = os.path.abspath(__file__)
        self.icon_path = "/".join(self.path.split("/")[:-1]+["icons"])
<<<<<<< HEAD
        self.saveclick = QAction(QIcon("/".join([self.icon_path,"save_icon.png"])), 'Save', self)        
        self.saveclick.setShortcut('Ctrl+S')
        self.saveclick.setStatusTip('Save')
        self.saveclick.triggered.connect(self.savefile)
        
        self.exitclick = QAction(QIcon("/".join([self.icon_path,"exit_icon.png"])),'Exit', self)        
        self.exitclick.setShortcut('Ctrl+Q')
        self.exitclick.setStatusTip('Exit')
        self.exitclick.triggered.connect(qApp.quit)
        
        self.newclick = QAction(QIcon("/".join([self.icon_path,"new_icon.png"])), 'New', self)        
        self.newclick.setShortcut('Ctrl+N')
        self.newclick.setStatusTip('New File')
        self.newclick.triggered.connect(self.newfile)
    
        self.openclick = QAction(QIcon("/".join([self.icon_path,"open_icon.png"])), 
                                        'Open', self)
        self.openclick.setShortcut('Ctrl+O')
        self.openclick.setStatusTip('Open')
        self.openclick.triggered.connect(self.openfile)

        self.saveasclick = QAction('SaveAs', self)        
        self.saveasclick.setStatusTip('Save As')
        self.saveasclick.triggered.connect(self.save_asfile)
        
        self.copyclick = QAction('Copy', self)
        self.copyclick.setShortcut('Ctrl+C')
        self.copyclick.setStatusTip('Copy')
        self.copyclick.triggered.connect(self.copy)
        
        self.pasteclick = QAction('Paste', self)        
        self.pasteclick.setShortcut('Ctrl+V')
        self.pasteclick.setStatusTip('Paste')
        self.pasteclick.triggered.connect(self.paste)
        
        self.close_tab_click = QAction('Close', self)        
        self.close_tab_click.setShortcut('Ctrl+W')
        self.close_tab_click.setStatusTip('Close Current Tab')
        self.close_tab_click.triggered.connect(self.close_tab)
        #self.close_tab_click = close_tab_click
        
        italicclick = QAction(QIcon("/".join([self.icon_path,"italic_icon.png"])),
                                    'Italic', self)
        italicclick.setShortcut('Ctrl+I')
=======
        saveclick = QAction(QtGui.QIcon('/home/kunj/Desktop/icons/save.png'), 'Save', self)        
        saveclick.setShortcut('Ctrl+S')
        saveclick.setStatusTip('Save')
        saveclick.triggered.connect(self.savefile)
        
        exitclick = QAction(QtGui.QIcon('/home/kunj/Desktop/icons/exit.png'),'Exit', self)        
        exitclick.setShortcut('Ctrl+Q')
        exitclick.setStatusTip('Exit')
        exitclick.triggered.connect(qApp.quit)
        
        newclick = QAction(QtGui.QIcon('/home/kunj/Desktop/icons/new.png'), 'New', self)        
        newclick.setShortcut('Ctrl+N')
        newclick.setStatusTip('New File')
        newclick.triggered.connect(self.newfile)
    
        openclick = QAction(QtGui.QIcon('/home/kunj/Desktop/icons/open.jpg'), 
                                        'Open', self)
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
        
        close_tab_click = QAction('Close', self)        
        close_tab_click.setShortcut('Ctrl+W')
        close_tab_click.setStatusTip('Close Current Tab')
        close_tab_click.triggered.connect(self.close_tab)
        self.close_tab_click = close_tab_click
        
        italicclick = QAction(QtGui.QIcon(
                                    '/home/kunj/Desktop/icons/font_italic.png'),
                                    'Italic', self)
>>>>>>> master
        italicclick.setStatusTip('Italic')
        italicclick.triggered.connect(self.italic)
        self.italicclick = italicclick
        
<<<<<<< HEAD
        boldclick = QAction(QIcon("/".join([self.icon_path,"bold_icon.png"])),
                                 'Bold', self)        
        boldclick.setShortcut('Ctrl+B')
        boldclick.setStatusTip('Bold')
        boldclick.triggered.connect(self.bold)
        self.boldclick = boldclick
        
        underlineclick = QAction(QIcon("/".join([self.icon_path,"underline_icon.png"])),
                                      'Underline', self) 
        underlineclick.setShortcut('Ctrl+U')
        underlineclick.setStatusTip('Underline')
        underlineclick.triggered.connect(self.underline)
        self.underlineclick = underlineclick
        
        printclick = QAction(QIcon("/".join([self.icon_path,"print_icon.png"])),
=======
        boldclick = QAction(QtGui.QIcon(
                                 '/home/kunj/Desktop/icons/font_bold.png'),
                                 'Bold', self)        
        boldclick.setStatusTip('Bold')
        boldclick.triggered.connect(self.bold)
        
        underlineclick = QAction(QtGui.QIcon(
                                      '/home/kunj/Desktop/icons/font_underline'),
                                      'Underline', self) 
        underlineclick.setStatusTip('Underline')
        underlineclick.triggered.connect(self.underline)
        
        printclick = QAction(QtGui.QIcon(
                                   '/home/kunj/Desktop/icons/print.png'),
>>>>>>> master
                                   'Print', self)        
        printclick.setShortcut('Ctrl+P')
        printclick.setStatusTip('Print')
        #printclick.triggered.connect(self.printfile)
        
        tab = QTextEdit()
        self.tab_widget = QTabWidget()
        self.tab_widget.tabsClosable()
        textEditf = QFont()
        
        layout = QVBoxLayout(tab)
        QtCore.QObject.connect(self.tab_widget, 
                              QtCore.SIGNAL('tabCloseRequested(int)'), 
                              self.close_tab)
        self.setCentralWidget(self.tab_widget)

        self.statusBar()
        self.toolbar = self.addToolBar('New')
        self.toolbar.addAction(self.newclick)
        self.toolbar.addAction(self.saveclick)
        self.toolbar.addAction(self.exitclick)
        self.toolbar.addAction(self.boldclick)
        self.toolbar.addAction(self.italicclick)
        self.toolbar.addAction(self.underlineclick)
        
        self.toolbar = self.addToolBar('New')
        self.toolbar.addAction(newclick)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveclick)
        self.toolbar = self.addToolBar('Print')
        self.toolbar.addAction(printclick)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitclick)
        self.toolbar = self.addToolBar('Bold')
        self.toolbar.addAction(boldclick)
        self.toolbar = self.addToolBar('Italic')
        self.toolbar.addAction(italicclick)
        self.toolbar = self.addToolBar('Underline')
        self.toolbar.addAction(underlineclick)
        
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('File')
<<<<<<< HEAD
        fileMenu.addAction(self.newclick)
        fileMenu.addAction(self.openclick)
        fileMenu.addAction(self.saveclick)
        fileMenu.addAction(self.saveasclick)
        fileMenu.addAction(self.close_tab_click)
        #fileMenu.addAction(printclick)
        fileMenu.addAction(self.exitclick)
=======
        fileMenu.addAction(newclick)
        fileMenu.addAction(openclick)
        fileMenu.addAction(saveclick)
        fileMenu.addAction(saveasclick)
        fileMenu.addAction(close_tab_click)
        fileMenu.addAction(printclick)
        fileMenu.addAction(exitclick)
>>>>>>> master
    
        editMenu = menubar.addMenu('Edit')
        editMenu.addAction(self.copyclick)
        editMenu.addAction(self.pasteclick)
        
        viewMenu = menubar.addMenu('View')
<<<<<<< HEAD
        viewMenu.addAction(self.italicclick)
        viewMenu.addAction(self.boldclick)
        viewMenu.addAction(self.underlineclick)
=======
        viewMenu.addAction(italicclick)
        viewMenu.addAction(boldclick)
        viewMenu.addAction(underlineclick)
>>>>>>> master
        
        self.showMaximized()        
        self.show()
    
    def keyReleaseEvent(self, e):
        tab_index = self.tab_widget.currentIndex()
        tabText = self.tab_widget.tabText(tab_index)
        self.tab_widget.tabBar().setTabTextColor(tab_index, 
                                                 QColor(255,0,0))
        if tab_index < 0:
            return
        if tabText != "untitled*" and tabText[-1] != "*":
            tabText = tabText+"*"
            self.tab_widget.setTabText(tab_index,tabText)
            
    def close_tab(self):
        print "closing tab"
        tab_index = self.tab_widget.currentIndex()
        if tab_index < 0:
            qApp.quit()
            return
        tabText = self.tab_widget.tabText(tab_index)
        if tabText[-1] == "*":
            msgBox = QMessageBox()
            msgBox.setText("The document has been modified.")
            msgBox.setInformativeText("Do you want to save your changes?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            
            if ret == QMessageBox.Save:
                self.savefile()
                self.close_tab()
            elif ret == QMessageBox.Discard:
                pass
            elif ret == QMessageBox.Cancel:
                return
        self.tab_widget.removeTab(tab_index)
            
    """
    def printfile(self):
        #print_cmd = 'lp -d NetPrinter filename'
        text=self.textEdit.toPlainText()
        os.popen(str(text))
        #self.textEdit.print_(os.printer)
    """
    
    def italic(self):
        italic_button = self.toolbar.widgetForAction(self.italicclick)
        italic_icon = QIcon("/".join([self.icon_path,"italic_icon.png"]))
        print self.italic_flag
        if not self.italic_flag:
            new_pixmap = italic_icon.pixmap(QtCore.QSize(20,20),QIcon.Disabled,QIcon.On)
        else:
            new_pixmap = italic_icon.pixmap(QtCore.QSize(20,20),QIcon.Active, QIcon.On)
        
        new_icon = QIcon(new_pixmap)
        italic_button.setIcon(new_icon)
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
<<<<<<< HEAD
        if not textEdit:
            return
=======
>>>>>>> master
        textEdit.setFontItalic(not self.italic_flag)
        self.italic_flag = not self.italic_flag
    
    def bold(self):
<<<<<<< HEAD
        bold_button = self.toolbar.widgetForAction(self.boldclick)
        bold_icon = QIcon("/".join([self.icon_path,"bold_icon.png"]))
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        if not textEdit:
            return
        font_weight = textEdit.fontWeight()
        if font_weight == 50:
            new_pixmap = bold_icon.pixmap(QtCore.QSize(20,20),QIcon.Disabled,QIcon.On)
            font_weight = 75
            textEdit.setFontWeight(font_weight)
        else: 
            new_pixmap = bold_icon.pixmap(QtCore.QSize(20,20),QIcon.Active, QIcon.On)
            font_weight = 50
            textEdit.setFontWeight(font_weight)
        new_icon = QIcon(new_pixmap)
        bold_button.setIcon(new_icon)
=======
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
        font_weight = textEdit.fontWeight()
        if font_weight == 50:
            font_weight = 75
            textEdit.setFontWeight(font_weight)
        else: 
            font_weight = 50
            textEdit.setFontWeight(font_weight)
>>>>>>> master
            
    def underline(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
<<<<<<< HEAD
        if not textEdit:
            return
        if not self.underline_flag:
            status = QIcon.Disabled
        else:
            status = QIcon.Active
        textEdit.setFontUnderline(not self.underline_flag)
        button = self.toolbar.widgetForAction(self.underlineclick)
        icon = QIcon("/".join([self.icon_path,"underline_icon.png"]))
        new_pixmap = icon.pixmap(QtCore.QSize(20,20),status,QIcon.On)
        new_icon = QIcon(new_pixmap)
        button.setIcon(new_icon)
=======
        textEdit.setFontUnderline(not self.underline_flag)
>>>>>>> master
        self.underline_flag = not self.underline_flag
    
    def copy(self):
        tab_index = self.tab_widget.currentIndex()
        if tab_index < 0:
            return
        textEdit = self.tab_widget.widget(tab_index)
        textEdit.copy()
        
    def paste(self):
        tab_index = self.tab_widget.currentIndex()
        if tab_index < 0:
            return
        textEdit = self.tab_widget.widget(tab_index)
        textEdit.paste()
                
    def savefile(self):
        tab_index = self.tab_widget.currentIndex()
        if tab_index < 0:
            return
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
        if tab_index < 0:
            return
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
        print filename
        f=open(filename, 'r')
        text=f.read()
        f.close()
        textEdit = QTextEdit()
        textEdit.setText(text)
        self.tab_widget.addTab(textEdit,filename.split("/")[-1])
        tab_count = self.tab_widget.count()
        tabbar = self.tab_widget.tabBar()
        close_tab_click = QAction(QIcon("/".join([self.icon_path,"dialog-close.svg"])),"",self)
        close_tab_click.triggered.connect(self.close_tab)
        but = QToolButton()
        but.setDefaultAction(close_tab_click)
        self.tab_widget.tabBar().setTabButton(tab_count-1,QTabBar.RightSide,but)
        self.tab_widget.tabsClosable()
        self.show()
        
    def newfile(self):
        tab = QTextEdit()
        layout = QVBoxLayout(tab)
        self.tab_widget.addTab(tab,"untitled*")
        tab_count = self.tab_widget.count()
        tabbar = self.tab_widget.tabBar()
        close_tab_click = QAction(QIcon("/".join([self.icon_path,"dialog-close.svg"])),"",self)
        close_tab_click.triggered.connect(self.close_tab)
        but = QToolButton()
        but.setDefaultAction(close_tab_click)
        self.tab_widget.tabBar().setTabButton(tab_count-1,QTabBar.RightSide,but)
        self.tab_widget.tabsClosable()
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
<<<<<<< HEAD
=======

KudoEdit()
>>>>>>> master

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
        
        self.exitclick = self.add_action("Exit", "Ctrl+Q", 
                                         "/".join([self.icon_path,"exit_icon.png"]))
        self.exitclick.triggered.connect(qApp.quit)
        
        self.newclick = self.add_action("New", "Ctrl+N",
                                        "/".join([self.icon_path,"new_icon.png"]))
        self.newclick.triggered.connect(self.newfile)
        
        self.openclick = self.add_action("Open", "Ctrl+O",
                                         "/".join([self.icon_path,"open_icon.png"]))
        self.openclick.triggered.connect(self.openfile)
        
        self.saveclick = self.add_action("Save", "Ctrl+S",
                                         "/".join([self.icon_path,"save_icon.png"]))
        self.exitclick.triggered.connect(self.savefile)
        
        self.saveasclick = self.add_action("SaveAs", "Ctrl+Shift+S", 
                                          "/".join([self.icon_path,"save_as_icon.gif"]))
        self.saveasclick.triggered.connect(self.save_asfile)
        
        self.copyclick = self.add_action("Copy", "Ctrl+C",
                                         "/".join([self.icon_path,"copy_icon.png"]))
        self.copyclick.triggered.connect(self.copy)
        
        self.pasteclick = self.add_action("Paste", "Ctrl+V",
                                         "/".join([self.icon_path,"paste_icon.jpg"]))
        self.pasteclick.triggered.connect(self.paste)
        
        #self.printclick = self.add_action("Print", "Ctrl+P", "/".join([self.icon_path,"print_icon.jpg"]))
        #self.pasteclick.triggered.connect(self.print)
        
        self.close_tab_click = self.add_action("Close", "Ctrl+W", self)
        self.close_tab_click.triggered.connect(self.close_tab)
        
        self.italicclick = self.add_action("Italic", "Ctrl+I",
                                          "/".join([self.icon_path,"italic_icon.png"]))
        self.italicclick.triggered.connect(self.italic)
        
        self.boldclick = self.add_action("Bold", "Ctrl+B",
                                         "/".join([self.icon_path,"bold_icon.png"]))
        self.boldclick.triggered.connect(self.bold)
        
        self.underlineclick = self.add_action("Underline", "Ctrl+U",
                                             "/".join([self.icon_path,"underline_icon.png"]))
        self.underlineclick.triggered.connect(self.underline)
        
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
        self.toolbar.addAction(self.saveasclick)
        self.toolbar.addAction(self.openclick)
        self.toolbar.addAction(self.exitclick)
        self.toolbar.addAction(self.copyclick)
        self.toolbar.addAction(self.pasteclick)
        self.toolbar.addAction(self.boldclick)
        self.toolbar.addAction(self.italicclick)
        self.toolbar.addAction(self.underlineclick)
        
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(self.newclick)
        fileMenu.addAction(self.openclick)
        fileMenu.addAction(self.saveclick)
        fileMenu.addAction(self.saveasclick)
        fileMenu.addAction(self.close_tab_click)
        #fileMenu.addAction(printclick)
        fileMenu.addAction(self.exitclick)
    
        editMenu = menubar.addMenu('Edit')
        editMenu.addAction(self.copyclick)
        editMenu.addAction(self.pasteclick)
        
        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(self.italicclick)
        viewMenu.addAction(self.boldclick)
        viewMenu.addAction(self.underlineclick)
        
        self.showMaximized()        
        self.show()
    
    def add_action(self, action_name, shortcut=None, icon_path=None):
        action = QAction(QIcon(icon_path), action_name, self)
        action.setShortcut(shortcut)
        action.setStatusTip(action_name)
        return action
    
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
        if not textEdit:
            return
        textEdit.setFontItalic(not self.italic_flag)
        self.italic_flag = not self.italic_flag
    
    def bold(self):
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
            
    def underline(self):
        tab_index = self.tab_widget.currentIndex()
        textEdit = self.tab_widget.widget(tab_index)
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
    
#KudoEdit()

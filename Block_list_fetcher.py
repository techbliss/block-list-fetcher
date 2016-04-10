
# Created by Storm Shadow www.techbliss.org
print "\n" #getting the box fit
print " ###################################################\n" \
    " #              Author Storm Shadow                # \n" \
    " #                   Hotkeys                       # \n" \
    " #         NewFile:            Ctrl+N              #\n" \
    " #         OpenFile:           Ctrl+O              #\n" \
    " #         SaveFile:           Ctrl+S              #\n" \
    " #         Undo:               Ctrl+Z              #\n" \
    " #         Redo:               Ctrl+Y              #\n" \
    " #         SelectALL:          Ctrl+A              #\n" \
    " #         Paste:              Ctrl+V              #\n" \
    " #         Author:             Ctrl+B              #\n" \
    " #         Zoom in             Ctrl+Shift+ +       #\n" \
    " #         Zoom Out            Ctrl+Shift+ -       #\n" \
    " #                                                 #\n" \
    " ###################################################\n" \
    " #              Malware block fetcher              #\n" \
    " ###################################################\n"
import os
import sys
from urllib2 import urlopen
import fileinput
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtGui import *



sys.path.insert(0, os.getcwd()+r'\icons')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    import icons
except ImportError:
    pass


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(854, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/Python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.filename = ""
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(563, 531))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(32, 0))
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setMinimumSize(QtCore.QSize(32, 0))
        self.toolBar_2.setIconSize(QtCore.QSize(32, 32))
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        MainWindow.insertToolBarBreak(self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setMinimumSize(QtCore.QSize(32, 0))
        self.toolBar_3.setIconSize(QtCore.QSize(32, 32))
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_3)
        MainWindow.insertToolBarBreak(self.toolBar_3)

        #populate action1
        #first action 1
        self.toolBar.Action1 = QtGui.QAction(QtGui.QIcon(":/icon/icons/reactor.png"),"Open http://ransomwaretracker.abuse.ch/  ",self.toolBar)
        self.toolBar.Action1.setStatusTip("Clear TextBox or make new document.")
        self.toolBar.Action1.setShortcut("")
        self.toolBar.Action1.triggered.connect(self.command1)
        #second Action 2
        self.toolBar.Action2 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockred.png"),"Download IP Block list",self.toolBar)
        self.toolBar.Action2.setStatusTip("")
        self.toolBar.Action2.setShortcut("Ctrl+O")
        self.toolBar.Action2.triggered.connect(self.command2)
        # action 3
        self.toolBar.Action3 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockblue.png"),"Download URL Blocklist",self.toolBar)
        self.toolBar.Action3.setStatusTip("")
        self.toolBar.Action3.setShortcut("Ctrl+S")
        self.toolBar.Action3.triggered.connect(self.command3)
        #action 4
        self.toolBar.Action4 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blocksaned.png"),"Download Domain Blocklist",self.toolBar)
        self.toolBar.Action4.setStatusTip("")
        self.toolBar.Action4.setShortcut("")
        self.toolBar.Action4.triggered.connect(self.command4)
        #action 5
        self.toolBar.Action5 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockpurp.png"),"Download Domain Blocklist And use it with Windows Host File",self.toolBar)
        self.toolBar.Action5.setStatusTip("")
        self.toolBar.Action5.setShortcut("")
        self.toolBar.Action5.triggered.connect(self.command5)
        #first 6 new
        self.toolBar.Action6 = QtGui.QAction(QtGui.QIcon(":/icon/icons/new.png"),"New",self.toolBar)
        self.toolBar.Action6.setStatusTip("Clear TextBox or make new document.")
        self.toolBar.Action6.setShortcut("Ctrl+N")
        self.toolBar.Action6.triggered.connect(self.newfile)
        #second 7 open
        self.toolBar.Action7 = QtGui.QAction(QtGui.QIcon(":/icon/icons/open.png"),"Open",self.toolBar)
        self.toolBar.Action7.setStatusTip("Create a new document from scratch.")
        self.toolBar.Action7.setShortcut("Ctrl+O")
        self.toolBar.Action7.triggered.connect(self.open)
        # action 8 save
        self.toolBar.Action8 = QtGui.QAction(QtGui.QIcon(":/icon/icons/save.png"),"Save",self.toolBar)
        self.toolBar.Action8.setStatusTip("Save Your File.")
        self.toolBar.Action8.setShortcut("Ctrl+S")
        self.toolBar.Action8.triggered.connect(self.savefile)



        #populate action2
        #first action 1
        self.toolBar_2.Action1 = QtGui.QAction(QtGui.QIcon(":/icon/icons/i.png"),"Open https://www.iblocklist.com  ",self.toolBar_2)
        self.toolBar_2.Action1.setStatusTip("Clear TextBox or make new document.")
        self.toolBar_2.Action1.setShortcut("")
        self.toolBar_2.Action1.triggered.connect(self.command6)
        #second Action 2
        self.toolBar_2.Action2 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockred.png"),"level1 bluetack list",self.toolBar_2)
        self.toolBar_2.Action2.setStatusTip("")
        self.toolBar_2.Action2.setShortcut("Ctrl+O")
        self.toolBar_2.Action2.triggered.connect(self.command7)
        # action 3
        self.toolBar_2.Action3 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockblue.png"),"level2 bluetack list",self.toolBar_2)
        self.toolBar_2.Action3.setStatusTip("")
        self.toolBar_2.Action3.setShortcut("")
        self.toolBar_2.Action3.triggered.connect(self.command8)
        # action 4
        self.toolBar_2.Action4 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blocksaned.png"),"level3 bluetack list",self.toolBar_2)
        self.toolBar_2.Action4.setStatusTip("")
        self.toolBar_2.Action4.setShortcut("")
        self.toolBar_2.Action4.triggered.connect(self.command9)
        # action 5
        self.toolBar_2.Action5 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockpurp.png"),"Spyware Blocklist",self.toolBar_2)
        self.toolBar_2.Action5.setStatusTip("")
        self.toolBar_2.Action5.setShortcut("")
        self.toolBar_2.Action5.triggered.connect(self.command10)


        #populate action3
        #first action 1
        self.toolBar_3.Action1 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blocklistde.jpg"),"Open http://www.blocklist.de  ",self.toolBar_3)
        self.toolBar_3.Action1.setStatusTip("")
        self.toolBar_3.Action1.setShortcut("")
        self.toolBar_3.Action1.triggered.connect(self.command11)
        #second Action 2
        self.toolBar_3.Action2 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockred.png"),"ALL last 48 hours",self.toolBar_3)
        self.toolBar_3.Action2.setStatusTip("")
        self.toolBar_3.Action2.setShortcut("")
        self.toolBar_3.Action2.triggered.connect(self.command12)
        # action 3
        self.toolBar_3.Action3 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockblue.png"),"SSH last 48 hours",self.toolBar_3)
        self.toolBar_3.Action3.setStatusTip("")
        self.toolBar_3.Action3.setShortcut("")
        self.toolBar_3.Action3.triggered.connect(self.command13)
        # action 4
        self.toolBar_3.Action4 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blocksaned.png"),"Mails last 48 hours",self.toolBar_3)
        self.toolBar_3.Action4.setStatusTip("")
        self.toolBar_3.Action4.setShortcut("")
        self.toolBar_3.Action4.triggered.connect(self.command14)
        # action 5
        self.toolBar_3.Action5 = QtGui.QAction(QtGui.QIcon(":/icon/icons/blockpurp.png"),"Bruteforcelogin last 48 hours",self.toolBar_3)
        self.toolBar_3.Action5.setStatusTip("")
        self.toolBar_3.Action5.setShortcut("")
        self.toolBar_3.Action5.triggered.connect(self.command15)

        #ekstra actions
        # zoom in
        self.toolBar.Action9 = QtGui.QAction(QtGui.QIcon(":/icon/icons/zoom-in.png"),"Zoom In",self.toolBar)
        self.toolBar.Action9.setStatusTip("Zoom In")
        self.toolBar.Action9.setShortcut("CTRL+SHIFT++")
        self.toolBar.Action9.triggered.connect(self.udder)
        #zoom out
        self.toolBar.Action10 = QtGui.QAction(QtGui.QIcon(":/icon/icons/zoom_out.png"),"Zoom Out",self.toolBar)
        self.toolBar.Action10.setStatusTip("Zoom Out")
        self.toolBar.Action10.setShortcut("CTRL+SHIFT+-")
        self.toolBar.Action10.triggered.connect(self.odder)
        #auther me :)
        self.toolBar.Action11 = QtGui.QAction(QtGui.QIcon(":/icon/icons/world.png"),"Author",self.toolBar)
        self.toolBar.Action11.setStatusTip("Author")
        self.toolBar.Action11.setShortcut("Ctrl+B")
        self.toolBar.Action11.triggered.connect(self.Author)



        #action for toolbar

        self.toolBar.addAction(self.toolBar.Action1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action7)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action9)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action10)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action11)

        #action for toolbar2
        self.toolBar_2.addAction(self.toolBar_2.Action1)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.toolBar_2.Action2)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.toolBar_2.Action3)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.toolBar_2.Action4)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.toolBar_2.Action5)

        #action for toolbar3
        self.toolBar_3.addAction(self.toolBar_3.Action1)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.toolBar_3.Action2)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.toolBar_3.Action3)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.toolBar_3.Action4)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.toolBar_3.Action5)



        #action for toolbar3


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Block list fetcher by Storm Shadow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar.setToolTip(_translate("MainWindow", "http://ransomwaretracker.abuse.ch/", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_2.setToolTip(_translate("MainWindow", "https://www.iblocklist.com/", None))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))
        self.toolBar_3.setToolTip(_translate("MainWindow", "blocklist.de", None))

    # file open/save/new

    def newfile(self):
        self.textEdit.clear()

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(
            self.centralwidget, 'Open File', self.path, "Open list (*.txt *.*)",
            '')

        if self.filename:
            with open(self.filename, "r") as self.file:
                self.textEdit.setText(self.file.read())
        os.chdir(str(self.path))

    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        self.filename = QtGui.QFileDialog.getSaveFileName(
            self.centralwidget, "Save as", self.path, "Save you list (*.txt *.*)",
        )
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.textEdit.toPlainText()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtGui.QMessageBox.information(self.centralwidget, "Unable to open file",
                                          file.errorString())
        os.chdir(str(self.path))

    #commands heyyyy!

    def command1(self):
        import webbrowser
        webbrowser.open('http://ransomwaretracker.abuse.ch/')

    def command2(self):
        url1 = 'https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt'
        fetchblock = urlopen(url1).read()
        self.textEdit.setPlainText(fetchblock)

    def command3(self):
        url2 = 'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt'
        fetchblock2 = urlopen(url2).read()
        self.textEdit.setPlainText(fetchblock2)

    def command4(self):
        url3 = 'https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt'
        fetchblock3 = urlopen(url3).read()
        self.textEdit.setPlainText(fetchblock3)


    def command5(self):
        url4 = 'https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt'
        fetchblock4 = urlopen(url4).read()
        self.textEdit.setPlainText('\n' + fetchblock4.replace('\n', '\n127.0.0.1 '))


    def command6(self):
        import webbrowser
        webbrowser.open('https://www.iblocklist.com')

    def command7(self):
        url6 = 'http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=cidr&archiveformat='
        fetchblock6 = urlopen(url6).read()
        self.textEdit.setPlainText(fetchblock6)

    def command8(self):
        url7 = 'http://list.iblocklist.com/?list=gyisgnzbhppbvsphucsw&fileformat=cidr&archiveformat='
        fetchblock7 = urlopen(url7).read()
        self.textEdit.setPlainText(fetchblock7)

    def command9(self):
        url8 = 'http://list.iblocklist.com/?list=uwnukjqktoggdknzrhgh&fileformat=cidr&archiveformat='
        fetchblock8 = urlopen(url8).read()
        self.textEdit.setPlainText(fetchblock8)

    def command10(self):
        url9 = 'http://list.iblocklist.com/?list=llvtlsjyoyiczbkjsxpf&fileformat=cidr&archiveformat='
        fetchblock9 = urlopen(url9).read()
        self.textEdit.setPlainText(fetchblock9)

    def command11(self):
        import webbrowser
        webbrowser.open('http://www.blocklist.de/en/index.html')

    def command12(self):
        url10 = ' http://lists.blocklist.de/lists/all.txt'
        fetchblock10 = urlopen(url10).read()
        self.textEdit.setPlainText(fetchblock10)

    def command13(self):
        url11 = 'http://lists.blocklist.de/lists/ssh.txt'
        fetchblock11 = urlopen(url11).read()
        self.textEdit.setPlainText(fetchblock11)

    def command14(self):
        url12 = 'http://lists.blocklist.de/lists/mail.txt'
        fetchblock12 = urlopen(url12).read()
        self.textEdit.setPlainText(fetchblock12)

    def command15(self):
        url13 = 'http://lists.blocklist.de/lists/bruteforcelogin.txt'
        fetchblock13 = urlopen(url13).read()
        self.textEdit.setPlainText(fetchblock13)

    #ekstra commands

    def udder(self):
        self.textEdit.zoomIn()

    def odder(self):
        self.textEdit.zoomOut()

    def Author(self):
        import webbrowser
        webbrowser.open('https://twitter.com/zadow28')

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


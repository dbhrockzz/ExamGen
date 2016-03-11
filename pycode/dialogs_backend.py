from PyQt4 import QtGui,QtCore
import smalldialog
import dbase
import home

class standard_dialog(QtGui.QDialog,smalldialog.Ui_Dialog):

    def __init__(self):
        super(standard_dialog,self).__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.label.setText("Enter Standard")
        self.lineEdit.setPlaceholderText("Enter the Standard")
        self.buttonBox.accepted.connect(self.add_standard)
        self.buttonBox.rejected.connect(QtCore.QCoreApplication.instance().quit)
        self.setWindowTitle("New Standard")

    def add_standard(self):
        standard = self.lineEdit.text()
        print standard
        try:
            dbase.enter_standard(str(standard))
        except:
            print "Standard Dialog Problem"

class subject_dialog(QtGui.QDialog,smalldialog.Ui_Dialog):

    def __init__(self,standard):
        super(subject_dialog,self).__init__()
        self.standard = standard
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.label.setText("Enter Subject")
        self.lineEdit.setPlaceholderText("Enter the Subject")
        self.buttonBox.accepted.connect(self.add_subject)
        self.buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("New Subject")

    def add_subject(self):
        self.standard = str(self.standard)
        if self.standard!="Select Standard":
            subject = str(self.lineEdit.text())
            try:
                dbase.enter_subject(subject,self.standard)
            except:
                print "Subject Dialog Problem"

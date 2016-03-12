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
        self.buttonBox.rejected.connect(self.close)
        self.setWindowTitle("New Standard")

    def add_standard(self):
        standard = self.lineEdit.text()
        print standard
        try:
            dbase.enter_standard(str(standard))
        except:
            print "Standard Dialog Problem"
        self.close()

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

class edit_standard_dialog(QtGui.QDialog,smalldialog.Ui_Dialog):

    def __init__(self,standard):
        self.standard = standard
        super(edit_standard_dialog,self).__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.label.setText("Edit Standard")
        self.lineEdit.setText(str(self.standard))
        self.buttonBox.accepted.connect(self.edit_standard)
        self.buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Edit Standard")

    def edit_standard(self):
        self.new_standard = str(self.lineEdit.text())
        self.standard = str(self.standard)
        try:
            dbase.edit_standard(self.standard,self.new_standard)
        except:
            print " Edit Standard Dialog Problem"

class edit_subject_dialog(QtGui.QDialog,smalldialog.Ui_Dialog):

    def __init__(self,standard,subject):
        super(edit_subject_dialog,self).__init__()
        self.standard = standard
        self.subject = subject
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.label.setText("Edit Subject")
        self.lineEdit.setText(str(self.subject))
        self.buttonBox.accepted.connect(self.edit_subject)
        self.buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Edit Subject")

    def edit_subject(self):
        self.new_subject = str(self.lineEdit.text())
        self.standard = str(self.standard)
        self.subject = str(self.subject)
        try:
            dbase.edit_subject(self.subject,self.new_subject,self.standard)
        except:
            print " Edit Subject Dialog Problem"

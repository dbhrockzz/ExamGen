import sys
import home
from PyQt4 import QtGui,QtCore
import dbase
import dialogs_backend

class homeBackend(QtGui.QMainWindow,home.Ui_MainWindow):

    def __init__(self):
        super(homeBackend,self).__init__()
        self.setupUi(self)
        self.initUi()
        self.newPaperClicked()


    def initUi(self):
        self.new_paper.clicked.connect(self.newPaperClicked)
        self.enter_data.clicked.connect(self.enterDataClicked)
        self.edit_data.clicked.connect(self.editDataClicked)
        #self.standards_ed.currentIndexChanged.connect(self.loadSubjectsED)

    def newPaperClicked(self):
        print "New Paper Button Clicked"
        self.stackedWidget.setCurrentIndex(1)
        self.loadStandardsNP()

    def enterDataClicked(self):
        print "Enter Data Button Clicked"
        self.stackedWidget.setCurrentIndex(2)
        self.loadStandardsED()

    def editDataClicked(self):
        print "Edit Data Button Clicked"
        self.stackedWidget.setCurrentIndex(0)
        self.loadStandardsED2()

    def loadStandardsNP(self):
        self.standards_np.clear()
        temp = dbase.retrieve_standard()
        self.standards_np.addItem("Select Standard")
        if temp:
            for i in temp:
                self.standards_np.addItem(str(i))
        self.standards_np.currentIndexChanged.connect(self.loadSubjectsNP)

    def loadSubjectsNP(self):
        standard = str(self.standards_np.currentText())
        self.subjects_np.clear()
        if standard!="Select Standard":
            temp  = dbase.retrieve_subjects(standard)
            self.subjects_np.addItem("Select Subject")
            if temp:
                for i in temp:
                    self.subjects_np.addItem(i)

    def loadStandardsED(self):
        self.standards_ed.clear()
        temp = dbase.retrieve_standard()
        self.standards_ed.addItem("Select Standard")
        if temp:
            for i in temp:
                self.standards_ed.addItem(str(i))
        self.standards_ed.currentIndexChanged.connect(self.loadSubjectsED)
        self.add_standard.clicked.connect(self.add_std)
        self.add_subjects.clicked.connect(self.add_sub)

    def loadSubjectsED(self):
        standard = str(self.standards_ed.currentText())
        self.subjects_ed.clear()
        if standard!="Select Standard":
            temp  = dbase.retrieve_subjects(standard)
            self.subjects_ed.addItem("Select Subject")
            if temp:
                for i in temp:
                    self.subjects_ed.addItem(i)

    def loadStandardsED2(self):
        self.standards_ed2.clear()
        temp = dbase.retrieve_standard()
        print temp
        self.standards_ed2.addItem("Select Standard")
        if temp:
            for i in temp:
                self.standards_ed2.addItem(str(i))
        self.standards_ed2.currentIndexChanged.connect(self.loadSubjectsED2)
        self.edit_standard.clicked.connect(self.edit_std)
        self.edit_subject.clicked.connect(self.edit_sub)
        self.delete_standard.clicked.connect(self.del_std)
        self.delete_subject.clicked.connect(self.del_sub)

    def loadSubjectsED2(self):
        standard = str(self.standards_ed2.currentText())
        self.subjects_ed2.clear()
        if standard!="Select Standard":
            temp  = dbase.retrieve_subjects(str(standard))
            self.subjects_ed2.addItem("Select Subject")
            if temp:
                for i in temp:
                    self.subjects_ed2.addItem(i)

    def add_std(self):
        dialog = dialogs_backend.standard_dialog()
        dialog.show()
        dialog.done(dialog.exec_())
        self.enterDataClicked()

    def add_sub(self):
        dialog = dialogs_backend.subject_dialog(str(self.standards_ed.currentText()))
        dialog.show()
        dialog.done(dialog.exec_())
        self.enterDataClicked()

    def edit_std(self):
        dialog = dialogs_backend.edit_standard_dialog(str(self.standards_ed2.currentText()))
        dialog.show()
        dialog.done(dialog.exec_())
        self.editDataClicked()

    def edit_sub(self):
        dialog = dialogs_backend.edit_subject_dialog(str(self.standards_ed2.currentText()),str(self.subjects_ed2.currentText()))
        dialog.show()
        dialog.done(dialog.exec_())
        self.editDataClicked()

    def del_std(self):
        message = "All data of Standard " + str(self.standards_ed2.currentText())+" will be deleted. Are you sure ? "
        reply = QtGui.QMessageBox.question(self, 'Message',
            message, QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            dbase.delete_standard(str(self.standards_ed2.currentText()))
            self.editDataClicked()

    def del_sub(self):
        message = "All data of Standard " + str(self.standards_ed2.currentText())+" "+ str(self.subjects_ed2.currentText()) +" will be deleted. Are you sure ? "
        reply = QtGui.QMessageBox.question(self, 'Message',
            message, QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            dbase.delete_subject(str(self.subjects_ed2.currentText()),str(self.standards_ed2.currentText()))
            self.editDataClicked()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = homeBackend()
    ex.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

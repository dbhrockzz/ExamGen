# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

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
        MainWindow.setFixedSize(799, 545)
        #MainWindow.resize(MainWindow.sizeHint())
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 121, 551))
        self.frame.setStyleSheet(_fromUtf8("QFrame\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.863, y2:0, stop:0 rgba(0, 0, 0, 37), stop:1 rgba(255, 255, 255, 0));\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.new_paper = QtGui.QToolButton(self.frame)
        self.new_paper.setGeometry(QtCore.QRect(0, 60, 121, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.new_paper.setFont(font)
        self.new_paper.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"    color: blue;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    border-right: 3px solid blue;\n"
"}\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    border-right: 3px solid red;\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/tools/ic_fiber_new_black_48dp_2x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_paper.setIcon(icon)
        self.new_paper.setIconSize(QtCore.QSize(100, 100))
        self.new_paper.setCheckable(True)
        self.new_paper.setAutoExclusive(True)
        self.new_paper.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.new_paper.setObjectName(_fromUtf8("new_paper"))
        self.enter_data = QtGui.QToolButton(self.frame)
        self.enter_data.setGeometry(QtCore.QRect(0, 200, 121, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.enter_data.setFont(font)
        self.enter_data.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"    color: blue;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    border-right: 3px solid blue;\n"
"}\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    border-right: 3px solid red;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/tools/ic_insert_drive_file_black_48dp_2x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enter_data.setIcon(icon1)
        self.enter_data.setIconSize(QtCore.QSize(100, 100))
        self.enter_data.setCheckable(True)
        self.enter_data.setAutoExclusive(True)
        self.enter_data.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.enter_data.setObjectName(_fromUtf8("enter_data"))
        self.edit_data = QtGui.QToolButton(self.frame)
        self.edit_data.setGeometry(QtCore.QRect(0, 350, 121, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.edit_data.setFont(font)
        self.edit_data.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"    color: blue;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    border-right: 3px solid blue;\n"
"}\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    border-right: 3px solid red;\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/tools/ic_border_color_black_48dp_2x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_data.setIcon(icon2)
        self.edit_data.setIconSize(QtCore.QSize(100, 100))
        self.edit_data.setCheckable(True)
        self.edit_data.setAutoExclusive(True)
        self.edit_data.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.edit_data.setObjectName(_fromUtf8("edit_data"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 0, 681, 541))
        self.stackedWidget.setStyleSheet(_fromUtf8("QStackedWidget\n"
"{\n"
"    background-color: white;\n"
"    border: none;\n"
"}"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.edit_data_frame = QtGui.QWidget()
        self.edit_data_frame.setObjectName(_fromUtf8("edit_data_frame"))
        self.standard = QtGui.QGroupBox(self.edit_data_frame)
        self.standard.setGeometry(QtCore.QRect(20, 20, 641, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.standard.setFont(font)
        self.standard.setObjectName(_fromUtf8("standard"))
        self.standards_ed2 = QtGui.QComboBox(self.standard)
        self.standards_ed2.setGeometry(QtCore.QRect(30, 50, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.standards_ed2.setFont(font)
        self.standards_ed2.setObjectName(_fromUtf8("standards_ed2"))
        self.delete_standard = QtGui.QPushButton(self.standard)
        self.delete_standard.setGeometry(QtCore.QRect(430, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_standard.setFont(font)
        self.delete_standard.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.delete_standard.setDefault(False)
        self.delete_standard.setFlat(False)
        self.delete_standard.setObjectName(_fromUtf8("delete_standard"))
        self.edit_standard = QtGui.QPushButton(self.standard)
        self.edit_standard.setGeometry(QtCore.QRect(520, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_standard.setFont(font)
        self.edit_standard.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.edit_standard.setObjectName(_fromUtf8("edit_standard"))
        self.subject = QtGui.QGroupBox(self.edit_data_frame)
        self.subject.setGeometry(QtCore.QRect(20, 120, 641, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.subject.setFont(font)
        self.subject.setObjectName(_fromUtf8("subject"))
        self.subjects_ed2 = QtGui.QComboBox(self.subject)
        self.subjects_ed2.setGeometry(QtCore.QRect(30, 50, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subjects_ed2.setFont(font)
        self.subjects_ed2.setObjectName(_fromUtf8("subjects_ed2"))
        self.delete_subject = QtGui.QPushButton(self.subject)
        self.delete_subject.setGeometry(QtCore.QRect(430, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_subject.setFont(font)
        self.delete_subject.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.delete_subject.setDefault(False)
        self.delete_subject.setFlat(False)
        self.delete_subject.setObjectName(_fromUtf8("delete_subject"))
        self.edit_subject = QtGui.QPushButton(self.subject)
        self.edit_subject.setGeometry(QtCore.QRect(520, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_subject.setFont(font)
        self.edit_subject.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.edit_subject.setObjectName(_fromUtf8("edit_subject"))
        self.stackedWidget.addWidget(self.edit_data_frame)
        self.new_paper_frame = QtGui.QWidget()
        self.new_paper_frame.setObjectName(_fromUtf8("new_paper_frame"))
        self.standard_label = QtGui.QLabel(self.new_paper_frame)
        self.standard_label.setGeometry(QtCore.QRect(60, 50, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.standard_label.setFont(font)
        self.standard_label.setObjectName(_fromUtf8("standard_label"))
        self.standards_np = QtGui.QComboBox(self.new_paper_frame)
        self.standards_np.setGeometry(QtCore.QRect(250, 60, 331, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.standards_np.setFont(font)
        self.standards_np.setObjectName(_fromUtf8("standards_np"))
        self.subject_label = QtGui.QLabel(self.new_paper_frame)
        self.subject_label.setGeometry(QtCore.QRect(60, 160, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.subject_label.setFont(font)
        self.subject_label.setObjectName(_fromUtf8("subject_label"))
        self.subjects_np = QtGui.QComboBox(self.new_paper_frame)
        self.subjects_np.setGeometry(QtCore.QRect(250, 170, 331, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.subjects_np.setFont(font)
        self.subjects_np.setObjectName(_fromUtf8("subjects_np"))
        self.exam_label = QtGui.QLabel(self.new_paper_frame)
        self.exam_label.setGeometry(QtCore.QRect(60, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.exam_label.setFont(font)
        self.exam_label.setObjectName(_fromUtf8("exam_label"))
        self.examination = QtGui.QLineEdit(self.new_paper_frame)
        self.examination.setGeometry(QtCore.QRect(250, 280, 331, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.examination.setFont(font)
        self.examination.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"}"))
        self.examination.setObjectName(_fromUtf8("examination"))
        self.session_label = QtGui.QLabel(self.new_paper_frame)
        self.session_label.setGeometry(QtCore.QRect(60, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.session_label.setFont(font)
        self.session_label.setObjectName(_fromUtf8("session_label"))
        self.year_from = QtGui.QLineEdit(self.new_paper_frame)
        self.year_from.setGeometry(QtCore.QRect(265, 390, 21, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(10)
        self.year_from.setFont(font)
        self.year_from.setObjectName(_fromUtf8("year_from"))
        self.fromyear_label = QtGui.QLabel(self.new_paper_frame)
        self.fromyear_label.setGeometry(QtCore.QRect(250, 380, 21, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(10)
        self.fromyear_label.setFont(font)
        self.fromyear_label.setObjectName(_fromUtf8("fromyear_label"))
        self.line = QtGui.QFrame(self.new_paper_frame)
        self.line.setGeometry(QtCore.QRect(290, 390, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.toyear_label = QtGui.QLabel(self.new_paper_frame)
        self.toyear_label.setGeometry(QtCore.QRect(315, 380, 21, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(10)
        self.toyear_label.setFont(font)
        self.toyear_label.setObjectName(_fromUtf8("toyear_label"))
        self.year_to = QtGui.QLineEdit(self.new_paper_frame)
        self.year_to.setGeometry(QtCore.QRect(330, 390, 21, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(10)
        self.year_to.setFont(font)
        self.year_to.setObjectName(_fromUtf8("year_to"))
        self.stackedWidget.addWidget(self.new_paper_frame)
        self.enter_data_frame = QtGui.QWidget()
        self.enter_data_frame.setObjectName(_fromUtf8("enter_data_frame"))
        self.standard_2 = QtGui.QGroupBox(self.enter_data_frame)
        self.standard_2.setGeometry(QtCore.QRect(20, 60, 641, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.standard_2.setFont(font)
        self.standard_2.setObjectName(_fromUtf8("standard_2"))
        self.standards_ed = QtGui.QComboBox(self.standard_2)
        self.standards_ed.setGeometry(QtCore.QRect(30, 50, 291, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.standards_ed.setFont(font)
        self.standards_ed.setObjectName(_fromUtf8("standards_ed"))
        self.add_standard = QtGui.QPushButton(self.standard_2)
        self.add_standard.setGeometry(QtCore.QRect(460, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_standard.setFont(font)
        self.add_standard.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.add_standard.setDefault(False)
        self.add_standard.setFlat(False)
        self.add_standard.setObjectName(_fromUtf8("add_standard"))
        self.subject_2 = QtGui.QGroupBox(self.enter_data_frame)
        self.subject_2.setGeometry(QtCore.QRect(20, 270, 641, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.subject_2.setFont(font)
        self.subject_2.setObjectName(_fromUtf8("subject_2"))
        self.subjects_ed = QtGui.QComboBox(self.subject_2)
        self.subjects_ed.setGeometry(QtCore.QRect(30, 50, 291, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        self.subjects_ed.setFont(font)
        self.subjects_ed.setObjectName(_fromUtf8("subjects_ed"))
        self.add_subjects = QtGui.QPushButton(self.subject_2)
        self.add_subjects.setGeometry(QtCore.QRect(460, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_subjects.setFont(font)
        self.add_subjects.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.add_subjects.setDefault(False)
        self.add_subjects.setFlat(False)
        self.add_subjects.setObjectName(_fromUtf8("add_subjects"))
        self.new_question = QtGui.QPushButton(self.enter_data_frame)
        self.new_question.setGeometry(QtCore.QRect(190, 440, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Light"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.new_question.setFont(font)
        self.new_question.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #304FFE;\n"
"    border-bottom: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"    background-color: #304FFE;\n"
"}\n"
"\n"
"QPushButton::default\n"
"{\n"
"    border: none;\n"
"    border-bottom: 1px solid red;\n"
"}"))
        self.new_question.setObjectName(_fromUtf8("new_question"))
        self.stackedWidget.addWidget(self.enter_data_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Exam Generator", None))
        self.new_paper.setText(_translate("MainWindow", "NEW PAPER", None))
        self.enter_data.setText(_translate("MainWindow", "ENTER DATA", None))
        self.edit_data.setText(_translate("MainWindow", "EDIT DATA", None))
        self.standard.setTitle(_translate("MainWindow", "Standard", None))
        self.delete_standard.setText(_translate("MainWindow", "Delete", None))
        self.edit_standard.setText(_translate("MainWindow", "Edit", None))
        self.subject.setTitle(_translate("MainWindow", "Subject", None))
        self.delete_subject.setText(_translate("MainWindow", "Delete", None))
        self.edit_subject.setText(_translate("MainWindow", "Edit", None))
        self.standard_label.setText(_translate("MainWindow", "Standard", None))
        self.subject_label.setText(_translate("MainWindow", "Subject", None))
        self.exam_label.setText(_translate("MainWindow", "Examination", None))
        self.session_label.setText(_translate("MainWindow", "Session", None))
        self.fromyear_label.setText(_translate("MainWindow", "20", None))
        self.toyear_label.setText(_translate("MainWindow", "20", None))
        self.standard_2.setTitle(_translate("MainWindow", "Standard", None))
        self.add_standard.setText(_translate("MainWindow", "Add New", None))
        self.subject_2.setTitle(_translate("MainWindow", "Subject", None))
        self.add_subjects.setText(_translate("MainWindow", "Add New", None))
        self.new_question.setText(_translate("MainWindow", "Add New Question", None))

import resource

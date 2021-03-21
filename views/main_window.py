# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_sign_in = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sign_in.sizePolicy().hasHeightForWidth())
        self.label_sign_in.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_sign_in.setFont(font)
        self.label_sign_in.setObjectName("label_sign_in")
        self.verticalLayout_2.addWidget(self.label_sign_in)
        self.label_stay_updated_text = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stay_updated_text.sizePolicy().hasHeightForWidth())
        self.label_stay_updated_text.setSizePolicy(sizePolicy)
        self.label_stay_updated_text.setObjectName("label_stay_updated_text")
        self.verticalLayout_2.addWidget(self.label_stay_updated_text)
        self.lineEdit_login_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_login_email.setObjectName("lineEdit_login_email")
        self.verticalLayout_2.addWidget(self.lineEdit_login_email)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_login_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_login_password)
        self.pushButton_show_hide = QtWidgets.QPushButton(self.frame)
        self.pushButton_show_hide.setObjectName("pushButton_show_hide")
        self.horizontalLayout_2.addWidget(self.pushButton_show_hide)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_sign_in = QtWidgets.QPushButton(self.frame)
        self.pushButton_sign_in.setObjectName("pushButton_sign_in")
        self.verticalLayout_2.addWidget(self.pushButton_sign_in)
        self.pushButton_sign_out = QtWidgets.QPushButton(self.frame)
        self.pushButton_sign_out.setObjectName("pushButton_sign_out")
        self.verticalLayout_2.addWidget(self.pushButton_sign_out)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_new_to_linked_in = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_new_to_linked_in.sizePolicy().hasHeightForWidth())
        self.label_new_to_linked_in.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_new_to_linked_in.setFont(font)
        self.label_new_to_linked_in.setObjectName("label_new_to_linked_in")
        self.horizontalLayout.addWidget(self.label_new_to_linked_in)
        self.pushButton_JoinNow = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_JoinNow.sizePolicy().hasHeightForWidth())
        self.pushButton_JoinNow.setSizePolicy(sizePolicy)
        self.pushButton_JoinNow.setObjectName("pushButton_JoinNow")
        self.horizontalLayout.addWidget(self.pushButton_JoinNow)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linked in"))
        self.label_sign_in.setText(_translate("MainWindow", "Sign in"))
        self.label_stay_updated_text.setText(_translate("MainWindow", "Stay updated on your professional world"))
        self.lineEdit_login_email.setPlaceholderText(_translate("MainWindow", "Email or Phone"))
        self.lineEdit_login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_show_hide.setText(_translate("MainWindow", "show"))
        self.pushButton_sign_in.setText(_translate("MainWindow", "Sign in"))
        self.pushButton_sign_out.setText(_translate("MainWindow", "Sign out"))
        self.label_new_to_linked_in.setText(_translate("MainWindow", "New to LinkedIn?"))
        self.pushButton_JoinNow.setText(_translate("MainWindow", "Join now"))

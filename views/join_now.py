# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join_now.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 200)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_new_email = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_new_email.sizePolicy().hasHeightForWidth())
        self.label_new_email.setSizePolicy(sizePolicy)
        self.label_new_email.setObjectName("label_new_email")
        self.verticalLayout.addWidget(self.label_new_email)
        self.lineEdit_new_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_new_email.setObjectName("lineEdit_new_email")
        self.verticalLayout.addWidget(self.lineEdit_new_email)
        self.label_new_password = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_new_password.sizePolicy().hasHeightForWidth())
        self.label_new_password.setSizePolicy(sizePolicy)
        self.label_new_password.setObjectName("label_new_password")
        self.verticalLayout.addWidget(self.label_new_password)
        self.lineEdit_new_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_new_password.setText("")
        self.lineEdit_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.verticalLayout.addWidget(self.lineEdit_new_password)
        self.pushButton_agree_and_join = QtWidgets.QPushButton(self.frame)
        self.pushButton_agree_and_join.setObjectName("pushButton_agree_and_join")
        self.verticalLayout.addWidget(self.pushButton_agree_and_join)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_new_email.setText(_translate("Form", "Email"))
        self.lineEdit_new_email.setPlaceholderText(_translate("Form", "Email or Phone"))
        self.label_new_password.setText(_translate("Form", "Password (6 or more characters)"))
        self.lineEdit_new_password.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton_agree_and_join.setText(_translate("Form", "Agree and Join"))
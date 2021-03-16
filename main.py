from PyQt5 import QtWidgets, QtGui
from main_ui import Ui_MainWindow
from authentication import Authenticator
from login_exceptions import UsernameAlreadyExists, PasswordTooWeak, InvalidUsername, InvalidPassword, UserNotLoggedIn
import sys


class LoginSystem(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.authenticator = Authenticator()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        self.ui.pushButton_sign_in.clicked.connect(self.sign_in)
        self.ui.pushButton_sign_out.clicked.connect(self.sign_out)
        self.ui.pushButton_agree_and_join.clicked.connect(self.agree_and_join)
        self.ui.pushButton_show_hide.clicked.connect(self.show_hide)

    def sign_in(self):
        popup_window = QtWidgets.QMessageBox()
        popup_window.setWindowTitle("Message")
        if self.authenticator.is_logged_in(self.ui.lineEdit_login_email.text()):
            popup_window.setIcon(QtWidgets.QMessageBox.Information)
            popup_window.setText("Already logged in")
            popup_window.exec()
        else:
            try:
                self.authenticator.login(self.ui.lineEdit_login_email.text(), self.ui.lineEdit_login_password.text())
                popup_window.setIcon(QtWidgets.QMessageBox.Information)
                popup_window.setText("Login successful")
            except InvalidUsername:
                popup_window.setIcon(QtWidgets.QMessageBox.Critical)
                popup_window.setText("User does not exist")
            except InvalidPassword:
                popup_window.setIcon(QtWidgets.QMessageBox.Critical)
                popup_window.setText("Invalid password")
            finally:
                popup_window.exec()

    def sign_out(self):
        popup_window = QtWidgets.QMessageBox()
        popup_window.setWindowTitle("Message")
        try:
            self.authenticator.logout(self.ui.lineEdit_login_email.text())
            popup_window.setIcon(QtWidgets.QMessageBox.Information)
            popup_window.setText("User logged out")
            popup_window.exec()
        except InvalidUsername:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Invalid username")
            popup_window.exec()
        except UserNotLoggedIn:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("User not logged in")
            popup_window.exec()

    def agree_and_join(self):
        popup_window = QtWidgets.QMessageBox()
        popup_window.setWindowTitle("Message")

        # popup_window.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        # return_value = popup_window.exec()
        # if return_value == QtWidgets.QMessageBox.Ok:
        #     print('OK clicked')

        try:
            self.authenticator.add_user(self.ui.lineEdit_new_email.text(), self.ui.lineEdit_new_password.text())
        except UsernameAlreadyExists as ex:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Username " + ex.username + " already exists")
        except PasswordTooWeak:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Password is too weak")
        else:
            popup_window.setIcon(QtWidgets.QMessageBox.Information)
            popup_window.setText("Username added")
        finally:
            popup_window.exec()

    def show_hide(self):
        if self.ui.lineEdit_login_password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.ui.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.pushButton_show_hide.setText("show")
        else:
            self.ui.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.pushButton_show_hide.setText("hide")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = LoginSystem()
    widget.show()
    sys.exit(app.exec_())
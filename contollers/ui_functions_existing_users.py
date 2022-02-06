from contollers.main_controller import LoginSystem
import exceptions.login_exceptions as login_ex

from PyQt5 import QtWidgets


class UIFunctions(LoginSystem):
    """
    Function callbacks on the main login system window.
    """

    def sign_in(self) -> None:
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
            except login_ex.InvalidUsername:
                popup_window.setIcon(QtWidgets.QMessageBox.Critical)
                popup_window.setText("User does not exist")
            except login_ex.InvalidPassword:
                popup_window.setIcon(QtWidgets.QMessageBox.Critical)
                popup_window.setText("Invalid password")
            finally:
                popup_window.exec()

    def sign_out(self) -> None:
        popup_window = QtWidgets.QMessageBox()
        popup_window.setWindowTitle("Message")
        try:
            self.authenticator.logout(self.ui.lineEdit_login_email.text())
            popup_window.setIcon(QtWidgets.QMessageBox.Information)
            popup_window.setText("User logged out")
        except login_ex.InvalidUsername:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Invalid username")
        except login_ex.UserNotLoggedIn:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("User not logged in")
        finally:
            popup_window.exec()

    def show_hide(self) -> None:
        if self.ui.lineEdit_login_password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.ui.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.pushButton_show_hide.setText("show")
        else:
            self.ui.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.pushButton_show_hide.setText("hide")
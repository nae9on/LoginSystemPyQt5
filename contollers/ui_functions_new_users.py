from contollers.main_controller import LoginSystem
import exceptions.login_exceptions as login_ex
from PyQt5 import QtWidgets


class UIFunctions(LoginSystem):
    def agree_and_join(self):
        popup_window = QtWidgets.QMessageBox()
        popup_window.setWindowTitle("Message")

        # popup_window.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        # return_value = popup_window.exec()
        # if return_value == QtWidgets.QMessageBox.Ok:
        #     print('OK clicked')

        try:
            self.authenticator.add_user(self.ui.lineEdit_new_email.text(), self.ui.lineEdit_new_password.text())
        except login_ex.UsernameAlreadyExists as ex:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Username " + ex.username + " already exists")
        except login_ex.PasswordTooWeak:
            popup_window.setIcon(QtWidgets.QMessageBox.Critical)
            popup_window.setText("Password is too weak")
        else:
            popup_window.setIcon(QtWidgets.QMessageBox.Information)
            popup_window.setText("Username added")
        finally:
            popup_window.exec()
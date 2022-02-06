from contollers.main_controller import LoginSystem
from contollers.join_now_controller import JoinNow
from services.authentication import Authenticator

from PyQt5 import QtWidgets

import sys


class MainApp(QtWidgets.QApplication):
    """
    Sub-classing QApplication to create an application object. Think of this as a circuit board of the application
    where all the components will be mounted and loosely connected together.
    """

    def __init__(self, argv):
        super().__init__(argv)

        # Service component
        self.authenticator = Authenticator()

        # Main login component
        self.login_system = LoginSystem(self.authenticator)
        self.login_system.show()

        # Join now component
        self.join_now = JoinNow(self.authenticator)

        # Loose coupling
        # Connect the join_now_requested signal with the show() public slot
        self.login_system.join_now_requested.connect(self.clear_join_now_screen)
        self.login_system.close_join_now_screen.connect(self.join_now.close)

    def clear_join_now_screen(self):
        self.join_now.ui.lineEdit_new_email.clear()
        self.join_now.ui.lineEdit_new_password.clear()
        self.join_now.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())
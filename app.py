from contollers.main_controller import LoginSystem
from PyQt5 import QtWidgets
import sys


class MainApp(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.widget = LoginSystem()
        self.widget.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())
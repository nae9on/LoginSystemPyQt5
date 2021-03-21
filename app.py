from contollers.main_controller import LoginSystem
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = LoginSystem()
    widget.show()
    sys.exit(app.exec_())
from views.main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore


# The main component was created as a QMainWindow in QT Designer
# Therefore, it should extend a QMainWindow
class LoginSystem(QtWidgets.QMainWindow):

    # Create a new external signal to request join now component widget
    # bool because clicked signal on a push button sends a boolean
    join_now_requested = QtCore.pyqtSignal(bool)

    def __init__(self, authenticator, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.authenticator = authenticator

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._connect_signals_and_slots()

    def _connect_signals_and_slots(self):
        # Import here instead of top of this module to avoid ImportError due to circular (or cyclic) imports
        from contollers import ui_functions_existing_users as uif_existing
        self.ui.pushButton_sign_in.clicked.connect(lambda: uif_existing.UIFunctions.sign_in(self))
        self.ui.pushButton_sign_out.clicked.connect(lambda: uif_existing.UIFunctions.sign_out(self))
        self.ui.pushButton_show_hide.clicked.connect(lambda: uif_existing.UIFunctions.show_hide(self))

        # Connect the clicked button signal to the join_now_requested signal
        self.ui.pushButton_JoinNow.clicked.connect(self.join_now_requested)
from services.authentication import Authenticator

from views.main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore


# The main component was created as a QMainWindow in Qt Designer
# Therefore, it should extend a QMainWindow
class LoginSystem(QtWidgets.QMainWindow):
    """
    Controls the actions that will follow when a user clicks any button on the main login system window.
    """

    # Create a new external signal to request join now component widget
    # bool because clicked signal on a push button sends a boolean
    join_now_requested = QtCore.pyqtSignal(bool)

    close_join_now_screen = QtCore.pyqtSignal()

    def __init__(self, authenticator: Authenticator, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.authenticator = authenticator

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._connect_signals_and_slots()

    def _connect_signals_and_slots(self) -> None:
        # Import here instead of top of this module to avoid ImportError due to circular (or cyclic) imports
        from contollers import ui_functions_existing_users as uif_existing
        self.ui.pushButton_sign_in.clicked.connect(lambda: uif_existing.UIFunctions.sign_in(self))
        self.ui.pushButton_sign_out.clicked.connect(lambda: uif_existing.UIFunctions.sign_out(self))
        self.ui.pushButton_show_hide.clicked.connect(lambda: uif_existing.UIFunctions.show_hide(self))

        # Connect the clicked button signal to the join_now_requested signal
        self.ui.pushButton_JoinNow.clicked.connect(self.join_now_requested)

    def closeEvent(self, event):
        """Cleanup code after the main window is closed."""
        self.close_join_now_screen.emit()
        event.accept()  # event.ignore() try this for fun :)
from services.authentication import Authenticator
from views.join_now import Ui_Form

from PyQt5 import QtWidgets


# The join now component was created as a QWidget in Qt Designer
# Therefore, it should extend a QWidget
class JoinNow(QtWidgets.QWidget):
    """
    Controls the actions that will follow when a user clicks join now button.
    """

    def __init__(self, authenticator: Authenticator, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.authenticator = authenticator

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._connect_signals_and_slots()

    def _connect_signals_and_slots(self):
        # Import here instead of top of this module to avoid ImportError due to circular (or cyclic) imports
        from contollers import ui_functions_new_users as uif_new
        self.ui.pushButton_agree_and_join.clicked.connect(lambda: uif_new.UIFunctions.agree_and_join(self))
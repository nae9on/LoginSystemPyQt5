from views.main_window import Ui_MainWindow
from services.authentication import Authenticator
from PyQt5 import QtWidgets


class LoginSystem(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.authenticator = Authenticator()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        from contollers import ui_functions_existing_users as uif_existing
        from contollers import ui_functions_new_users as uif_new
        self.ui.pushButton_sign_in.clicked.connect(lambda: uif_existing.UIFunctions.sign_in(self))
        self.ui.pushButton_sign_out.clicked.connect(lambda: uif_existing.UIFunctions.sign_out(self))
        self.ui.pushButton_agree_and_join.clicked.connect(lambda: uif_new.UIFunctions.agree_and_join(self))
        self.ui.pushButton_show_hide.clicked.connect(lambda: uif_existing.UIFunctions.show_hide(self))

from PyQt6.QtCore import  PYQT_SIGNAL
from PyQt6.QtWidgets import  QMainWindow
from ..ui.main_tour_ui import Ui_MainWindow as UI_Main_Tour

class MainTour(QMainWindow,UI_Main_Tour):

    def __int__(self):
        super().__init__()
        self.setupUi(self)
import sys

from PyQt6 import QtWidgets

import login_form_ui

class LogginForm(QtWidgets.QMainWindow,login_form_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)






if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = LogginForm()
  window.show()
  app.exec()
  window = LogginForm()

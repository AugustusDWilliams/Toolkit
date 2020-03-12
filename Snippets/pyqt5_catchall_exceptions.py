import os
import sys
import traceback
from loguru import logger
from PyQt5 import QtWidgets
os.environ['CONFIG'] = 'production'


def custom_excepthook(type, value, tback):
    msg_box = QtWidgets.QMessageBox(app.ui)
    msg_box.setText("App Crashed!")
    err = ''.join(traceback.format_exception(type, value, tback))
    sys.__excepthook__(type, value, tback)
    if os.environ['CONFIG'] == "production":
        logger.error(err)
        msg_box.exec()
    

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv[1:])
    app.exec()

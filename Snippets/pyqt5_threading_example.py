import sys
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from datetime import datetime, timedelta


class AppThread(QtCore.QThread):

    def __init__(self, function, args=None, interval=None):
        super().__init__()
        self.function = function
        self.args = args
        self.interval = interval
        self._abort = False
        self._thread_running = False

    def run(self):
        if self.interval:
            while not self._abort:
                if self._thread_running:
                    if self.args:
                        self.function(self.args)
                    else:
                        self.function()
                    self.sleep(self.interval)
            self.exit()
        else:
            if self.args:
                self.function(self.args)
            else:
                self.function()

    def shutdown(self):
        self._abort = True

    def exit(self):
        self._abort = False


class App(QtWidgets.QApplication):
    sig_main_app_func = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__(sys.argv[1:])
        self.timer = QtCore.QTimer()
        self.ui = QtWidgets.QMainWindow()
        self.sig_main_app_func.connect(self.main_app_func)
        #self.ui = UI(self)
        self.ui.show()
        self.start_threads()

    def main_app_func(self):
        print(datetime.now())

    def start_threads(self):
        self.mainthread = AppThread(self.main_app_func)#(self.sig_main_app_func.emit)
        self.timer.setInterval(2*1000)
        self.timer.timeout.connect(self.mainthread.start)
        self.timer.start()

    def stop_threads(self):
        self.timer.stop()


if __name__ == "__main__":
    app = App()
    app.exec()

import PyQt6.QtWidgets as qtw




class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("gui")
        self.show()


class GUI:
    def run(self):
        app = qtw.QApplication([])
        mw = MainWindow()
        app.exec()
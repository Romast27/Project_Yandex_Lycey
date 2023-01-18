import sys

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox


class Example(QMainWindow):
    def __init__(self, answer):
        self.finished = None        
        super().__init__()
        self.initUI(answer)

    def initUI(self, answer):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
        while not fname:
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
        with open(fname, 'r') as f:
            read_data = f.read()
        try:
            exec(read_data, globals())
            while answer != result:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка\nНе правильный пароль")
                msg.setWindowTitle("Error")
                msg.exec_()
                fname = QFileDialog.getOpenFileName(
                    self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
                while not fname:
                    fname = QFileDialog.getOpenFileName(
                        self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
                with open(fname, 'r') as f:
                    read_data = f.read()
                exec(read_data, globals())
            self.finished = True
            self.close()
            return
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка\nОшибка в работе программы")
            msg.setWindowTitle("Error")
            msg.exec_()
            self.finished = False
            self.close()
            return

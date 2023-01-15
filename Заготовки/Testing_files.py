import sys

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox


class Example(QMainWindow):
    def __init__(self, answer):
        self.finished = None        
        super().__init__()
        self.initUI(answer)

    def initUI(self, answer):
        fname = None
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
        while not fname:
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]                
        with open(fname, 'r') as f:
            read_data = f.read()
        compiled_file = compile(read_data, fname, mode='exec')
        print('*')
        print(exec(compiled_file))
        print('**')
        print(answer)        
        while answer != exec(compiled_file):
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
            compiled_file = compile(read_data, fname, mode='exec')
            print(exec(compiled_file), answer, exec(compiled_file) == answer)
        self.finished = True

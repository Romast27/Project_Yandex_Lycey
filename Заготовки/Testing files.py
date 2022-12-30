import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл с решением', '', 'Python файл (*.py)')[0]
        with open(fname, 'r') as f:
            read_data = f.read()
        compiled_file = compile(read_data, fname, mode='exec')
        print(exec(compiled_file))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

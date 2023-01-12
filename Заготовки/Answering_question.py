from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox


class AnsweringQuestion(QDialog):
    def __init__(self, answer, question):
        super().__init__()
        uic.loadUi('Answering question.ui', self)
        self.label.setText(question)
        self.answer = answer
        self.finished = None
        self.lineEdit.setPlaceholderText('Ответ:')
        self.widget.setStyleSheet("QWidget {background-color: #6924ff; color: white; style-text: bold;}"
                                  " QPushButton { background-color: #242fff; color: white;}"
                                  " QLineEdit { background-color: white;color: black;}")
        self.btn_1.clicked.connect(self.ok)
        self.btn_2.clicked.connect(self.cancel)

    def ok(self):
        if self.lineEdit.text() == self.answer:
            self.finished = True
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка\nНе правильный ответ")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

    def cancel(self):
        self.close()

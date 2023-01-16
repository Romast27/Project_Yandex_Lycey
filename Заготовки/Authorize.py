import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QDialog


class Authorize(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorize.ui', self)
        self.authorized = None
        self.edit_password.setPlaceholderText('Не менее 8 символов')
        self.pushButton_enter.clicked.connect(self.enter_account)
        self.pushButton_create.clicked.connect(self.create_account)
        self.con = sqlite3.connect("project_db.sqlite")
        self.cur = self.con.cursor()
        self.widget.setStyleSheet("QWidget {background-color: #6924ff; color: white; style-text: bold;}"
                                  " QPushButton { background-color: #242fff; color: white;}"
                                  " QLineEdit { background-color: white;color: black;}")

    def create_account(self):
        self.name = self.edit_login.text()
        self.password = self.edit_password.text()
        if len(self.password) < 8:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка\nНе правильный пароль")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        sql_names = "SELECT login FROM Players WHERE login=?"
        if self.cur.execute(sql_names, (login := self.name,)).fetchone():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка\nТакой логин уже существует")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        sql = "INSERT INTO Players(login, password, current_level) VALUES(?, ?, ?)"
        self.cur.execute(sql, (login := self.name, password := self.password, current_level := 1))
        self.id = self.cur.execute("SELECT MAX(id) FROM Players")
        self.authorized = self.name
        self.con.commit()
        self.con.close()
        self.close()

    def enter_account(self):
        self.name = self.edit_login.text()
        self.password = self.edit_password.text()
        sql = "SELECT id FROM Players WHERE login=? AND password=?"
        info = self.cur.execute(sql, (login := self.name, password := self.password)).fetchall()
        if info:
            sql = "SELECT id, current_level FROM Players WHERE login=?"
            info = self.cur.execute(sql, (login := self.name,)).fetchone()
            self.id = info[0]
            self.authorized = self.name
            self.level = info[1]
            self.id = self.cur.execute("SELECT MAX(id) FROM Players")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка\nНеправильный логин или пароль")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        self.close()
        self.con.close()

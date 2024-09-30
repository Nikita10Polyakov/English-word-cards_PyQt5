from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo_app import app


win_start = QWidget()

win_start.resize(500, 500)
win_start.move(300, 300)
win_start.setWindowTitle('Start Menu')

font = QFont('Arial', 14)
font.setBold(True)


btn_first_level = QPushButton('1 рівень')
btn_second_level = QPushButton('2 рівень')
btn_third_level = QPushButton('3 рівень')


btn_first_level.setStyleSheet("background-color: #90ee90 ; color: black; padding:  10px; margin-bottom: 100px;")
btn_second_level.setStyleSheet("background-color: #f7da76 ; color: black; padding:  10px; margin-bottom: 100px;")
btn_third_level.setStyleSheet("background-color: #f0807f ; color: black; padding:  10px; margin-bottom: 100px;")

layout_start = QVBoxLayout()

Vitaiu = QLabel('Вітаю в Memory Card!')
Oberit = QLabel('Оберіть рівень складності')

Vitaiu.setFont(font)

layout_start.addWidget(Vitaiu, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_start.addWidget(Oberit, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_startLine = QHBoxLayout()
layout_startLine.addWidget(btn_first_level)
layout_startLine.addWidget(btn_second_level)
layout_startLine.addWidget(btn_third_level)

layout_start.addLayout(layout_startLine)







win_start.setLayout(layout_start)

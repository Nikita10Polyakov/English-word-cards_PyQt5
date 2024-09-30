from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo_app import app 
from memo_edit_layout import layout_form  
from memo_card_layout import layout_card




list_questions = QListView()
font = QFont('Arial', 12)
list_questions.setFont(font)
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Нове питання')
btn_delete = QPushButton('Видалити питання')
btn_start = QPushButton('Почати тренування')
 
btn_add.setStyleSheet("background-color: lightblue; color: black;")
btn_delete.setStyleSheet("background-color: lightcoral; color: black;")
btn_start.setStyleSheet("background-color: lightgreen ; color: black;")


font = QFont('Arial', 14)  # Создать шрифт Arial размером 14
font.setBold(True)
btn_add.setFont(font)
btn_delete.setFont(font)
btn_start.setFont(font)


main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()

btn_back = QPushButton('Повернутися')
btn_back.setFont(font)
btn_back.setStyleSheet("background-color: #c98cf5 ; color: black;")


layout_line0 = QHBoxLayout()
layout_line0.addWidget(btn_back)

layout_main.addLayout(layout_line0)

layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)



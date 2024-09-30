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
from PyQt5.QtGui import QFont

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Не правильний варіант №1:', txt_Wrong1)
layout_form.addRow('Не правильний варіант №2', txt_Wrong2)
layout_form.addRow('Не правильний варіант №3:', txt_Wrong3)

font = QFont('Arial', 12)
txt_Question.setFont(font)
txt_Answer.setFont(font)
txt_Wrong1.setFont(font)
txt_Wrong2.setFont(font)
txt_Wrong3.setFont(font)


for i in range(layout_form.rowCount()):
        label = layout_form.itemAt(i, QFormLayout.LabelRole).widget()
        if label:
                label.setFont(font)


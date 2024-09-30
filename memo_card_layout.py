''' Окно для карточки вопроса '''
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


btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('')


btn_Menu.setStyleSheet("background-color: lightblue; color: black;")
btn_Sleep.setStyleSheet("background-color: lightgreen; color: black;")
btn_OK.setStyleSheet("background-color: #DDA0DD; color: black;")


font = QFont('Arial', 12)
font.setBold(False)
ans_font = QFont('Arial', 12)
ans_font.setBold(True)
btn_Menu.setFont(font)
btn_Sleep.setFont(font)
btn_OK.setFont(font)
lb_Question.setFont(font)



btn_Menu.setFixedSize(100, 50)
btn_Sleep.setMinimumSize(100, 50)
btn_OK.resize(100, 50)


RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

RadioGroupBox.setFont(font)

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)




AnsGroupBox = QGroupBox("Результат тестування")
AnsGroupBox.setFont(ans_font)
lb_Result = QLabel('')
lb_Correct = QLabel('')
lb_Result.setFont(font)
lb_Correct.setFont(font)



layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

ResGroupBox = QGroupBox("Результат тестування")
ResGroupBox.setFont(ans_font)
lb_FinalResult = QLabel('')
lb_Right = QLabel('')

layout_final_res = QVBoxLayout()
layout_final_res.addWidget(lb_FinalResult)
ResGroupBox.setLayout(layout_final_res)
ResGroupBox.hide()


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
Min_label = QLabel('хвилин')
Min_label.setFont(font)
layout_line1.addWidget(Min_label)


layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)
layout_line3.addWidget(ResGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result(ans_quantity):
    RadioGroupBox.hide()
    ResGroupBox.hide()
    AnsGroupBox.show()
    if ans_quantity == 10:
        text = "Закінчити тестування"
    else:
        text = "Наступне питання"
    btn_OK.setText(text)


def show_question(right_answers):

    if lb_Result.text() == "Правильно ✅":
        if right_answers == 0 and lb_Right.text() == "":
            right_answers = right_answers + 1
            lb_Right.setText(str(right_answers))

        else:
            right_answers = lb_Right.text()
            right_answers = str(right_answers)
            right_answers = int(right_answers)
            right_answers = right_answers + 1
            lb_Right.setText(str(right_answers))

    AnsGroupBox.hide()
    ResGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_final_result():
    right_answers = lb_Right.text()
    text = str(right_answers) + " из 10"
    lb_FinalResult.setText(text)
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResGroupBox.show()
    btn_OK.setText('Повторити тест')
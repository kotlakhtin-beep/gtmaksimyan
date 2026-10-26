from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, 
    QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QGroupBox
)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = [
    Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Английский"),
    Question("Какого цвета нет на флаге России", "Зеленый", "Белый", "Синий", "Красный"),
    Question("На каком материке расположен Египет", "Африка", "Азия", "Европа", "Южная Америка"),
    Question("Столица Австралии", "Канберра", "Сидней", "Мельбурн", "Брисбен"),
    Question("Самая большая планета Солнечной системы", "Юпитер", "Сатурн", "Марс", "Земля"),
    Question("В каком году человек впервые полетел в космос", "1961", "1957", "1969", "1975"),
    Question("Какая химическая формула у воды", "H2O", "CO2", "O2", "NaCl"),
    Question("Самая длинная река в мире", "Нил", "Амазонка", "Миссисипи", "Янцзы"),
    Question("Сколько континентов на Земле", "6", "5", "7", "4"),
    Question("Какая планета ближе всего к Солнцу", "Меркурий", "Венера", "Марс", "Земля")
]

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Memo Card")
main_win.resize(400, 300)

question = QLabel("Самый сложный вопрос в мире!")
btn_answer = QPushButton("Ответить")

rbtn_1 = QRadioButton("Вариант 1")
rbtn_2 = QRadioButton("Вариант 2")
rbtn_3 = QRadioButton("Вариант 3")
rbtn_4 = QRadioButton("Вариант 4")

radio_group = QButtonGroup()
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

layout_ans1.addWidget(rbtn_1)
layout_ans1.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3)
layout_ans2.addWidget(rbtn_4)

layout_answers = QVBoxLayout()
layout_answers.addLayout(layout_ans1)
layout_answers.addLayout(layout_ans2)

RadioGroupBox = QGroupBox("Варианты ответов")
RadioGroupBox.setLayout(layout_answers)

lb_Result = QLabel("прав ты или нет?")
lb_Correct = QLabel("ответ будет тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)

ResultGroupBox = QGroupBox("Результат теста")
ResultGroupBox.setLayout(layout_res)
ResultGroupBox.hide()

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(ResultGroupBox)
layout_main.addWidget(btn_answer, alignment=Qt.AlignCenter)

layout_main.setContentsMargins(20, 20, 20, 20)
layout_main.setSpacing(15)

main_win.setLayout(layout_main)

def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    btn_answer.setText("Следующий вопрос")

def show_question():
    ResultGroupBox.hide()
    RadioGroupBox.show()
    btn_answer.setText("Ответить")
    radio_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

score = 0
total = 0

def show_correct(res):
    global score, total
    lb_Result.setText(res)
    if res == "Правильно!":
        score += 1
    total += 1
    
    # Вывод статистики и рейтинга происходит при нажатии «Ответить»
    print('Статистика')
    print('-Всего вопросов:', total)
    print('-Правильных ответов:', score)
    if total > 0:
        print(f'Рейтинг: {(score / total) * 100} %')

    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def start_test():
    if btn_answer.text() == "Ответить":
        check_answer()
    else:
        next_question()

btn_answer.clicked.connect(start_test)

next_question()
main_win.show()
app.exec_()

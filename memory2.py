from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

# ---------- Хранение вопросов ----------
class Question():
    """Структура вопроса: текст, правильный ответ и три неправильных."""
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# Хранение всех вопросов
questions_list = []
questions_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
questions_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))

# ---------- Приложение и окно ----------
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 400)

# ---------- Создание виджетов ----------
question = QLabel('')
btn_ok = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup = QButtonGroup()
for button in (rbtn_1, rbtn_2, rbtn_3, rbtn_4):
    RadioGroup.addButton(button)

# ---------- Расположение ответов ----------
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

# ---------- Расположение элементов окна ----------
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

# ---------- Главный лэйаут ----------
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

main_win.setLayout(layout_card)

# ---------- Отображение случайного вопроса ----------
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    """Записать вопрос и перемешанные ответы в виджеты формы."""
    shuffle(answers)
    answers[0].setText(q.right_answer)  # answers[0] всегда правильный
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)

def next_question():
    """Выбрать случайный вопрос из списка и показать его."""
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])

next_question()
main_win.show()
app.exec_()

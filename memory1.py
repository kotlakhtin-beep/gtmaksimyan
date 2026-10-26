from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, 
    QVBoxLayout, QGroupBox
)

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Memo Card")
main_win.resize(400, 300)

question = QLabel("Самый сложный вопрос в мире!")

lb_Result = QLabel("Правильно/Неправильно")
lb_Correct = QLabel("Правильный ответ")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)

ResultGroupBox = QGroupBox("Результат теста")
ResultGroupBox.setLayout(layout_res)

btn_next = QPushButton("Следующий вопрос")

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(ResultGroupBox)
layout_main.addWidget(btn_next, alignment=Qt.AlignCenter)

layout_main.setContentsMargins(20, 20, 20, 20)
layout_main.setSpacing(15)

main_win.setLayout(layout_main)

main_win.show()
app.exec_()

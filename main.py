from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Вікторина')
main_win.resize(500, 200)

lbl_instr = QLabel('Питання')
rbtn_1 = QRadioButton("Відповідь 1")
rbtn_2 = QRadioButton("Відповідь 2")
rbtn_3 = QRadioButton("Відповідь 3")
rbtn_4 = QRadioButton("Відповідь 4")

main_layout = QVBoxLayout()
main_layout.addWidget(lbl_instr)

row1_layout = QHBoxLayout()
row2_layout = QHBoxLayout()

row1_layout.addWidget(rbtn_1)
row1_layout.addWidget(rbtn_2)

row2_layout.addWidget(rbtn_3)
row2_layout.addWidget(rbtn_4)

main_layout.addLayout(row1_layout)
main_layout.addLayout(row2_layout)

def show_right():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle('Результат')
    win_info.setText('Вірно!')
    win_info.show()


def show_wrong():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle('Результат')
    win_info.setText('Невірно!')
    win_info.show()


rbtn_1.clicked.connect(show_wrong)
rbtn_2.clicked.connect(show_right)
rbtn_3.clicked.connect(show_wrong)
rbtn_4.clicked.connect(show_wrong)

main_win.setLayout(main_layout)
main_win.show()
app.exec()
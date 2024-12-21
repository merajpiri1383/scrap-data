import sys
from page import code_3_month,code_month_31,code_year,code_month
from main import get_by_date
from threading import Thread
import multiprocessing
from time import sleep
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QMessageBox
)

from PyQt5.QtGui import (
    QFont
)
import re


date_re = re.compile("^[0-9]{4}/[0-9]{2}/[0-9]{2}$")



class MainWindow (QMainWindow) : 

    def __init__ (self) : 
        super().__init__()
        self.setWindowTitle("Scraping")
        self.setGeometry(100,100,400,300)
        self.selected_codes = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout 
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # change font 
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)

        # row 1 

        row_1 = QHBoxLayout()

        # check boxed 

        self.check_box_30 = QCheckBox("گزارش ماهیانه 30")
        self.check_box_31 = QCheckBox("گزارش ماهیانه 31")
        self.checK_box_10 = QCheckBox("گزارش سه ماه")
        self.check_box_52 = QCheckBox("گزارش سالیانه")

        # set font 
        self.checK_box_10.setFont(font)
        self.check_box_30.setFont(font)
        self.check_box_52.setFont(font)
        self.check_box_31.setFont(font)

        # check box handeler 
        self.check_box_30.stateChanged.connect(self.update_check_boxes)
        self.check_box_31.stateChanged.connect(self.update_check_boxes)
        self.checK_box_10.stateChanged.connect(self.update_check_boxes)
        self.check_box_52.stateChanged.connect(self.update_check_boxes)


        row_1.addWidget(self.check_box_30)
        row_1.addWidget(self.check_box_31)
        row_1.addWidget(self.checK_box_10)
        row_1.addWidget(self.check_box_52)


        # row 2 

        row_2 = QHBoxLayout()

        label_from_date = QLabel("از تاریخ")
        label_from_date.setFont(font)
        self.text_edit_from_date = QTextEdit()
        self.text_edit_from_date.setFixedSize(150,30)
        self.text_edit_from_date.setFont(font)
        self.text_edit_from_date.setPlaceholderText("yyyy/mm/dd")

        label_to_date = QLabel("تا تاریخ")
        label_to_date.setFont(font)

        self.text_edit_to_date = QTextEdit()
        self.text_edit_to_date.setFixedSize(150,30)
        self.text_edit_to_date.setFont(font)
        self.text_edit_to_date.setPlaceholderText("yyyy/mm/dd")

        row_2.addWidget(label_from_date)
        row_2.addWidget(self.text_edit_from_date)
        row_2.addWidget(label_to_date)
        row_2.addWidget(self.text_edit_to_date)


        self.layout.addLayout(row_1)
        self.layout.addLayout(row_2)
        


        # start button

        self.start_button = QPushButton("Start")
        self.layout.addWidget(self.start_button)
        
        self.start_button.clicked.connect(self.start_button_handeler)
        
    def show_invalid_date_alert (self) : 

        alert = QMessageBox(self)
        alert.setWindowTitle("Alert")
        alert.setText("فرمت اشتباه تاریخ")
        alert.setIcon(QMessageBox.Critical) 
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()

    
    def update_check_boxes (self) :
        if self.checK_box_10.isChecked() : 
            self.selected_codes.append(code_3_month)
        if self.check_box_30.isChecked() : 
            self.selected_codes.append(code_month)
        if self.check_box_31.isChecked() : 
            self.selected_codes.append(code_month_31)
        if self.check_box_52.isChecked() : 
            self.selected_codes.append(code_year)
    
    def start(self) : 
        print("start")
        # check format date 
        if not date_re.findall(self.text_edit_from_date.toPlainText()) : 
            self.show_invalid_date_alert()

        elif not date_re.findall(self.text_edit_to_date.toPlainText()) : 
            self.show_invalid_date_alert()   
        else : 
            self.task = multiprocessing.Process(
                target=get_by_date,
                args=[
                    self.text_edit_from_date.toPlainText(),
                    self.text_edit_to_date.toPlainText(),
                    self.selected_codes,
                ]
            )
            self.task.start()

    def stop (self) : 
        print("stop")
        self.task.terminate()

    def start_button_handeler (self) : 
        if self.start_button.text() == "Start" : 
            self.start()
            self.start_button.setText("Stop")
        elif self.start_button.text() == "Stop" : 
            self.stop()
            self.start_button.setText("Start")
        




if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
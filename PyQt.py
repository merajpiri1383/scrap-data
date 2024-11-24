import sys
from page import code_3_month,code_month_31,code_year,code_month
from main import run_script
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QHBoxLayout,
    QSpinBox,
    QLabel
)

from PyQt5.QtGui import (
    QFont
)


class MainWindow (QMainWindow) : 

    def __init__ (self) : 
        super().__init__()
        self.setWindowTitle("Scraping")
        self.setGeometry(100,100,400,300)
        self.selected_codes = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout 
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

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

        self.from_number_input = QSpinBox()
        self.from_number_input.setRange(1,20)
        self.from_number_input.setFixedSize(50,40)
        self.from_number_input.setFont(font)

        lable_from_number_input = QLabel("از صفحه ")
        lable_from_number_input.setFont(font)


        self.to_number_input = QSpinBox()
        self.to_number_input.setRange(1,50)
        self.to_number_input.setFixedSize(50,40)
        self.to_number_input.setFont(font)

        lable_to_number_input = QLabel("تا صفحه")
        lable_to_number_input.setFont(font)



        row_2.addWidget(self.from_number_input)
        row_2.addWidget(lable_from_number_input)
        row_2.addWidget(self.to_number_input)
        row_2.addWidget(lable_to_number_input)


        layout.addLayout(row_1)
        layout.addLayout(row_2)


        # start button

        start_button = QPushButton("Start Scraping ...")
        layout.addWidget(start_button)
        start_button.clicked.connect(self.start_button_handeler)
        

    
    def update_check_boxes (self) :
        if self.checK_box_10.isChecked() : 
            self.selected_codes.append(code_3_month)
        if self.check_box_30.isChecked() : 
            self.selected_codes.append(code_month)
        if self.check_box_31.isChecked() : 
            self.selected_codes.append(code_month_31)
        if self.check_box_52.isChecked() : 
            self.selected_codes.append(code_year)
    

    def start_button_handeler (self) : 
        run_script(
            self.from_number_input.value(),
            self.to_number_input.value(),
            self.selected_codes,
            )




if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
import sys
import PySide6.QtWidgets as Qw
import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f: 
        data = json.load(f) 
    return data

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = load_json('data.json')
button_set = (327,140)
button_size = (60,30)
window_size = (540,220)

class SubElement(Qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(window_size[0], window_size[1])
        self.center()
        self.setWindowTitle("サブ要素の追加")  
        
        label_list = Qw.QLabel("追加するリスト名", self)
        label_list.setGeometry(50, 20, 200, 30)

        self.combo_box_list = Qw.QComboBox(self)
        self.combo_box_list.setGeometry(50, 50, 195, 30)
        self.combo_box_list.addItems(data["list_data"][1:])
        
        label_main = Qw.QLabel("紐づけるメイン要素", self)
        label_main.setGeometry(50, 80, 200, 30)

        self.combo_box_main = Qw.QComboBox(self)
        self.combo_box_main.setGeometry(50, 110, 195, 30)
        self.combo_box_main.addItems(data["element_main"])

        self.input_field = Qw.QLineEdit(self)
        self.input_field.setPlaceholderText("要素名を入力してください")
        self.input_field.setGeometry(295,110,190,28)
        self.input_field.setFocus()

        self.btn_decide = Qw.QPushButton('決定',self)
        self.btn_decide.setGeometry(button_set[0],button_set[1],button_size[0],button_size[1])
        self.btn_decide.clicked.connect(self.btn_decide_clicked)

        self.btn_cancel = Qw.QPushButton('中止',self)
        self.btn_cancel.setGeometry(button_set[0]+100,button_set[1],button_size[0],button_size[1])
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def btn_decide_clicked(self):
      selected_list = self.combo_box_list.currentText()
      selected_main = self.combo_box_main.currentText()
      for i in range(len(data["list_data"])-1):
        for j in range(len(data["element_main"])):
          if data["list_data"][i+1] == selected_list and data["element_main"][j] == selected_main:
            data[f"element_sub{i+1}"][j] = self.input_field.text()
            save_json('data.json', data)
            self.close()

    def btn_cancel_clicked(self):
        self.close()

    def center(self):
        screen = Qw.QApplication.primaryScreen()
        screen_rect = screen.geometry()
        window_rect = self.geometry()
        x = (screen_rect.width() - window_rect.width()) // 2
        y = (screen_rect.height() - window_rect.height()) // 2
        self.setGeometry(x, y-30, window_rect.width(), window_rect.height())

if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = SubElement()
    main_window.show()
    sys.exit(app.exec())
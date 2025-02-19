import sys
import PySide6.QtCore as Qc
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
button_set = (327,80)
button_size = (60,30)

class AddList(Qw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("リスト名の変更")  # ウィンドウのタイトル
        self.setGeometry(150, 150, 540, 120)  # ウィンドウの位置とサイズ
        
        # 何かシンプルなラベルを追加
        label = Qw.QLabel("変更するリスト名", self)
        label.setGeometry(50, 20, 200, 30)

        self.combo_box = Qw.QComboBox(self)
        self.combo_box.setGeometry(50, 50, 195, 30)  # 位置とサイズを指定
        self.combo_box.addItems(data["list_data"])

        self.input_field = Qw.QLineEdit(self)
        self.input_field.setPlaceholderText("リスト名を入力してください")
        self.input_field.setGeometry(295,50,190,28)
        self.input_field.setFocus()

        self.btn_decide = Qw.QPushButton('決定',self)
        self.btn_decide.setGeometry(button_set[0],button_set[1],button_size[0],button_size[1])
        self.btn_decide.clicked.connect(self.btn_decide_clicked)

        self.btn_cancel = Qw.QPushButton('中止',self)
        self.btn_cancel.setGeometry(button_set[0]+100,button_set[1],button_size[0],button_size[1])
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def btn_decide_clicked(self):
      selected_item = self.combo_box.currentText()
      for i in range(len(data["list_data"])):
        if data["list_data"][i] == selected_item:
          data["list_data"][i] = self.input_field.text()
          print(data["list_data"])
          save_json('data.json', data)
          self.close()

      
    def btn_cancel_clicked(self):
        self.close()



if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = AddList()
    main_window.show()
    sys.exit(app.exec())
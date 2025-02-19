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
button_set = (80,80)
button_size = (60,30)

class AddElement(Qw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("メイン要素の追加")  # ウィンドウのタイトル
        self.setGeometry(150, 150, 290, 120)  # ウィンドウの位置とサイズ
        
        # 何かシンプルなラベルを追加
        label = Qw.QLabel("追加するメイン要素", self)
        label.setGeometry(50, 20, 200, 30)

        self.input_field = Qw.QLineEdit(self)
        self.input_field.setPlaceholderText("要素名を入力してください")
        self.input_field.setVisible(True)
        self.input_field.setGeometry(50,50,190,28)
        self.input_field.setFocus()

        self.btn_decide = Qw.QPushButton('決定',self)
        self.btn_decide.setGeometry(button_set[0],button_set[1],button_size[0],button_size[1])
        self.btn_decide.clicked.connect(self.btn_decide_clicked)

        self.btn_cancel = Qw.QPushButton('中止',self)
        self.btn_cancel.setGeometry(button_set[0]+100,button_set[1],button_size[0],button_size[1])
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def btn_decide_clicked(self):
      if data["element_main"][0] == "---":
        data["element_main"][0] = self.input_field.text()
      else:
        data["element_main"].append(self.input_field.text())
        for i in range(4):
          data["element_sub"+f"{i+1}"].append("---")
      save_json('data.json', data)
      self.close()

      
    def btn_cancel_clicked(self):
        self.close()



if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = AddElement()
    main_window.show()
    sys.exit(app.exec())
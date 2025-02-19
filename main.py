import sys
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
import subprocess
import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # 'r'モードでファイルを開く
        data = json.load(f)  # JSONデータをPythonのデータ構造に変換
    return data
data = load_json('data.json')


class MainWindow(Qw.QMainWindow):
  
  def __init__(self):

    super().__init__() 
    self.setWindowTitle('MainWindow') 
    self.setGeometry(100, 50, 640, 320) 

    self.input_field = Qw.QLineEdit(self)
    self.input_field.setPlaceholderText("リスト名を入力してください")
    self.input_field.setVisible(False)

    self.btn_list = Qw.QPushButton('リスト名を変更',self)
    self.btn_list.setGeometry(10,10,100,40)
    self.btn_list.clicked.connect(self.btn_list_clicked)


    self.btn_add = Qw.QPushButton('要素を追加',self)
    self.btn_add.setGeometry(120,10,100,40)
    # self.btn_add.clicked.connect(self.btn_add_clicked)

    self.btn_reload = Qw.QPushButton('更新',self)
    self.btn_reload.setGeometry(230,10,100,40)
    self.btn_reload.clicked.connect(self.btn_reload_clicked)

    self.tb_log = Qw.QTextEdit('',self)
    self.tb_log.setStyleSheet("{background-color: white;}")
    self.tb_log.setGeometry(10,50,620,265)
    self.tb_log.setReadOnly(True)
    self.labels = []

    for i in range(len(data["list_data"])):
      self.list_name = Qw.QLabel(data["list_data"][i],self)
      self.list_name.setStyleSheet("font-size: 16px; color: gray;")
      self.list_name.setGeometry(20+i*100,50,100,20)
      self.list_name.show()
      self.labels.append(self.list_name)
      

  def btn_list_clicked(self):
    subprocess.Popen([sys.executable, 'sab.py'])

  def btn_reload_clicked(self):
    self.update_labels()

  def update_labels(self):
    data = load_json('data.json')
    print(data["list_data"])

    for i in range(len(data["list_data"])):
      blank = Qw.QLabel("                    ",self)
      new_label = Qw.QLabel(data["list_data"][i], self)
      new_label.setStyleSheet("font-size: 16px; color: gray;")
      blank.setStyleSheet("background-color: white;font-size: 16px; color: gray;")
      blank.setGeometry(20 + i * 100, 50, 100, 20)
      new_label.setGeometry(20 + i * 100, 50, 100, 20)
      blank.show()
      new_label.show()


      
      

if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())

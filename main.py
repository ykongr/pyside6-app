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

    self.btn_add_main = Qw.QPushButton('メイン要素を追加',self)
    self.btn_add_main.setGeometry(120,10,100,40)
    self.btn_add_main.clicked.connect(self.btn_add_main_clicked)

    self.btn_add = Qw.QPushButton('サブ要素を追加',self)
    self.btn_add.setGeometry(230,10,100,40)
    self.btn_add.clicked.connect(self.btn_add_sub_clicked)

    self.btn_reload = Qw.QPushButton('更新',self)
    self.btn_reload.setGeometry(340,10,100,40)
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

    for i in range(len(data["element_main"])):
      self.el_main = Qw.QLabel(data["element_main"][i],self)
      self.el_main.setStyleSheet("font-size: 14px; color: gray;")
      self.el_main.setGeometry(20,75+i*15,100,15)
      self.el_main.show()
      for j in range(4):
        self.el_sub = Qw.QLabel(data["element_sub"+f"{j+1}"][i],self)
        self.el_sub.setStyleSheet("font-size: 14px; color: gray;")
        self.el_sub.setGeometry(120+j*100,75+i*15,100,15)
        self.el_sub.show()
      

  def btn_list_clicked(self):
    subprocess.Popen([sys.executable, 'list.py'])

  def btn_add_main_clicked(self):
    subprocess.Popen([sys.executable, 'element_main.py'])

  def btn_add_sub_clicked(self):
    subprocess.Popen([sys.executable, 'element_sub.py'])

  def btn_reload_clicked(self):
    self.update_labels()
    self.updata_element()
  

  def update_labels(self):
    data = load_json('data.json')

    for i in range(len(data["list_data"])):
      blank = Qw.QLabel("                    ",self)
      blank.setStyleSheet("background-color: white;")
      blank.setGeometry(20 + i * 100, 50, 100, 20)
      new_label = Qw.QLabel(data["list_data"][i], self)
      new_label.setStyleSheet("font-size: 16px; color: gray;")
      new_label.setGeometry(20 + i * 100, 50, 100, 20)
      blank.show()
      new_label.show()

  def updata_element(self):
    data = load_json('data.json')
    
    for i in range(len(data["element_main"])):
      blank = Qw.QLabel("                    ",self)
      blank.setStyleSheet("background-color: white;")
      blank.setGeometry(20,75+i*15,100,15)
      new_el_main = Qw.QLabel(data["element_main"][i],self)
      new_el_main.setStyleSheet("font-size: 14px; color: gray;")
      new_el_main.setGeometry(20,75+i*15,100,15)
      blank.show()
      new_el_main.show()
      for j in range(4):
        blank = Qw.QLabel("                    ",self)
        blank.setStyleSheet("background-color: white;")
        blank.setGeometry(120+j*100,75+i*15,100,15)
        new_el_sub = Qw.QLabel(data["element_sub"+f"{j+1}"][i],self)
        new_el_sub.setStyleSheet("font-size: 14px; color: gray;")
        new_el_sub.setGeometry(120+j*100,75+i*15,100,15)
        blank.show()
        new_el_sub.show()


if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())

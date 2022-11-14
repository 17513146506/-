
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
12345
# 登陆对话框
class DialogUI(QWidget):
    def __init__(self,parent=None):
        super(DialogUI,self).__init__(parent)

        self.setWindowTitle("登陆")
        # self.resize(350,150)
        # 输入密码框
        flo=QFormLayout()
        e1=QLineEdit()
        BtnOk=QPushButton("  确   定   ")
        BtnCancel=QPushButton(" 取 消 ")
        BtnCancel.clicked.connect(self.close)   # 点击取消关闭窗口
        e1.setEchoMode(QLineEdit.Password)  # 设置密码不可见
        e1.textChanged.connect(self.textchanged)
        flo.addRow("请输入密码：",e1)
        flo.addRow(BtnOk,BtnCancel)
        self.setLayout(flo)

    # 核对密码是否正确
    def textchanged(self,text):
        if text == "12345":
            self.close()    # 关闭登陆界面
            WindowShow.show()
            print("输入正确,跳转至主界面")
        os.system

# 主窗口
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 860)
class WindowShow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WindowShow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('主窗口')
        self.setWindowIcon(QIcon('logo.jpg'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DialogUI()
    d.show()
    WindowShow=WindowShow() # 生成主窗口的实例
    # 使用qdarkstyle渲染模式
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec())



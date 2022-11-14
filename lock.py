import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel, QDesktopWidget, QHBoxLayout, QFormLayout, \
    QPushButton, QLineEdit


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化UI
        :return:
        """
        self.setObjectName("loginWindow")
        self.setStyleSheet('#loginWindow{background-color:white}')
        self.setFixedSize(650, 400)
        self.setWindowTitle("登录")
        self.setWindowIcon(QIcon('static/logo_title.png'))

        self.text = "xxxx消息盒子用户登录"

        # 添加顶部logo图片
        pixmap = QPixmap("background.jpg")
        scaredPixmap = pixmap.scaled(650, 140)
        label = QLabel(self)
        label.setPixmap(scaredPixmap)
        # 绘制顶部文字
        lbl_logo = QLabel(self)
        lbl_logo.setText(self.text)
        lbl_logo.setStyleSheet("QWidget{color:white;font-weight:600;background: transparent;font-size:30px;}")
        lbl_logo.setFont(QFont("Microsoft YaHei"))
        lbl_logo.move(150, 50)
        lbl_logo.setAlignment(Qt.AlignCenter)
        lbl_logo.raise_()

        # 登录表单内容部分
        login_widget = QWidget(self)
        login_widget.move(0, 140)
        login_widget.setGeometry(0, 140, 650, 260)

        hbox = QHBoxLayout()
        # 添加左侧logo
        logolb = QLabel(self)
        logopix = QPixmap("static/logo.png")
        logopix_scared = logopix.scaled(100, 100)
        logolb.setPixmap(logopix_scared)
        logolb.setAlignment(Qt.AlignCenter)
        hbox.addWidget(logolb, 1)
        # 添加右侧表单
        fmlayout = QFormLayout()
        lbl_workerid = QLabel("用户名")
        lbl_workerid.setFont(QFont("Microsoft YaHei"))
        led_workerid = QLineEdit()
        led_workerid.setFixedWidth(270)
        led_workerid.setFixedHeight(38)

        lbl_pwd = QLabel("密码")
        lbl_pwd.setFont(QFont("Microsoft YaHei"))
        led_pwd = QLineEdit()
        led_pwd.setEchoMode(QLineEdit.Password)
        led_pwd.setFixedWidth(270)
        led_pwd.setFixedHeight(38)

        btn_login = QPushButton("登录")
        btn_login.setFixedWidth(270)
        btn_login.setFixedHeight(40)
        btn_login.setFont(QFont("Microsoft YaHei"))
        btn_login.setObjectName("login_btn")
        btn_login.setStyleSheet("#login_btn{background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}")

        fmlayout.addRow(lbl_workerid, led_workerid)
        fmlayout.addRow(lbl_pwd, led_pwd)
        fmlayout.addWidget(btn_login)
        hbox.setAlignment(Qt.AlignCenter)
        # 调整间距
        fmlayout.setHorizontalSpacing(20)
        fmlayout.setVerticalSpacing(12)

        hbox.addLayout(fmlayout, 2)

        login_widget.setLayout(hbox)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginForm()
    sys.exit(app.exec_())
from PySide2.QtWidgets import *

class SQLClientWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)

        self.layout = QVBoxLayout()
        self.buttonsPanel = buttonsPanel()
        self.notificationPanel = QTextEdit()
        self.resulttable = QTableWidget(5, 3)
        self.resulttable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonsPanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resulttable)

        self.setLayout(self.layout)

class buttonsPanel(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layoutPrincipal = QHBoxLayout()

        self.B1 = QPushButton("Configure")
        self.B2 = QPushButton("Connect")
        self.B3 = QPushButton("Disconnect")

        self.layoutPrincipal.addWidget(self.B1)
        self.layoutPrincipal.addWidget(self.B2)
        self.layoutPrincipal.addWidget(self.B3)

        self.setLayout(self.layoutPrincipal)

if __name__ == "__main__":
   app = QApplication([])
   win = SQLClientWindow()
   win.show()
   app.exec_()

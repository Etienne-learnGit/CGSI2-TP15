from PySide2.QtWidgets import *

class labeledTextField(QWidget):

    def __init__(self, text):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.setMaximumHeight(50)

        self.obj1 = QLabel(text)
        self.obj2 = QTextEdit()

        self.layout.addWidget(self.obj1)
        self.layout.addWidget(self.obj2)

        self.setLayout(self.layout)

class configurationDialog(QDialog) :

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()

        self.t1 = labeledTextField("ip address")
        self.t2 = labeledTextField("User")
        self.t3 = labeledTextField("Passeword")

        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.t2)
        self.layout.addWidget(self.t3)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = configurationDialog()
   win.show()
   app.exec_()

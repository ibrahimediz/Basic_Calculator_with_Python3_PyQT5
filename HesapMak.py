import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton
class App(QMainWindow):
    #Hesap Makinası PyQT
    def __init__(self):
        super().__init__()
        self.title = 'Hesap Makinesi'
        self.pencere = uic.loadUi(r"D:\ibrahim_ediz\Ornekler\GUI\HesapMak.ui")
        self.liste = ["+","-","/","*"]
        self.pencere.txtEkran.textChanged.connect(self.controlFonk)
        self.islem = True
        self.initUI()
    def initUI(self):
        self.pencere.setWindowTitle(self.title)
        self.butonHazirla()

        # self.pencere.btdeneme2.clicked.connect(self.on_click1)
        self.pencere.show()
    def butonHazirla(self):
        for i in range(0,10):
            bt =  self.pencere.findChild(QPushButton,"b"+str(i))
            bt.clicked.connect(self.on_click1)
        for i in range(0,4):
            bt = self.pencere.findChild(QPushButton,"is"+str(i+1))
            bt.clicked.connect(self.on_click2)
        self.pencere.esit.clicked.connect(self.esittirTemizle)
        self.pencere.temizle.clicked.connect(self.esittirTemizle)
    def controlFonk(self):
        if self.islem == True:
            simdi = self.pencere.txtEkran.text() 
            if simdi[len(simdi)-2:len(simdi)-1] in self.liste and simdi[len(simdi)-1:] in self.liste:
                simdi = simdi[:len(simdi)-1]
            self.pencere.txtEkran.setText(simdi)
    def on_click1(self):
        sender = self.sender()
        if not self.islem :
            self.pencere.txtEkran.setText("")
            self.islem = True
        for i in range(0,10):
            simdi =  self.pencere.txtEkran.text()
            if sender == self.pencere.findChild(QPushButton,"b"+str(i)):
                self.pencere.txtEkran.setText(simdi+str(i))
    def on_click2(self):
        sender = self.sender()
        simdi =  self.pencere.txtEkran.text()
        for i in range(0,4):
            if sender == self.pencere.findChild(QPushButton,"is"+str(i+1)):
                self.pencere.txtEkran.setText(simdi+self.liste[i])
    def esittirTemizle(self):
        simdi = self.pencere.txtEkran.text()
        sender = self.sender()
        if sender == self.pencere.esit:
            simdi = str(eval(simdi))
            self.islem = False
        elif sender == self.pencere.temizle:
            simdi = ""
        else : 
            simdi = "Hata!"
        self.pencere.txtEkran.setText(simdi)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QFont
import sys
class restoran(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dorixona")
        self.setGeometry(50,50,1000,500)
        self.start()
    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 15))
        obj.move(x, y)
    def start(self):
        self.nomi = QLabel("",self) #Ekranni urtasidagi
        self.nomi.setFont(QFont("Roman, Times-New Roman",25))
        self.nomi.move(350,30)
#  Birinchi ustun
        self.taom1 = QLabel("Tabletka 1",self)
        self.font(self.taom1, 30, 90)
        self.osh = QCheckBox("Parasetamol",self)
        self.font(self.osh, 30, 130)
        self.dimlama = QCheckBox("Trimol",self)
        self.font(self.dimlama,30,170)
        self.qotirma = QCheckBox("Seteramon", self)
        self.font(self.qotirma, 30, 210)
        self.norin = QCheckBox("Atsetse", self)
        self.font(self.norin, 30, 250)
        self.kabob = QCheckBox("Doktor-Mom", self)
        self.font(self.kabob, 30, 290)
    #  Ikkinchi Ustun
        self.taom2 = QLabel("Sirop 2",self)
        self.font(self.taom2,240,90)
        self.lagmon = QCheckBox("Qiszil miyya",self)
        self.font(self.lagmon,240,130)
        self.chuchvara = QCheckBox("Taylalhot",self)
        self.font(self.chuchvara,240,170)
        self.shorva = QCheckBox("Griphot",self)
        self.font(self.shorva,240,210)
        self.moshxorda = QCheckBox("nimadurhot",self)
        self.font(self.moshxorda,240,250)
        self.ajabsanda = QCheckBox("lula-la",self)
        self.font(self.ajabsanda,240,290)
    # Uchinchi qator
        self.ichimlik = QLabel("Qushimcha 3",self)
        self.font(self.ichimlik,450,90)
        self.kofe = QCheckBox("Shpris", self)
        self.font(self.kofe, 450, 130)
        self.cocacola = QCheckBox("Spert", self)
        self.font(self.cocacola, 450, 170)
        self.chortoq = QCheckBox("Maska", self)
        self.font(self.chortoq, 450, 210)
        self.fanta = QCheckBox("Davlena ulchedgan", self)
        self.font(self.fanta, 450, 250)
        self.sharbat = QCheckBox("Osmaa", self)
        self.font(self.sharbat, 450, 290)
        self.desert = QLabel("", self)
        self.font(self.desert, 680, 90)
#Pasdadgi tugmacha
        self.hisob = QPushButton("Hisob",self)
        self.font(self.hisob,30,350)
        self.hisob.clicked.connect(self.run)
        self.malumot = QPushButton("Dorixona haqida ma'lumot", self)
        self.font(self.malumot, 60, 380)
        self.taomlar1 = QLabel(self)
        self.font(self.taomlar1, 30, 100)
        self.taomlar2 = QLabel(self)
        self.font(self.taomlar2,250,100)
        self.ichim = QLabel(self)
        self.font(self.ichim,500,100)
        self.des = QLabel(self)
        self.font(self.des,720,100)
        self.jami_hisob = QLabel(self)
        self.font(self.jami_hisob,300,40)
    def run(self):
        hisob = 0
        taom_1 = ""
        self.osh.hide()
        self.dimlama.hide()
        self.qotirma.hide()
        self.norin.hide()
        self.kabob.hide()
        self.taom1.hide()
        if self.osh.isChecked():
            taom_1 += "Parasetamol -> 5000\n\n"
            hisob += 5000
        if self.dimlama.isChecked():
            taom_1 += "Trimol -> 14999\n\n"
            hisob += 14999
        if self.qotirma.isChecked():
            taom_1 += "Seteramon -> 19234\n\n"
            hisob += 19234
        if self.norin.isChecked():
            taom_1 += "Atsetse -> 10000\n\n"
            hisob += 10000
        if self.kabob.isChecked():
            taom_1 += "Doktor-mom -> 15000"
            hisob += 15000
        self.taomlar1.setText(f"1-Tabletkalar -> {hisob}\n\n{taom_1}")
        self.taomlar1.adjustSize()

        self.lagmon.hide()
        self.chuchvara.hide()
        self.shorva.hide()
        self.moshxorda.hide()
        self.ajabsanda.hide()
        self.taom2.hide()
        hisob2 = 0
        taom_2 = ""
        if self.lagmon.isChecked():
            taom_2 += "Qizil miya -> 18000\n\n"
            hisob2 += 18000
        if self.chuchvara.isChecked():
            taom_2 += "Taylalhot -> 15000\n\n"
            hisob2 += 15000
        if self.shorva.isChecked():
            taom_2 += "Griphot -> 15000\n\n"
            hisob2 += 15000
        if self.moshxorda.isChecked():
            taom_2 += "nimadurhot -> 17000\n\n"
            hisob2 += 17000
        if self.ajabsanda.isChecked():
            taom_2 += "Lula-la -> 19000"
            hisob2 += 19000
        self.taomlar2.setText(f"2-Sirop -> {hisob2}\n\n{taom_2}")
        self.taomlar2.adjustSize()

        self.kofe.hide()
        self.cocacola.hide()
        self.chortoq.hide()
        self.fanta.hide()
        self.sharbat.hide()
        self.ichimlik.hide()
        hisob3 = 0
        ichimli = ""
        if self.kofe.isChecked():
            ichimli += "Shpris -> 5000\n\n"
            hisob3 += 5000
        if self.cocacola.isChecked():
            ichimli += "Spert -> 10000\n\n"
            hisob3 += 10000
        if self.chortoq.isChecked():
            ichimli += "Maska -> 9000\n\n"
            hisob3 += 9000
        if self.fanta.isChecked():
            ichimli += "Davlena Ulchagich -> 10000\n\n"
            hisob3 += 10000
        if self.sharbat.isChecked():
            ichimli += "Osmaa -> 8000"
            hisob3 += 8000
        self.ichim.setText(f"Qushimcha -> {hisob3}\n\n{ichimli}")
        self.ichim.adjustSize()


        self.des.adjustSize()
        self.nomi.hide()
        self.hisob.hide()
        self.malumot.hide()


        self.jami_hisob.setText(f"Jami hisob --> {hisob+hisob2+hisob3}")
        self.jami_hisob.adjustSize()
app = QApplication(sys.argv)
ob = restoran()
ob.show()
sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import continuoreaccionquimica
import continuoreactornuclear
import discretapeluqueria
import discretarestaurante
import discretarestaurantes2
import discretasistemaderedes

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Cargar el archivo .ui
        uic.loadUi("vista.ui", self)

        # Conectar el botón a la función
        self.pushButton.clicked.connect(self.objetivo1_reaccionquimica)
        self.pushButton_2.clicked.connect(self.objetivivo2_reactornuclear)
        self.pushButton_3.clicked.connect(self.objetivo3_peluqueria)
        self.pushButton_4.clicked.connect(self.objetivo4_discretarestaurantes)
        self.pushButton_5.clicked.connect(self.objetivo5_discretarestaurantes2)
        self.pushButton_6.clicked.connect(self.objetivo6_sistemas_de_redes)

    def objetivo1_reaccionquimica(self):
        # Obtener el texto de los QTextEdit
        a_text = self.textEdit.toPlainText()
        b_text = self.textEdit_2.toPlainText()

        # Convertir el texto a los tipos apropiados, por ejemplo, float
        try:
            a = float(a_text)
            b = float(b_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return

        # Llamar a la clase con los valores convertidos
        result = continuoreaccionquimica.ReaccionPrimeraOrden(a, b)
        result.resolver()
        result.graficar()
    def objetivivo2_reactornuclear(self):
        # Obtener el texto de los QTextEdit
        

        a_text = self.textEdit_4.toPlainText()
        b_text = self.textEdit_5.toPlainText()
        c_text = self.textEdit_6.toPlainText()
        d_text = self.textEdit_7.toPlainText()
        e_text = self.textEdit_8.toPlainText()

        try:
            a = float(a_text)
            b = float(b_text)
            c = float(c_text)
            d = float(d_text)
            e = float(e_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return


        
        result = continuoreactornuclear.ReactorNuclear(a,b,c,d,e)
        result.resolver()
        result.graficar()

    def objetivo3_peluqueria(self):

        a_text = self.textEdit_9.toPlainText()
        b_text = self.textEdit_10.toPlainText()
        c_text = self.textEdit_11.toPlainText()
        d_text = self.textEdit_12.toPlainText()
        e_text = self.textEdit_13.toPlainText()
        f_text = self.textEdit_14.toPlainText()

        try:
            a = int(a_text)
            b = int(b_text)
            c = int(c_text)
            d = int(d_text)
            e = int(e_text)
            f = int(f_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return

        result= discretapeluqueria.Peluqueria(a,b,c,d,e,f)
        result.ejecutar()

    def objetivo4_discretarestaurantes(self):
        a_text = self.textEdit_16.toPlainText()
        b_text = self.textEdit_17.toPlainText()
        c_text = self.textEdit_18.toPlainText()
        d_text = self.textEdit_34.toPlainText() # numero de mostradores
        try:
            a = int(a_text)
            b = int(b_text)
            c = int(c_text)
            d = int(d_text)
            libreria_rangos= (a,b)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return
        result = discretarestaurante.SimulacionRestaurante(num_counters=d, customer_range_norm=libreria_rangos,sim_time=c)
        result.run()

    def objetivo5_discretarestaurantes2(self):


        a_text = self.textEdit_19.toPlainText()
        b_text = self.textEdit_20.toPlainText()
        c_text = self.textEdit_21.toPlainText()
        d_text = self.textEdit_22.toPlainText()
        e_text = self.textEdit_23.toPlainText()
        f_text = self.textEdit_24.toPlainText()
        
        try:
            a = int(a_text)
            b = int(b_text)
            c = int(c_text)
            d = int(d_text)
            e = int(e_text)
            f = int(f_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return
        result= discretarestaurantes2.Restaurante(b,c,d,e,f,a)
        result.run()
    def objetivo6_sistemas_de_redes(self):

        a_text = self.textEdit_26.toPlainText()
        b_text = self.textEdit_27.toPlainText()
        c_text = self.textEdit_28.toPlainText()
        d_text = self.textEdit_29.toPlainText()
        e_text = self.textEdit_30.toPlainText()
        f_text = self.textEdit_31.toPlainText()
        g_text = self.textEdit_32.toPlainText()
        
        try:
            a = int(a_text)
            b = int(b_text)
            c = int(c_text)
            d = int(d_text)
            e = int(e_text)
            f = int(f_text)
            g = int(g_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese números válidos.")
            return
        result= discretasistemaderedes.SimulacionRedComputadoras()
        result.iniciar(a,b,c,d,e,f,g)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


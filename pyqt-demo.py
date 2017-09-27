import sys#, os, glob
from PyQt5 import QtWidgets, uic#QtCore, QtGui, uic
import serial, time

qtCreatorFile = "pyQtEdit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.pushButton_LED_ON.clicked.connect(self.LED_ON)
		self.pushButton_LED_OFF.clicked.connect(self.LED_OFF)
		
		self.textEdit_LogMessage.append("Demo LED menggunakan PyQt - Aruino Uno")
		#self.pushButton_Send.setEnabled(False)
		
	def OpenSerial(self):
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM3", "9600", timeout=0.1)
			if self.ser.isOpen():
				self.pushButton_OpenSerial.setText('Close Serial')
				self.textEdit_LogMessage.append("Opening serial port... OK")
				#self.pushButton_Send.setEnabled(True)
			else:
				self.textEdit_LogMessage.append("can not open serial port")
		else:
			if self.ser.isOpen():
				self.ser.close()
			self.pushButton_OpenSerial.setText('Open Serial')
			self.textEdit_LogMessage.append("Closing serial port... OK")
			#self.pushButton_Send.setEnabled(False)
			
	def LED_ON(self):
		#tON  = self.spinBox_tON.value()
		#tOFF = self.spinBox_tOFF.value()
		#self.textEdit_LogMessage.append("Sending tON = %d ms, tOFF = %d ms" %(tON*100,tOFF*100))
		self.TXdata = bytearray(2)
		#self.TXdata = bytearray(2)
		#self.TXdata[0]=tON
		#self.TXdata[1]=tOFF
		self.TXdata[0]=1
		self.TXdata[1]=1
		self.ser.write(self.TXdata)

		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		if (self.bytesToRead > 0):
			rxdata = self.ser.read(self.bytesToRead)
			self.textEdit_LogMessage.append(rxdata)


	def LED_OFF(self):
		#tON  = self.spinBox_tON.value()
		#tOFF = self.spinBox_tOFF.value()
		#self.textEdit_LogMessage.append("Sending tON = %d ms, tOFF = %d ms" %(tON*100,tOFF*100))
		self.TXdata = bytearray(1)
		#self.TXdata = bytearray(2)
		#self.TXdata[0]=tON
		#self.TXdata[1]=tOFF
		self.TXdata[0]=1
		#self.TXdata[1]=1
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		if (self.bytesToRead > 0):
			rxdata = self.ser.read(self.bytesToRead)
			self.textEdit_LogMessage.append(rxdata)
			
	def AppExit(self):
		self.textEdit_LogMessage.setText("Exit application")
		sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

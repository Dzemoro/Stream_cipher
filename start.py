from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys, os

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno, self).__init__(*args,*kwargs)
        self.setWindowTitle("XOR Encryptor")
        
        titleText = QLabel()
        titleText.setText("XOR")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Comic Sans',50))
        titleText.setStyleSheet("QLabel {color : #cae8d5}")

        titleText2 = QLabel()
        titleText2.setText("ENCRYPTOR")
        titleText2.setAlignment(Qt.AlignCenter)
        titleText2.setFont(QFont('Comic Sans',50))
        titleText2.setStyleSheet("QLabel {color : #cae8d5}")

        self.subtitleText = QLabel()
        self.subtitleText.setText(" ")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Comic Sans',20))
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Comic Sans',12))
        self.infoButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.infoButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.infoButton.clicked.connect(self.infoClicked)

        self.checkTextButton = QPushButton()
        self.checkTextButton.setText("Check text")
        self.checkTextButton.setFont(QFont('Comic Sans',12))
        self.checkTextButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.checkTextButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.checkTextButton.clicked.connect(self.checkTextClicked)

        self.checkResultButton = QPushButton()
        self.checkResultButton.setText("Check result")
        self.checkResultButton.setFont(QFont('Comic Sans',12))
        self.checkResultButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.checkResultButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.checkResultButton.clicked.connect(self.checkResultClicked)

        encryptButton = QPushButton()
        encryptButton.setText("Encrypt")
        encryptButton.setFont(QFont('Comic Sans',12))
        encryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        encryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        encryptButton.clicked.connect(self.encryptClicked)

        decryptButton = QPushButton()
        decryptButton.setText("Decrypt")
        decryptButton.setFont(QFont('Comic Sans',12))
        decryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        decryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        decryptButton.clicked.connect(self.decryptClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(decryptButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)

        checkLayout = QHBoxLayout()
        checkLayout.addWidget(self.checkTextButton)
        checkLayout.addWidget(self.checkResultButton)
        checkLayoutW = QWidget()
        checkLayoutW.setLayout(checkLayout)

        infoButtonsLayout = QHBoxLayout()
        #infoButtonsLayout.addWidget(self.checkTextButton)
        infoButtonsLayout.addWidget(self.infoButton)
        infobuttonsLayoutW = QWidget()
        infobuttonsLayoutW.setLayout(infoButtonsLayout)

        #Main Layout
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(titleText2)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(checkLayoutW)
        mainMenu.addWidget(infobuttonsLayoutW)

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)

    def encryptClicked(self):
        self.subtitleText.setText(" ")
        self.encryptDecrypt("text.txt")
        self.subtitleText.setText("ENCRYPT DONE")

    def decryptClicked(self):
        self.subtitleText.setText(" ")
        self.encryptDecrypt("result.txt")
        self.subtitleText.setText("DECRYPT DONE")

    def messageFileClicked(self):
        self.keyFromFileButton.hide()
        self.messageFromFileButton.show()

        if self.messageFromFileButton.exec():
            files = self.messageFromFileButton.selectedFiles()
            r = open(files[0],'r',encoding="utf-8")
            with r:
                data = r.read()
                self.messageField.setText(data)
    
    def keyFileClicked(self):
        self.messageFromFileButton.hide()
        self.keyFromFileButton.show()
        if self.keyFromFileButton.exec():
            files = self.keyFromFileButton.selectedFiles()
            r = open(files[0],'r',encoding="utf-8")
            with r:
                data = r.read()
                self.keyField.setText(data)
    
    def saveClicked(self):
        f = open("result.txt", "w",encoding="utf-8")
        f.write("Encrypted text: "+self.encryptedText.text())
        f.write("\nDecrypted text: "+self.decryptedText.text())
        f.write("\nKey: "+self.genKey())
        f.close()

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("info.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()
    
    def checkTextClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Text")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("text.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()

    def checkResultClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Result")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("result.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()
    
    def encryptDecrypt(self,path):
        text = open(path, 'r', encoding="utf8")
        key = open("key.txt", 'r', encoding="utf8")
        output = ""
        val = 0
        while True:
            tmp = text.read(1)
            if not tmp:
                break
            for i in range(8):
                val = (2**(7-i)) * int(key.read(1))
            output = output + chr(ord(tmp) ^ val)
        f = open("result.txt", 'w')
        f.write(output)
                     
#MAIN
app = QApplication(sys.argv)
window = Okno()
window.setFixedSize(500,400)
window.setStyleSheet("background-color: #204051")
window.show()

app.exec_()
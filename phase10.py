#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit
from PyQt5.QtGui import QFont


class EndRound(QWidget):

    def __init__(self):
        super().__init__()
        self.xOrigName = 15
        self.yOrigName = 50
        self.titleFont = QFont("Sans Serif",20,QFont.Bold)
        self.initPopUp()

    def initPopUp(self):
        #Player Labels

        plbl = QLabel('Players',self)
        plbl.move(self.xOrigName, self.yOrigName-35)
        plbl.setFont(self.titleFont)

        p1 = QLabel('Player 1', self)
        p1.move(self.xOrigName, self.yOrigName)

        p2 = QLabel('Player 2', self)
        p2.move(self.xOrigName, self.yOrigName+30)

        p3 = QLabel('Player 3', self)
        p3.move(self.xOrigName, self.yOrigName+60)

        p4 = QLabel('Player 4', self)
        p4.move(self.xOrigName, self.yOrigName+90)

        p5 = QLabel('Player 5', self)
        p5.move(self.xOrigName, self.yOrigName+120)

        p6 = QLabel('Player 6', self)
        p6.move(self.xOrigName, self.yOrigName+150)

        #Score Labels

        slbl = QLabel('Score',self)
        slbl.move(self.xOrigName+180, self.yOrigName-35)
        slbl.setFont(self.titleFont)

        s1 = QLineEdit(self)
        s1.move(self.xOrigName+150, self.yOrigName)

        s2 = QLineEdit(self)
        s2.move(self.xOrigName+150, self.yOrigName+30)

        s3 = QLineEdit(self)
        s3.move(self.xOrigName+150, self.yOrigName+60)

        s4 = QLineEdit(self)
        s4.move(self.xOrigName+150, self.yOrigName+90)

        s5 = QLineEdit(self)
        s5.move(self.xOrigName+150, self.yOrigName+120)

        s6 = QLineEdit(self)
        s6.move(self.xOrigName+150, self.yOrigName+150)

        phlbl = QLabel('Completed \nPhase?',self)
        phlbl.move(self.xOrigName+360, self.yOrigName-45)
        phlbl.setFont(self.titleFont)

        self.setGeometry(800, 300, 500, 300)
        self.setWindowTitle('End of Round')
        self.show()



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.xOrigName = 15
        self.yOrigName = 50
        self.titleFont = QFont("Sans Serif",20,QFont.Bold)

        self.initUI()


    def initUI(self):


        #Player Labels

        plbl = QLabel('Players',self)
        plbl.move(self.xOrigName, self.yOrigName-35)
        plbl.setFont(self.titleFont)

        p1 = QLabel('Player 1', self)
        p1.move(self.xOrigName, self.yOrigName)

        p2 = QLabel('Player 2', self)
        p2.move(self.xOrigName, self.yOrigName+30)

        p3 = QLabel('Player 3', self)
        p3.move(self.xOrigName, self.yOrigName+60)

        p4 = QLabel('Player 4', self)
        p4.move(self.xOrigName, self.yOrigName+90)

        p5 = QLabel('Player 5', self)
        p5.move(self.xOrigName, self.yOrigName+120)

        p6 = QLabel('Player 6', self)
        p6.move(self.xOrigName, self.yOrigName+150)

        #Score Labels

        slbl = QLabel('Score',self)
        slbl.move(self.xOrigName+150, self.yOrigName-35)
        slbl.setFont(self.titleFont)

        s1 = QLabel('  0  ', self)
        s1.move(self.xOrigName+168, self.yOrigName)

        s2 = QLabel('  0  ', self)
        s2.move(self.xOrigName+168, self.yOrigName+30)

        s3 = QLabel('  0  ', self)
        s3.move(self.xOrigName+168, self.yOrigName+60)

        s4 = QLabel('  0  ', self)
        s4.move(self.xOrigName+168, self.yOrigName+90)

        s5 = QLabel('  0  ', self)
        s5.move(self.xOrigName+168, self.yOrigName+120)

        s6 = QLabel('  0  ', self)
        s6.move(self.xOrigName+168, self.yOrigName+150)

        #Phase Labels

        phlbl = QLabel('Phase',self)
        phlbl.move(self.xOrigName+250, self.yOrigName-35)
        phlbl.setFont(self.titleFont)

        ph1 = QLabel(' 1  ', self)
        ph1.move(self.xOrigName+275, self.yOrigName)

        ph2 = QLabel(' 1  ', self)
        ph2.move(self.xOrigName+275, self.yOrigName+30)

        ph3 = QLabel(' 1  ', self)
        ph3.move(self.xOrigName+275, self.yOrigName+60)

        ph4 = QLabel(' 1 ', self)
        ph4.move(self.xOrigName+275, self.yOrigName+90)

        ph5 = QLabel(' 1 ', self)
        ph5.move(self.xOrigName+275, self.yOrigName+120)

        ph6 = QLabel(' 1 ', self)
        ph6.move(self.xOrigName+275, self.yOrigName+150)

        #Buttons
        endRoundBtn = QPushButton("End Round", self)
        endRoundBtn.move(self.xOrigName+25, self.yOrigName+200)

        endRoundBtn.clicked.connect(self.endRoundClicked)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Phase 10 Score Keeper')
        self.show()

    def endRoundClicked(self):
        self.endround = EndRound()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    game = MainWindow()
    sys.exit(app.exec_())

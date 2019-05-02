#! /usr/bin/env python3
__author__ = "rafael daveiga"

import sys
from sys import path
import tictactoeResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtCore import pyqtSlot, QCoreApplication, QSettings, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load


logFilenameDefault = 'tictactoe.log'
pickleFileNameDefault = '.tictactoeSave.pl'


class TicTacToe(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = getLogger('Rafael.TicTacToe')
        self.appSetting = QSettings()
        self.quitCount = 0

        uic.loadUi("TicTacToe.ui", self)
        self.pickleFilename = pickleFileNameDefault
        self.playerOne = 'X'
        self.computer = 'O'
        self.playerOneWins = 0
        self.computerWins = 0
        self.draws = 0
        self.box0.clicked.connect(self.clickedHandler(0))
        self.box1.clicked.connect(self.clickedHandler(0))
        self.box2.clicked.connect(self.clickedHandler(0))
        self.box3.clicked.connect(self.clickedHandler(0))
        self.box4.clicked.connect(self.clickedHandler(0))
        self.box5.clicked.connect(self.clickedHandler(0))
        self.box6.clicked.connect(self.clickedHandler(0))
        self.box7.clicked.connect(self.clickedHandler(0))
        self.box8.clicked.connect(self.clickedHandler(0))
#        self.restoreSetting()

        if self.exist(self.pickleFilename):
            pass

        else:
            self.restartGame()

    def __str__(self):
        pass

    def updateUi(self):
        if self.createLogFile:
            self.logger.info()
        self.set


    def restartGame(self):
        if self.createLogFile:
            self.logger.debug("Game Restarting")
        self.win = 0
        self.loss = 0

    def saveGame(self):
        if self.createLogFile:
            self.logger.debug("Saving Game")
        saveItem = ()
        if self.appSetting.contain('pickleFilename'):
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename', type=str
                                                                                              )), 'wb') as pickleFile:
                dump(saveItem, pickleFile)
                return load(pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def restoreGame(self):
        if self.appSettings.conatains('pickleFilename'):
            self.appSettings.value('pickleFilename', type=str)
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename', type=str
                                                                                              )), 'rb') as pickleFile:
                return load(pickleFile)
        else:
            self.logger.critical('No pickle Filename')

    def restoreSettings(self):
        if self.appSettings.contains('createLogFile'):
            self.createLogFile = self.appSettings.value('createLogFile')
        else:
            self.createLogFile = logFilenameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)

        if self.appSettings.contains("pickleFilename"):
            self.pickleFilename = self.appSettings.value('pickleFilename', type=str)
        else:
            self.pickleFilename = pickleFileNameDefault
            self.appSettings.setValue('pickleFilename', self.pickleFilename)

    def tictacToe(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        end = False
        win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def cancelClickedHandler(self):

        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    testApp = TicTacToe()
    testApp.show()
    sys.exit(app.exec_())


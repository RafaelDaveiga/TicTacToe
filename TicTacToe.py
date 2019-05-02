#! /usr/bin/env python3
__author__ = "rafael daveiga"


import sys
import tictactoeResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load


logFilenameDefault = 'tictactoe.log'
pickleFileNameDefault = '.tictactoeSave.pl'


class TicTacToe(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = getLogger('Rafael.TicTacToe')
        self.appSetting = QSetting()
        self.quitCount = 0

        uic.loadUi('tictactoe.ui', self)

        self.pickleFilename = pickleFileNameDefault

        self.restoreSetting()

        if path.exist(self.pickleFilename):
            pass
        else:
            self.restartGame

    def __str__(self):
        pass

    def updateUi(self):
        if self.createLogFile:
            self.logger.info()

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
        if self.createLogFile:
            self.logger.debug("Starting restoreSettings")
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

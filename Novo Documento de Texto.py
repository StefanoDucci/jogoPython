# ecoding: UTF-8


import sys
from PyQt4 import QtGui, QtCore

class Main(QtGui.QWidget):
    """
    Janela principal
    """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #Muda a geometria da janela
        self.setGeometry(200, 200, 200, 100)

        #Muda o título
        self.setWindowTitle('Teste')

        #Cria um botão
        quit = QtGui.QPushButton('Fechar', self)
        quit.setGeometry(10, 10, 60, 35)

        #Conecta o sinal gerado pelo botão com a função que encerra o programa
        self.connect(quit, QtCore.SIGNAL('cliked()'),
                     QtGui.qApp, QtCore.SLOT('quit()'))

        #Cria um objeto "aplicação QT", que trata o eventos
        app = QtGui.QApplication(sys.argv)

        #Cria a janela principal
        qb = Main()
        qb.show()

        #Inicia a aplicação
        sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroProdutos.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from CustomDialogEmptyFields import CustomDialogEmptyFields
from CustomDialogCadastrado import CustomDialogCadastrado
BancoDedados = ""

class Ui_CadastroProdutos(object):
    def pegandoBancoDeDados(self, banco):
        criarDb = sqlite3.connect(banco)
        criando = criarDb.cursor()
        criando.execute("CREATE TABLE IF NOT EXISTS produtos (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nome VARCHAR, quantidade VARCHAR, categoria VARCHAR, preco VARCHAR);")
        criarDb.commit()
        criarDb.close()

        global BancoDedados
        BancoDedados = banco

    def inserindoDados(self):
        conectar = sqlite3.Connection(BancoDedados)
        cursor = conectar.cursor()

        produto = self.txt_NomeProduto.toPlainText()
        quantidade = self.txt_Quantidade.toPlainText()
        categoria = self.listItem.currentItem().text()
        preco = self.txt_categoria_2.toPlainText()
        if(produto == "" or quantidade == "" or categoria == "" or preco == ""):
            print("Um ou mais valores estão em branco")
            dlg = CustomDialogEmptyFields()
            dlg.exec()
        else:
            cursor.execute("INSERT INTO produtos (nome, quantidade, categoria, preco) VALUES ('{}', '{}', '{}', '{}')".format(produto, quantidade, categoria, preco))
            conectar.commit()
            conectar.close()
            dlg = CustomDialogCadastrado()
            dlg.exec()
    def setupUi(self, MainWindow):
        conn = sqlite3.connect(BancoDedados)
        print(conn)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 448)
        MainWindow.setStyleSheet("background-color: pink;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setGeometry(QtCore.QRect(110, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setObjectName("lb_titulo")


        self.txt_NomeProduto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_NomeProduto.setGeometry(QtCore.QRect(120, 80, 221, 41))
        self.txt_NomeProduto.setStyleSheet("background-color: white;\n"
"font-size:14pt;")
        self.txt_NomeProduto.setObjectName("txt_NomeProduto")


        self.lb_produto = QtWidgets.QLabel(self.centralwidget)
        self.lb_produto.setGeometry(QtCore.QRect(30, 85, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_produto.setFont(font)
        self.lb_produto.setObjectName("lb_produto")
        self.lb_quantidade = QtWidgets.QLabel(self.centralwidget)
        self.lb_quantidade.setGeometry(QtCore.QRect(10, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_quantidade.setFont(font)
        self.lb_quantidade.setObjectName("lb_quantidade")
        self.txt_Quantidade = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_Quantidade.setGeometry(QtCore.QRect(120, 140, 51, 41))
        self.txt_Quantidade.setStyleSheet("background-color: white;\n"
"font-size:14pt;")
        self.txt_Quantidade.setObjectName("txt_Quantidade")
        self.btn_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastrar.setGeometry(QtCore.QRect(70, 330, 211, 61))
        self.btn_cadastrar.setStyleSheet("background-color: white;\n"
"font-family: verdana;\n"
"border: 1px solid;\n"
"font-size: 11pt;")
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.btn_cadastrar.clicked.connect(self.inserindoDados)
        self.lb_categoria = QtWidgets.QLabel(self.centralwidget)
        self.lb_categoria.setGeometry(QtCore.QRect(20, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_categoria.setFont(font)
        self.lb_categoria.setObjectName("lb_categoria")
        self.lb_categoria_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_categoria_2.setGeometry(QtCore.QRect(50, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_categoria_2.setFont(font)
        self.lb_categoria_2.setObjectName("lb_categoria_2")
        self.txt_categoria_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_categoria_2.setGeometry(QtCore.QRect(120, 260, 81, 41))
        self.txt_categoria_2.setStyleSheet("background-color: white;\n"
"font-size:14pt;")
        self.txt_categoria_2.setPlainText("")
        self.txt_categoria_2.setObjectName("txt_categoria_2")
        self.listItem = QtWidgets.QListWidget(self.centralwidget)
        self.listItem.setGeometry(QtCore.QRect(120, 200, 161, 31))
        self.listItem.setStyleSheet("background-color: white;\n"
"font-size:14pt;")
        self.listItem.setObjectName("listItem")
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        self.listItem.setCurrentItem(item)

        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listItem.addItem(item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_titulo.setText(_translate("MainWindow", "Cadastrar Produto"))
        self.lb_produto.setText(_translate("MainWindow", "Produto:"))
        self.lb_quantidade.setText(_translate("MainWindow", "Quantidade:"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.lb_categoria.setText(_translate("MainWindow", "Categoria:"))
        self.lb_categoria_2.setText(_translate("MainWindow", "Preço:"))
        __sortingEnabled = self.listItem.isSortingEnabled()
        self.listItem.setSortingEnabled(False)
        item = self.listItem.item(0)
        item.setText(_translate("MainWindow", "Higiene"))
        item = self.listItem.item(1)
        item.setText(_translate("MainWindow", "Alimento"))
        item = self.listItem.item(2)
        item.setText(_translate("MainWindow", "frios e laticínios"))
        item = self.listItem.item(3)
        item.setText(_translate("MainWindow", "Brinquedo"))
        item = self.listItem.item(4)
        item.setText(_translate("MainWindow", "Enlatados"))
        item = self.listItem.item(5)
        item.setText(_translate("MainWindow", "Bebidas"))
        item = self.listItem.item(6)
        item.setText(_translate("MainWindow", "Açougue"))
        item = self.listItem.item(7)
        item.setText(_translate("MainWindow", "Outros"))
        self.listItem.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CadastroProdutos()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

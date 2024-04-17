# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dadosCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
import pandas as pd
import variaveisControle


class Ui_formDadosCliente(object):
    def setupUi(self, formDadosCliente):
        formDadosCliente.setObjectName("formDadosCliente")
        formDadosCliente.resize(400, 300)
        self.lb_nome = QtWidgets.QLabel(formDadosCliente)
        self.lb_nome.setGeometry(QtCore.QRect(40, 40, 51, 17))
        self.lb_nome.setObjectName("lb_nome")
        self.lb_telefone = QtWidgets.QLabel(formDadosCliente)
        self.lb_telefone.setGeometry(QtCore.QRect(30, 80, 67, 17))
        self.lb_telefone.setObjectName("lb_telefone")
        self.lb_cidade = QtWidgets.QLabel(formDadosCliente)
        self.lb_cidade.setGeometry(QtCore.QRect(40, 120, 51, 17))
        self.lb_cidade.setObjectName("lb_cidade")
        self.txt_nome = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_nome.setGeometry(QtCore.QRect(110, 40, 251, 25))
        self.txt_nome.setObjectName("txt_nome")
        self.txt_telefone = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_telefone.setGeometry(QtCore.QRect(110, 80, 251, 25))
        self.txt_telefone.setObjectName("txt_telefone")
        self.txt_cidade = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_cidade.setGeometry(QtCore.QRect(110, 120, 251, 25))
        self.txt_cidade.setObjectName("txt_cidade")
        self.bt_cancelar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cancelar.setGeometry(QtCore.QRect(110, 180, 89, 71))
        self.bt_cancelar.setStyleSheet("image: url(:/icon_cancelar/imagens/icons/cancelar.png)")
        self.bt_cancelar.setText("")
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.bt_cadastrar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cadastrar.setGeometry(QtCore.QRect(230, 180, 89, 71))
        self.bt_cadastrar.setStyleSheet("image: url(:/icon_cadastrar/imagens/icons/cadastrar.png)")
        self.bt_cadastrar.setText("")
        self.bt_cadastrar.setObjectName("bt_cadastrar")

        self.retranslateUi(formDadosCliente)
        QtCore.QMetaObject.connectSlotsByName(formDadosCliente)

    def retranslateUi(self, formDadosCliente):
        _translate = QtCore.QCoreApplication.translate
        formDadosCliente.setWindowTitle(_translate("formDadosCliente", "Form"))
        self.lb_nome.setText(_translate("formDadosCliente", "Nome:"))
        self.lb_telefone.setText(_translate("formDadosCliente", "Telefone:"))
        self.lb_cidade.setText(_translate("formDadosCliente", "Cidade:"))
        self.bt_cancelar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_cadastrar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p><br/></p></body></html>"))

        #botoes
        self.bt_cancelar.clicked.connect(lambda: self.sairTela(formDadosCliente))
        self.bt_cadastrar.clicked.connect(self.cadastrarCliente)

    #Funcoes sistema

    def sairTela(self, formDadosCliente):
        formDadosCliente.close()


    def cadastrarCliente(self):
        nomeCliente = self.txt_nome.text()
        telefoneCliente = self.txt_telefone.text()
        cidadeCliente = self.txt_cidade.text()
        
        mydb = mysql.connector.connect(
            host = variaveisControle.host,
            user = variaveisControle.user,
            password = variaveisControle.password,
            database = variaveisControle.database
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO cliente(nome, telefone, cidade) VALUES (%s, %s, %s)"
        val = (nomeCliente, telefoneCliente, cidadeCliente)
        mycursor.execute(sql, val)

        mydb.commit()
        mycursor.close()

        #Limpando campos
        self.txt_nome.setText("")
        self.txt_telefone.setText("")
        self.txt_cidade.setText("")

import icon_cadastrar
import icon_cancelar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formDadosCliente = QtWidgets.QWidget()
    ui = Ui_formDadosCliente()
    ui.setupUi(formDadosCliente)
    formDadosCliente.show()
    sys.exit(app.exec_())

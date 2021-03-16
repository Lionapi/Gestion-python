# coding: utf-8

import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import functools
import pymysql
import win10toast
import datetime
import time

def DBconnection():
    con, h, u, p, bd = "", "localhost", "user", "password", "appgestcom"

    try:
        con = pymysql.connect(host = h, user = u, password = p, db = bd)
    except Exception as e:
        msger = QtWidgets.QMessageBox()
        msger.setWindowIcon(QtGui.QIcon("ma.jpg"))
        msger.setWindowTitle("Error")
        msger.setIcon(QtWidgets.QMessageBox.Critical)
        msger.setText("Connection error : {}".format(e))
        msger.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msger.setDefaultButton(QtWidgets.QMessageBox.Ok)
        splash.close()
        msger.buttonClicked.connect(lambda: sys.exit(app.exec()))
        msger.exec()  

    return con

def Createproduct(n, d, p):
    try:
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = "" 

        with DBconnection().cursor() as c:
            sql = "INSERT INTO products SET name = %s, description = %s, price = %s, created = %s"
            c.execute(sql, (n, d, p, dt))

            if c.rowcount > 0:
                data = "Data created."
            else:
                data = "Data wasn't created."

            c.close()

        DBconnection().commit()
    except:
        DBconnection().rollback()
    finally:
        DBconnection().close()
    
    return win10toast.ToastNotifier().show_toast("Create product", data, icon_path="ma.ico", duration=4, threaded=True)

def Readallproducts():
    try:
        allproducts, data = {}, []

        with DBconnection().cursor() as c:
            sql = "SELECT * FROM products"
            c.execute(sql)
            result = c.fetchall()

            if c.rowcount > 0:
                for r in result:
                    data.append({
                        "id": r[0], 
                        "name": r[1], 
                        "description": r[2], 
                        "price": r[3], 
                        "created": r[4].strftime('%Y/%m/%d %H:%M:%S'), 
                        "modified": r[5].strftime('%Y/%m/%d %H:%M:%S')
                    })
            
            c.close()
            allproducts["records"] = data

        DBconnection().commit()
    except:
        DBconnection().rollback()
    finally:
        DBconnection().close()

    return allproducts

def Readoneproduct(id):
    try:
        oneproduct, data = {}, []

        with DBconnection().cursor() as c:
            sql = "SELECT * FROM products WHERE id = %s LIMIT 0,1"
            c.execute(sql, id)
            result = c.fetchall() #fetchone()

            if c.rowcount > 0:
                for r in result:
                    data.append({
                        "id": r[0],
                        "name": r[1], 
                        "description": r[2], 
                        "price": r[3] #,
                        #"created": r[4].strftime('%Y/%m/%d %H:%M:%S'), 
                        #"modified": r[5].strftime('%Y/%m/%d %H:%M:%S')
                    })
            
            c.close()
            oneproduct["records"] = data

        DBconnection().commit()
    except:
        DBconnection().rollback()
    finally:
        DBconnection().close()

    return oneproduct

def Updateproduct(n, d, p, id):
    try:
        data = "" 

        with DBconnection().cursor() as c:
            sql = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
            c.execute(sql, (n, d, p, id))

            if c.rowcount > 0:
                data = "Data updated."
            else:
                data = "Data wasn't updated."

            c.close()

        DBconnection().commit()
    except:
        DBconnection().rollback()
    finally:
        DBconnection().close()
    
    return win10toast.ToastNotifier().show_toast("Update product", data, icon_path="ma.ico", duration=4, threaded=True)

def Deleteproduct(id):
    try:
        data = ""

        with DBconnection().cursor() as c:
            sql = "DELETE FROM products WHERE id = %s"
            c.execute(sql, id)

            if c.rowcount > 0:
                data = "Data deleted."
            else:
                data = "Data wasn't deleted."

            c.close()

        DBconnection().commit()
    except:
        DBconnection().rollback()
    finally:
        DBconnection().close()

    return win10toast.ToastNotifier().show_toast("Delete product", data, icon_path="ma.ico", duration=4, threaded=True)

#############################################################################################################################

#css

#progress bar
pgbr = "QProgressBar { border: 2px solid grey; border-radius: 5px; text-align: center; padding: 1.5px; padding-left: 1.5px; padding-right: 1.5px; background-color: transparent; } QProgressBar::chunk { background-color: #88b0eb; }"

#btn create
btna = "border: 2px solid #fff; border-radius: 10px; padding: 5px; padding-left: 5px; padding-right: 5px; min-width: 50px; max-width: 50px; min-height: 11px; max-height: 11px; color: #fff; background-color: #2bbbad;"

#btn update
btne = "border: 2px solid #fff; border-radius: 10px; padding: 5px; padding-left: 5px; padding-right: 5px; min-width: 50px; max-width: 50px; min-height: 11px; max-height: 11px; color: #fff; background-color: #ffbb33;"

#btn delete
btnd = "border: 2px solid #fff; border-radius: 10px; padding: 5px; padding-left: 5px; padding-right: 5px; min-width: 50px; max-width: 50px; min-height: 11px; max-height: 11px; color: #fff; background-color: #ff3547;"

#input (line edit & text edit)
input = "outline: none; border: none; border-bottom: 1px solid #000; border-radius: 0; background-color: #fff; color: #000;"

def Dia_create():
    winau.setWindowTitle("Create product")
    winau.lename.setText("")
    winau.txtedescription.setText("")
    winau.leprice.setText("")
    winau.btnb.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Close)
    winau.btnb.button(QtWidgets.QDialogButtonBox.Ok).setDefault(True)
    winau.btnb.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: (win.tableWidget.setRowCount(0),
                                                                                Createproduct(winau.lename.text(), winau.txtedescription.toPlainText(), int(winau.leprice.text())),
                                                                                Refrestable(), winau.close()))
    winau.btnb.button(QtWidgets.QDialogButtonBox.Close).clicked.connect(lambda: winau.close())
    winau.exec()

def Dia_update(id):
    pro = Readoneproduct(id)["records"][0]
    winau.setWindowTitle("Update product")
    winau.lename.setText(pro["name"])
    winau.txtedescription.setText(pro["description"])
    winau.leprice.setText(str(pro["price"]))
    winau.btnb.setStandardButtons(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Close)
    winau.btnb.button(QtWidgets.QDialogButtonBox.Save).setDefault(True)
    winau.btnb.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(lambda: (win.tableWidget.setRowCount(0),
                                                                                Updateproduct(winau.lename.text(), winau.txtedescription.toPlainText(), int(winau.leprice.text()), id),
                                                                                Refrestable(), winau.close()))
    winau.btnb.button(QtWidgets.QDialogButtonBox.Close).clicked.connect(lambda: winau.close())
    winau.exec()

def Msgdelete(id):
    msgdel = QtWidgets.QMessageBox()
    msgdel.setWindowIcon(QtGui.QIcon("ma.jpg"))
    msgdel.setWindowTitle("Delete product")
    msgdel.setIcon(QtWidgets.QMessageBox.Warning)
    msgdel.setText("Do you want to delete this product ?")
    msgdel.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msgdel.setDefaultButton(QtWidgets.QMessageBox.No)
    msgdel.buttonClicked.connect(lambda: Refrestable())
    val = msgdel.exec()

    if val == QtWidgets.QMessageBox.Yes:
        win.tableWidget.setRowCount(0)
        Deleteproduct(id)
        Refrestable()

def Refrestable():
    pdts = Readallproducts()["records"]
    win.tableWidget.setRowCount(len(pdts))
    row = 0
    for p in pdts:
        win.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(p["id"])))
        win.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p["name"]))
        win.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p["description"]))
        win.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(p["price"])))
        btn_e = QtWidgets.QPushButton("Edit")
        btn_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_e.setStyleSheet(btne)
        btn_e.clicked.connect(functools.partial(Dia_update, p["id"]))
        win.tableWidget.setCellWidget(row, 4, btn_e)
        btn_d = QtWidgets.QPushButton("Delete")
        btn_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_d.setStyleSheet(btnd)
        btn_d.clicked.connect(functools.partial(Msgdelete, p["id"]))
        win.tableWidget.setCellWidget(row, 5, btn_d)
        row += 1

def Findinlist(val):
    for x in range(0, win.tableWidget.rowCount()):
        for y in range(0, win.tableWidget.columnCount()):
            if win.tableWidget.item(x, y) and val.lower() not in win.tableWidget.item(x, y).text().lower():
                win.tableWidget.setRowHidden(x, True)

    for x in range(0, win.tableWidget.rowCount()):
        for y in range(0, win.tableWidget.columnCount()):
            if win.tableWidget.item(x, y) and val.lower() in win.tableWidget.item(x, y).text().lower():
                win.tableWidget.setRowHidden(x, False)

#https://likegeeks.com/pyqt5-tutorial/

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    #splashscreen
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('splash.png'), QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(QtGui.QPixmap('splash.png').mask())
    splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    
    progressBar = QtWidgets.QProgressBar(splash)
    progressBar.setStyleSheet(pgbr)
    progressBar.setAlignment(QtCore.Qt.AlignCenter)
    progressBar.setGeometry(20, QtGui.QPixmap('splash.png').height() - 50, QtGui.QPixmap('splash.png').width() - 40, 20)

    splash.setEnabled(False)
    splash.show()
    splash.showMessage("<h4><font color='black'>Loading ...</font></h4>", QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter, QtCore.Qt.black)

    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
           app.processEvents()

    #Views
    win = uic.loadUi("product.ui")
    winau = uic.loadUi("auproduct.ui")

    # ordre des champs
    win.setTabOrder(win.lesrch, win.btn_a)
    win.setTabOrder(win.btn_a, win.tableWidget)
    winau.setTabOrder(winau.lename, winau.txtedescription)
    winau.setTabOrder(winau.txtedescription, winau.leprice)

    winau.lename.setStyleSheet(input)
    winau.txtedescription.setStyleSheet(input)
    winau.leprice.setStyleSheet(input)
    
    # data of table
    Refrestable()

    # redimentionne la taille des colonnes en fonction du contenu
    win.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    win.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    #win.tableWidget.resizeColumnsToContents()

    # cache la colonne des id
    win.tableWidget.setColumnHidden(0, True)

    #btn add product function
    win.btn_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    win.btn_a.setStyleSheet(btna)
    win.btn_a.clicked.connect(lambda: Dia_create())

    # on recherche dans le tableau avec la barre de recherche
    win.lesrch.setStyleSheet(input)
    win.lesrch.textChanged.connect(lambda: Findinlist(win.lesrch.text()))

    #close splash
    splash.close()

    # affiche la fenetre
    win.showMaximized()
    sys.exit(app.exec())

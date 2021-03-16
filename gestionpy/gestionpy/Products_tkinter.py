# coding: utf-8

import tkinter
import tkinter.ttk
import pymysql

def DBconnection():
    con, h, u, p, bd = "", "localhost", "Franck-Lionel", "Franck-Lionel007", "appgestcom"

    try:
        con = pymysql.connect(host = h, user = u, password = p, db = bd)
    except Exception as e:
        print("Connection impossible à la base de données: {}".format(e))

    return con

def Createproduct():
    try:
        n = None #flask.request.get_json()['name']
        d = None #flask.request.get_json()['description']
        p = None #flask.request.get_json()['price']
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
    
    return data

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

def Readoneproduct():
    try:
        id = None #flask.request.get_json()['id']
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

def Updateproduct():
    try:
        n = None #flask.request.get_json()['name']
        d = None #flask.request.get_json()['description']
        p = None #flask.request.get_json()['price']
        id = None #flask.request.get_json()['id']
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
    
    return data

def Deleteproduct():
    try:
        id = None #flask.request.get_json()['id']
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

    return data

def Apptkinter():
    app = tkinter.Tk()
    app.iconbitmap("ma.png")
    app.title("Gestion de produits")
    app.minsize(800, 700)
    app.geometry("{}x{}".format(app.winfo_screenwidth(), app.winfo_screenheight()))

    table = tkinter.ttk.Treeview(app)
    table["columns"] = (1, 2, 3, 4, 5, 6)
    table["show"] = "headings"

    table.column(1, minwidth=1, anchor="center")
    table.column(2, minwidth=20, anchor="center")
    table.column(3, minwidth=500, anchor="center")
    table.column(4, minwidth=2, anchor="center")
    table.column(5, minwidth=5, anchor="center")
    table.column(6, minwidth=5, anchor="center")

    table.heading(1, text="N°")
    table.heading(2, text="Nom")
    table.heading(3, text="Description")
    table.heading(4, text="Prix")
    table.heading(5, text="Date de création")
    table.heading(6, text="Date de modification") 

    i=1

    for d in Readallproducts()["records"]:
        table.insert("", "end", tags=i, values=(d["id"], d["name"], d["description"], d["price"], d["created"], d["modified"]))
        if i % 2 == 0:
            table.tag_configure(i, background="silver")
        i+=1

    table.pack(fill="x", padx=10, pady=10)

    app.mainloop()

Apptkinter()
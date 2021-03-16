# coding: utf-8

import flask
import pymysql
import datetime

app = flask.Flask(__name__)

def DBconnection():
    con, h, u, p, bd = "", "localhost", "user", "password", "appgestcom"

    try:
        con = pymysql.connect(host = h, user = u, password = p, db = bd)
    except Exception as e:
        print("Connection impossible à la base de données: {}".format(e))

    return con

@app.route('/', methods = ['GET', 'POST'])
def Index():
    return flask.render_template('index_flask.html')

@app.route('/createproduct', methods = ['POST'])
def Createproduct():
    try:
        n = flask.request.get_json()['name']
        d = flask.request.get_json()['description']
        p = flask.request.get_json()['price']
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

@app.route('/readallproducts', methods = ['GET'])
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

@app.route('/readoneproduct', methods = ['POST'])
def Readoneproduct():
    try:
        id = flask.request.get_json()['id']
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

@app.route('/updateproduct', methods = ['POST'])
def Updateproduct():
    try:
        n = flask.request.get_json()['name']
        d = flask.request.get_json()['description']
        p = flask.request.get_json()['price']
        id = flask.request.get_json()['id']
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

@app.route('/deleteproduct', methods = ['POST'])
def Deleteproduct():
    try:
        id = flask.request.get_json()['id']
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

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import mysql.connector
import json
import datetime
import os
from dotenv import load_dotenv
import generator.member as member

load_dotenv()


app = Flask(__name__)
CORS(app)


@app.get('/download/<fileName>')
def generate_timetable(fileName):
    try:
        # d = datetime.datetime.now()
        # d = filename
        # fileName = '{}.csv'.format(str(d).replace(":", "-"))
        # print(fileName)
        member.start_BFSRB(fileName)
        path = "./generator/timetables/{}".format(fileName)
        return send_file(path, as_attachment=True)
    except Exception as e:
        print("error", e)
        return {"success": False, "error": str(e)}, 500


@app.get('/modules')
def get_modules():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM module"
        mycursor.execute(sql)
        # this will extract row headers
        # row_headers = [x[0] for x in mycursor.description]

        myresult = mycursor.fetchall()
        # json_data = []
        # for result in myresult:
        #     json_data.append(dict(zip(row_headers, result)))
        # print(json.dumps(json_data))
        return {
            "success": True,
            "data": myresult
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }, 500


@app.get('/modules/<code>')
def get_module(code):
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM module WHERE code = %s"
        val = (code,)
        mycursor.execute(sql, val)
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        return {
            "data": json.dumps(json_data),
            "success": True
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }, 500


@app.post('/modules')
def add_module():
    try:
        code = request.json.get('code')
        name = request.json.get('name')
        lecturer_id = request.json.get('lecturer_id')
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO module (code, name, lecturer_id) VALUES (%s, %s, %s)"
        val = (code, name, lecturer_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        if(mycursor.rowcount == 1):
            return {"success": True, "data": "Module added"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.put('/modules/<code_old>')
def edit_module(code_old):
    try:
        code = request.json.get('code')
        name = request.json.get('name')
        lecturer_id = request.json.get('lecturer_id')
        print(code, name, lecturer_id, code_old)
        # lecturer_id = request.form['lecturer_id']
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        # if(code == code_old):
        sql = "UPDATE module SET code = %s, name = %s, lecturer_id = %s WHERE code = %s"
        val = (code, name, lecturer_id, code_old)
        # print(sql)
        mycursor.execute(sql, val)
        mydb.commit()
        # else:
        #     # insert new module and delete code_old
        #     sql = "INSERT INTO module (code, name, lecturer_id) VALUES (%s, %s, %s)"
        #     val = (code, name, lecturer_id)
        #     mycursor.execute(sql, val)
        #     mydb.commit()
        #     sql = "DELETE FROM module WHERE code = %s"
        #     val = (code_old,)
        #     mycursor.execute(sql, val)
        #     mydb.commit()

        print(mycursor.rowcount, "record updated.")
        return {"success": True, "data": "Module updated"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.delete('/modules/<code>')
def remove_module(code):
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM module WHERE code = %s"
        val = (code,)
        mycursor.execute(sql, val)
        mydb.commit()
        return {"success": True, "data": "Module deleted"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.get('/lecturers')
def get_lecturers():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM lecturer"
        mycursor.execute(sql)
        # print(mycursor.fetchall())
        # this will extract row headers
        # row_headers = [x[0] for x in mycursor.description]

        myresult = mycursor.fetchall()
        # print(myresult)
        # for result in myresult:
        #     print(result, '\n')

        # json_data = []
        # for result in myresult:
        #     json_data.append(dict(zip(row_headers, result)))
        return {"data": myresult, "success": True}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.get('/lecturers/<id>')
def get_lecturer(id):
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM lecturer WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        return {"data": json.dumps(json_data), "success": True}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.post('/lecturers')
def add_lecturer():
    name = None
    try:
        name = request.json.get('name')
        if name == None:
            return {"success": False, "message": "missing parameters"}, 500
    except:
        return {"success": False, "message": "missing parameters"}, 500
    try:

        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO lecturer (name) VALUES (%s)"
        val = (name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return {"success": True, "data": "Lecturer added"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.put('/lecturers/<id>')
def edit_lecturer(id):
    name = None
    try:
        name = request.json.get('name')
        if name == None:
            print("Missing parameters123")
            return {"success": False, "message": "missing parameters"}, 500
    except:
        print("Missing parameters")
        return {"success": False, "message": "missing parameters"}, 500
    try:

        # print("name = ", name)
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )

        mycursor = mydb.cursor()
        sql = "UPDATE lecturer SET name = %s WHERE id = %s"
        val = (name, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record updated.")
        return {"success": True, "message": "Lecturer updated"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@app.delete('/lecturers/<id>')
def remove_lecturer(id):
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            unix_socket=os.getenv('DB_SOCKET'),
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM lecturer WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record deleted.")
        return {"success": True, "data": "Lecturer deleted"}
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)

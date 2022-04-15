import rlcompleter
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pymysql
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

cors = CORS(app)


@app.route('/students', methods=['GET'])
def get():
    # To connect MySQL database
    conn = pymysql.connect(host='b0clzpugielugeh7wawd-mysql.services.clever-cloud.com', user='uw4yfuekpswusgii',
                           password='pMKj4JgoV3JalvUv4kph', db='b0clzpugielugeh7wawd')

    cur = conn.cursor()

    # cur.execute(f"SELECT * FROM bike_details ORDER BY {id} DESC;")
    cur.execute("SELECT * FROM students")
    output = cur.fetchall()

    print(type(output))  # this will print tuple

    for rec in output:
        print(rec)

    # To close the connection
    conn.close()

    return jsonify(output)


@app.route('/students', methods=['DELETE'])
def deleteRecord():
    # To connect MySQL database
    conn = pymysql.connect(host='b0clzpugielugeh7wawd-mysql.services.clever-cloud.com', user='uw4yfuekpswusgii',
                           password='pMKj4JgoV3JalvUv4kph', db='b0clzpugielugeh7wawd')
    cur = conn.cursor()
    id = int(request.args.get('Roll_no'))

    query = f"Delete from students WHERE Roll_no ={'Roll_no'}"
    cur.execute(query)
    conn.commit()
    print(cur.rowcount, "record(s) deleted")

    return {"result": "Record deleted Succesfully"}


@app.route('/students', methods=['POST'])
def insertRecord():
    conn = pymysql.connect(host='b0clzpugielugeh7wawd-mysql.services.clever-cloud.com', user='uw4yfuekpswusgii',
                           password='pMKj4JgoV3JalvUv4kph', db='b0clzpugielugeh7wawd')

    # get raw json values
    raw_json = request.get_json()
    # print(raw_json)
    # quit()

    
    first_name = raw_json["First_Name"] ;
    Last_Name = raw_json["Last_Name"] ;
    branch = raw_json["Branch"] ;

    sql = f"INSERT INTO students (Roll_no,First_Name,Last_Name,branch) VALUES (NULL,'{first_name}','{Last_Name}','{branch}')"
    print(sql)
    cur = conn.cursor()

    cur.execute(sql)
    conn.commit()
    return {"result": "Record inserted Succesfully"}


@app.route('/students', methods=['PUT'])
def updateRecord():
    conn = pymysql.connect(host='b0clzpugielugeh7wawd-mysql.services.clever-cloud.com', user='uw4yfuekpswusgii',
                           password='pMKj4JgoV3JalvUv4kph', db='b0clzpugielugeh7wawd')

    raw_json = request.get_json()

    # print(type(raw_json));

    raw_json = request.get_json()
    roll_no = raw_json['Roll_no']
    first_name= raw_json["First_Name"]
    Last_Name = raw_json["Last_Name"]
    branch = raw_json["Branch"]
   


    sql_update_query = f"UPDATE students SET First_Name = '{first_name}',Last_Name ='{Last_Name}',Branch = '{branch}' WHERE Roll_no = '{roll_no}'"
    cur = conn.cursor()
    cur.execute(sql_update_query)
    conn.commit()
    return {"result": "Record updated Succesfully"}


if __name__ == "__main__":
 app.run(debug=True)
 app.run (host="0.0.0.0", port=int("1234"), debug=True)

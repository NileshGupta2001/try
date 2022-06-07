'''
!C:/Users/dell/AppData/Local/Programs/Python/Python310/python.exe
'''
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    print("Content-Type: text/html")
    print()

    #import cgi
    print("<h1>Welcome to Python</h1>")
    print("<hr/>")
    print("<h1>Using input tag</h1>")
    print("<body bgcolor='red'>")

    #form=cgi.FieldStorage()

    '''
    userid=form.getvalue("userid")
    username=form.getvalue("username")
    address=form.getvalue("address")
    gender=form.getvalue("gender")
    hindi=form.getvalue("hindi")
    english=form.getvalue("english")
    urdu=form.getvalue("urdu")
    select1=form.getvalue("select")
    '''
    
    
    import mysql.connector
    from mysql.connector import errorcode
    from mysql.connector.constants import ClientFlag
    #import pyodbc
    Server = 'registerdbnew.mysql.database.azure.com'
    database = 'register'
    username = 'nilesh'
    password = 'NewPass@21'   
    driver= '{ODBC Driver 17 for SQL Server}'

    try:
    #con=pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+Server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    #con=mysql.connector.connect(user='root',password='',host='localhost',database='webpython',port='3307')
        con = mysql.connector.connect(user="nilesh", password="NewPass@21", host="registerdbnew.mysql.database.azure.com", port=3306, database="register",  ssl_ca=r"C:\Users\dell\Downloads\BaltimoreCyberTrustRoot.crt.pem",ssl_disabled=False)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cur=con.cursor()

        if request.method=='POST':
            singup=request.form
            userid=singup['userid']
            username=singup['username']
            address=singup['address']
            gender=singup['gender']
            hindi=singup['hindi']
            english=singup['english']
            urdu=singup['urdu']
            select1=singup['select']
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(userid,username,address,gender,hindi,english,urdu,select1))
            con.commit()

            cur.close()
            con.close()
            print("<h3>YOUR RECORD HAS BEEN SUCCESSFULLY INSERTED!!</h3>")
            print("<a href='https://nice-bush-0404bfe10.1.azurestaticapps.net'>GO BACK?</a>")
    return 'REGISTER SUCCESSFUL'

if __name__ == '__main__':
  app.run(debug=True)

import ibm_db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_cors import CORS, cross_origin

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=cwy91974;PWD=aj53b8isyFaXUrZy;","","")


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
@cross_origin()
def signup():
    global EMAIL
    if request.method=='GET':
        return render_template('signup.html')
    
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        EMAIL=email
        password=request.form['password']
        sql="SELECT * FROM signup WHERE email=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return redirect(url_for('signup'))
        else:
            sql="INSERT INTO signup VALUES(?,?,?)"
            stmt=ibm_db.prepare(conn,sql)
            ibm_db.bind_param(stmt,1,name)
            ibm_db.bind_param(stmt,2,email)
            ibm_db.bind_param(stmt,3,password)
            ibm_db.execute(stmt)
            return redirect(url_for('login'))

    """
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        sql="INSERT INTO signup VALUES(?,?,?)"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,email)
        ibm_db.bind_param(stmt,3,password)
        ibm_db.execute(stmt)
    return redirect(url_for('login'))

    #return render_template('signup.html')
"""



@app.route('/login', methods=['POST','GET'])
def login():
    global EMAIL
    if request.method=='POST':
        email=request.form['email']
        EMAIL=email
        password=request.form['password']
        sql="SELECT * FROM signup WHERE email=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
           #return render_template('home.html')
            return redirect(url_for('home'))
        else:
            error = "Invalid email/password"  
            #flash("email/ Password isincorrect! ")
            return redirect(url_for('login'))
    elif request.method=='GET':
        return render_template('login.html')
    #return render_template('login.html' ,msg="success")

@app.route('/forgot', methods=['POST','GET'])
def forgot():
    return render_template('forgot.html' ,msg="success")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/jobApplication')
def jobApplication():
    return render_template('jobApplication.html', msg="success")

@app.route('/category')
def category():
    return render_template('category.html', msg="success")

@app.route('/jobList')
def jobList():
    return render_template('jobList.html', msg="success")

@app.route('/applicationSuccess')
def applicationSuccess():
    return render_template('applicationSuccess.html', msg="success")



if __name__=='__main__':
    app.run(debug=True)

       
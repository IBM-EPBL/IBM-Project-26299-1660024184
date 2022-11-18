import ibm_db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask import session
import sqlite3
import os

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=cwy91974;PWD=aj53b8isyFaXUrZy;","","")

con=sqlite3.connect("myimage.db")
con.execute("create table if not exists image(pid integer primary key,img TEXT)")
con.close()

app = Flask(__name__)
app.secret_key = '//sd_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_FOLDER']="static\images"

l = []

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/home')
def home():
    login=False
    if 'usernameid' and 'passwordid' in session:
        login=True
    return render_template('index.html', login=login)

@app.route('/signup', methods=['POST','GET'])
def signup():
    global EMAIL
    if request.method=='GET':
        return render_template('signup.html')
    
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        #EMAIL=email
        password=request.form['password']
        secret=request.form['secret']
        sql="SELECT * FROM authentication WHERE email=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return redirect(url_for('signup'))
        else:
            sql="INSERT INTO authentication VALUES(?,?,?,?)"
            stmt=ibm_db.prepare(conn,sql)
            ibm_db.bind_param(stmt,1,name)
            ibm_db.bind_param(stmt,2,email)
            ibm_db.bind_param(stmt,3,password)
            ibm_db.bind_param(stmt,4,secret)

            ibm_db.execute(stmt)
            return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    global EMAIL
    if request.method=='POST':
        email=request.form['email']
        #session['emailid']=email
        password=request.form['password']
        #session['passwordid']=password
        EMAIL=email
        l.append(email)
        sql="SELECT * FROM authentication WHERE email=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        if account:
            #session['loggedin'] = True
            #session['email'] = email
           #return render_template('home.html')
            return redirect(url_for('home'))
        else:
            error = "Invalid email/password"  
            return redirect(url_for('login'))
    elif request.method=='GET':
        return render_template('login.html')

@app.route('/forgot', methods=['POST','GET'])
def forgot():
    if request.method=='POST':
        email=request.form['email']
        remail=email
        secret=request.form['secret']
        sql="SELECT * FROM authentication WHERE email=? AND secret=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,secret)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        if account:
            return redirect(url_for('reset'))
        else:
            return redirect(url_for('forgot'))
    elif request.method=='GET':
        return render_template('forgot.html')

@app.route('/reset', methods=['POST','GET'])
def reset():
    if request.method=='POST':
        email=request.form['email']
        confirm=request.form['confirm']
        sql="UPDATE authentication SET password=? where email=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,confirm)
        ibm_db.bind_param(stmt,2,email)
        ibm_db.execute(stmt)
        return redirect(url_for('login'))
    else:
        return render_template('reset.html')

@app.route('/contacts', methods=['POST','GET'])
def contacts():
    if request.method=='POST':
            return redirect(url_for('contactsSuccess'))
    return render_template('contacts.html')

@app.route('/jobApplication', methods=['POST','GET'])
def jobApplication():
    if request.method=='POST':
        ufname=request.form['ufname']
        ulname=request.form['ulname']
        uemail=request.form['uemail']
        uphone=request.form['uphone']
        udob=request.form['udob']
        ugender=request.form['ugender']
        curAdd=request.form['curAdd']
        curzipid=request.form['curzipid']
        curcity=request.form['curcity']
        curstate=request.form['curstate']
        curcntryid=request.form['curcntryid']

        Xboard=request.form['Xboard']
        XPercent=request.form['XPercent']
        XYOP=request.form['XYOP']

        XIIboard=request.form['XIIboard']
        XIIPercent=request.form['XIIPercent']
        XIIYOP=request.form['XIIYOP']

        GradPercent=request.form['GradPercent']
        GradYOP=request.form['GradYOP']

        MastersPercent=request.form['MastersPercent']
        MastersYOP=request.form['MastersYOP']

        work=request.form['work']
        skill=request.form['skill']

        sql="INSERT INTO application VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,ufname)
        ibm_db.bind_param(stmt,2,ulname)
        ibm_db.bind_param(stmt,3,uemail)
        ibm_db.bind_param(stmt,4,uphone)
        ibm_db.bind_param(stmt,5,udob)
        ibm_db.bind_param(stmt,6,ugender)
        ibm_db.bind_param(stmt,7,curAdd)
        ibm_db.bind_param(stmt,8,curzipid)
        ibm_db.bind_param(stmt,9,curcity)
        ibm_db.bind_param(stmt,10,curstate)
        ibm_db.bind_param(stmt,11,curcntryid)

        ibm_db.bind_param(stmt,12,Xboard)
        ibm_db.bind_param(stmt,13,XPercent)
        ibm_db.bind_param(stmt,14,XYOP)

        ibm_db.bind_param(stmt,15,XIIboard)
        ibm_db.bind_param(stmt,16,XIIPercent)
        ibm_db.bind_param(stmt,17,XIIYOP)

        ibm_db.bind_param(stmt,18,GradPercent)
        ibm_db.bind_param(stmt,19,GradYOP)

        ibm_db.bind_param(stmt,20,MastersPercent)
        ibm_db.bind_param(stmt,21,MastersYOP)

        ibm_db.bind_param(stmt,22,work)
        ibm_db.bind_param(stmt,23,skill)

        ibm_db.execute(stmt)
        return redirect(url_for('applicationSuccess'))
    elif request.method=='GET':
        return render_template('jobApplication.html', msg = "success")

@app.route('/category')
def category():
    return render_template('category.html', msg="success")

@app.route('/jobList')
def jobList():
    return render_template('jobList.html', msg="success")

@app.route('/applicationSuccess')
def applicationSuccess():
    return render_template('applicationSuccess.html', msg="success")

@app.route('/contactsSuccess')
def contactsSuccess():
    return render_template('contactsSuccess.html', msg="success")

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/post",methods=['GET','POST'])
def post():
    con = sqlite3.connect("myimage.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from image")
    data = cur.fetchall()
    con.close()

    if request.method=='POST':
        upload_image=request.files['upload_image']

        if upload_image.filename!='':
            filepath=os.path.join(app.config['UPLOAD_FOLDER'],upload_image.filename)
            upload_image.save(filepath)
            con=sqlite3.connect("myimage.db")
            cur=con.cursor()
            cur.execute("insert into image(img)values(?)",(upload_image.filename,))
            con.commit()
            flash("File Upload Successfully","success")

            con = sqlite3.connect("myimage.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("select * from image")
            data=cur.fetchall()
            con.close()
            return render_template("post.html",data=data)
    return render_template("post.html",data=data)

@app.route('/profile')
def profile():
    students = []
    r = l.pop()
    sql = f"SELECT * FROM authentication WHERE email='{r}' "
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        students.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)
    if students:
        return render_template("profile.html", students = students)

@app.route('/delete_record/<string:id>')
def delete_record(id):
    try:
        con=sqlite3.connect("myimage.db")
        cur=con.cursor()
        cur.execute("delete from image where pid=?",[id])
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Deleted Failed", "danger")
    finally:
        return redirect(url_for("post"))
        con.close()

if __name__ == '__main__':
    app.run(debug=True)



if __name__=='__main__':
    app.run(debug=True)

       
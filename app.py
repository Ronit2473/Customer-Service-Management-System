
from tkinter import E
from flask import Flask, render_template,request,redirect, session, url_for
from flask_mysqldb import MySQL
from waitress import serve



app=Flask(__name__)
app.secret_key='barney'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='csm'

mysql=MySQL(app)

@app.route('/home')
def home():
    return render_template('home.html')
    

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        fm=request.form
        a=fm['cname']
        b=fm['ccontact']
        c=fm['cmail']
        d=fm['caddress']
        e=fm['ccarno']
        f=fm['cpack']
        q="insert into csm(name,contact,email,address,car_no,package) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/book')
    return render_template('signup.html')


@app.route('/pack')
def pack():
    return render_template('pack.html')

from flask import flash

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        fm = request.form
        name = fm['aname'].strip()  # Remove leading and trailing whitespaces
        pwd = fm['apwd'].strip()    # Remove leading and trailing whitespaces
        cursor = mysql.connection.cursor()
        try:
            # Use parameterized query to prevent SQL injection
            cursor.execute("SELECT * FROM admin WHERE name = %s AND password = %s", (name, pwd))
            result = cursor.fetchall()
            count = cursor.rowcount
            if count == 1:
                return redirect('/users')
            else:
                flash("Incorrect Name/Password", "error")
                return render_template("admin.html")
        except Exception as e:
            flash("An error occurred: " + str(e), "error")
            return render_template("admin.html")
        finally:
            cursor.close()  # Close cursor after executing the query

    return render_template("admin.html")


     
@app.route('/users')
def users():
    cursor=mysql.connection.cursor()
    q="select * from csm"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('users.html',user=res)   

@app.route('/remove/<string:id>')
def remove(id):
    q="delete from csm where id='"+id+"'"
    cursor=mysql.connection.cursor()
    cursor.execute(q)
    mysql.connection.commit()
    return redirect('/users')

@app.route('/edit/<string:id>')
def edit(id):
    cursor=mysql.connection.cursor()
    q="select * from csm where id='"+id+"'"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('edit.html',user=res)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        fm=request.form
        a=fm['cname']
        b=fm['ccontact']
        c=fm['cmail']
        d=fm['caddress']
        e=fm['ccarno']
        f=fm['cpack']
        g=fm['id']
        q="update csm set name='"+a+"',contact='"+b+"',email='"+c+"',address='"+d+"',car_no='"+e+"',package='"+f+"' where id='"+g+"'"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/users')

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        fm=request.form
        a=fm['search']
        cursor=mysql.connection.cursor()
        q="select * from csm where name='"+a+"'"
        cursor.execute(q)
        res=cursor.fetchall()
    return render_template('users.html',user=res)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        fm = request.form
        slot_date = fm['slot_date']
        slot_time = fm['slot_time']
        car_number = fm['car_number']  # Retrieve car number from the form
        # Now, you can use the car number to perform any necessary actions, such as saving the booking information to the database
        # You can also perform validation on the input data before saving it
        flash("Slot booked successfully!", "success")
        return redirect('/bookings')  # Redirect to the booking page again or any other page you prefer
    return render_template('book.html')


def get_booking_information():
    """
    Fetch booking information from the database.
    Modify this function according to your database schema and connection.
    """
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name, slot_date, slot_time FROM bookings") 
    users = cursor.fetchall()
    cursor.close()
    return users

@app.route('/bookings')
def bookings():
    # Fetch booking information from the database
    users = get_booking_information()
    return render_template('bookings.html', users=users)





if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)
    


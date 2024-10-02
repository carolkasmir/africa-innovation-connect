from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mentorship', methods=['GET', 'POST'])
def mentorship():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mentorship_requests (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()
        
        flash('Your mentorship request has been submitted successfully!', 'success')
        return redirect(url_for('mentorship'))
    
    return render_template('mentorship.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact_submissions (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.secret_key = Config.SECRET_KEY
    app.run(debug=True)


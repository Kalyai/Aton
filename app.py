from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = '0007'

def get_db_connection():
    con = sqlite3.connect('clients.db')
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']

    con = get_db_connection()
    sql = "SELECT * FROM users WHERE login = ? AND password = ?"
    user = con.execute(sql, (login, password)).fetchone()
    con.close()

    if user:
        session['user_full_name'] = user['full_name']
        return redirect(url_for('clients'))
    else:
        flash('Неправильный логин или пароль')
        return render_template('login.html')

@app.route('/clients')
def clients():
    if 'user_full_name' not in session:
        return redirect(url_for('index'))

    user_full_name = session.get('user_full_name')

    con = get_db_connection()
    sql = "SELECT * FROM clients WHERE responsible_full_name = ?"

    clients = con.execute(sql, (user_full_name,)).fetchall()
    con.close()
    return render_template('clients.html', clients=clients)

@app.route('/update_status', methods=['POST'])
def update_status():
    if 'user_full_name' not in session:
        return redirect(url_for('index'))

    account_number = request.form['account_number']
    new_status = request.form['status']

    sql = "UPDATE clients SET status = ? WHERE account_number = ?"
    con = get_db_connection()
    con.execute(sql, (new_status, account_number))
    con.commit()
    con.close()
    return redirect(url_for('clients'))

if __name__ == '__main__':
    app.run(debug=True)

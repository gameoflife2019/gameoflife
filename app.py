
from flask import Flask, render_template, redirect, url_for, request, session, abort

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('admin_logged_in') or session.get('user_logged_in'):
        return render_template('login_selection.html')
    elif session.get('admin_logged_in'):
        return render_template('admin_home.html')
    else:
        return render_template('user_home.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['admin_logged_in'] = True
        return redirect(url_for('admin_home'))
    else
        flash('Invalid Entry')
        return home()

@app.route('/user_login', methods=['POST'])
def user_login():
    if request.form['password'] == 'password' and request.form['username'] == 'user':
        session['user_logged_in'] = True
        return redirect(url_for('user_home'))
    else
        flash('Invalid Entry')
        return home()

@app.route('/medicine/')
def medicine():
    return render_template('medicine.html')

if __name__ == '__main__':
    app.run(debug=true, host='0.0.0.0', port=5000)

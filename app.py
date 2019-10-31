from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login_selection.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        return redirect(url_for('admin_home'))
    else
        flash('Invalid Entry')
        return home()

@app.route('/user_login', methods=['POST'])
def user_login():
    if request.form['password'] == 'password' and request.form['username'] == 'user':
        return redirect(url_for('user_home'))
    else
        flash('Invalid Entry')
        return home()

@app.route('/medicine/')
def medicine():
    return render_template('medicine.html')

if __name__ == '__main__':
    app.run(debug=true, host='0.0.0.0', port=5000)

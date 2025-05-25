from flask import Flask, render_template, url_for, request, redirect, session
import secrets  

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  

users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Username already exists. Please choose another."
        users[username] = {'fullname': fullname, 'email': email, 'password': password}
        return redirect(url_for('login'))  
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username  
            return redirect(url_for('home'))  
        else:
            return "Invalid username or password."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
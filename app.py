from flask import Flask, render_template, session, request, redirect, url_for
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random value

# Simulated user data (replace with OAuth authentication)
users = {}

@app.route('/')
def home():
    user_info = session.get('user_info')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', user_info=user_info, current_time=current_time)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input
        email = request.form['email']
        name = request.form['name']

        # Simulate successful login (replace with OAuth authentication)
        user_info = {'name': name, 'email': email}
        session['user_info'] = user_info

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user_info', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

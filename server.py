from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def show_all_users():
    users = User.get_all()
    print(users)
    return render_template('read(all).html', all_users = users)

@app.route('/create')
def create_user():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def create_user_submit():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    User.add_new_user(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import *

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    email = request.form['email']
    # if uname == "admin" and passwrd == "admin":
    return f"Welcome {uname}. We will contact you on {email} shortly."


if __name__ == '__main__':
    app.run(debug=True)

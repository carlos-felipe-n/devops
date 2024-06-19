from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!s'

@app.route('/user')
def list_users():
    users = ['Carloss', 'Felipe', 'Nascimento', 'Souza']
    return f'<h1>{users}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
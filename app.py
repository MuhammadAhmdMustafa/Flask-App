from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Flask Lab App</h1><p>This is a demo for Static and Dynamic Code Analysis.</p>"

@app.route('/hello/<name>')
def hello(name):
    return f"<h2>Hello, {name}!</h2>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"<h3>Welcome {username}, but never send passwords like '{password}' in URL or response!</h3>"
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

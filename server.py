from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:num>/<name>')
def hello(num, name):
    return render_template('hello.html', num=num, name=name)

if __name__=='__main__':
    app.run(debug = True)

#The code above will create a web server and render a template (similar to server.js in MERN)

###pipenv install flask
###pipenv shell

##In our template html files we are using a *template engine* called Jinja

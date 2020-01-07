from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About Page!'


@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

if __name__ == "__main__":
    app.run(debug=True)

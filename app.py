from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    todos = [
        {
            'id' : 1,
            'text':'Learn Flask',
            'isComplete':False

        },
        {
            'id': 2,
            'text': 'Have Breakfast',
            'isComplete': True

        },
        {
            'id': 3,
            'text': 'Have tea',
            'isComplete': True

        }
    ]
    isAdmin = True
    return render_template('index.html', todos=todos ,isAdmin=isAdmin, name=name)


@app.route('/about')
def about():
    return 'About Page!'


@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == 'GET':        
        return render_template('contact.html')
    elif request.method == "POST":
        name = request.form.get('name')
        return render_template("contact.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

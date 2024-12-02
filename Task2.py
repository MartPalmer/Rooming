from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    from datetime import datetime
    current_year = datetime.now().year
    return render_template('home.html', year = current_year)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['emails']
        return f"Hello, {name}, your email is {email}"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
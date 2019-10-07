from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This is the Coding Dojo Counter Application"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else: 
        session['counter'] = 0

    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    
    return render_template("index.html")

@app.route('/add2', methods=['POST'])
def add2():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return redirect("/")

@app.route('/clear', methods=["POST"])
def clear():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
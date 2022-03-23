
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
#THIS WILL CHANGE!!!!! *********
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/info')

@app.route('/info')
def info():
    
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comments = session['comments'])
# END OF CHANGE

#KEEP THIS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)
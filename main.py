### Integrate HTML with Flask
## HTTP verb GET and post

from flask import Flask,redirect,url_for,render_template
'''
It creates an instance of the flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')



@app.route('/success/<int:score>')
def success(score):
    return "The Person has passes and the mark is "+ str(score)



@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the mark is "+ str(score)



###   Result checker 
@app.route('/results/<int:marks>')
def results(marks):
    results=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))




if __name__=="__main__":
    app.run(debug=True)



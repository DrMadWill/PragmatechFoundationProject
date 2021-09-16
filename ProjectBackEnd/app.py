from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('include/maxwill.html')



@app.route('/project')
def project():
    return render_template('include/will-project.html')


if __name__ == '__main__':
    
    app.run(debug=True)
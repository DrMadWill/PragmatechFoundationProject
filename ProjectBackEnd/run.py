from flask import Flask,redirect,render_template,request
from app import *


app=Flask(__name__)
@app.route('/')
def main():
    return render_template('maxwill.html',infos=infose,homeinfoes=homein)


@app.route('/project')
def project():
    return render_template('will-project.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        HomeInf =homein(
            info=request.form.get('HomeTitleText')) ;

        infose[0]['cardTime']=request.form.get('cardTime');
        infose[0]['cardTitle']=request.form.get('cardTitle');
        infose[0]['cardText']=request.form.get('cardText')
        db.session.add(HomeInf)
        db.session.commit()
        return redirect('/admin')
    return render_template('admin/adminpanel.html')


if __name__ == '__main__':
    app.run(debug=True)




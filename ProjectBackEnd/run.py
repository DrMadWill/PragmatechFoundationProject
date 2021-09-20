from flask import Flask,redirect,render_template,request
from app import *


app=Flask(__name__)
@app.route('/')
def main():
    return render_template('include/maxwill.html',infos=infose,homeinfoes=homeinf)


@app.route('/project')
def project():
    return render_template('include/will-project.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        HomeInf1 =homeinf(
            homeinfores=request.form.get('HomeTitleText')) ;
        db.session.add(HomeInf1)
        db.session.commit()
        
        return redirect('/admin')
    return render_template('controlpanel.html')


if __name__ == '__main__':
    app.run(debug=True)



# infose[0]['cardTime']=request.form.get('cardTime');
        # infose[0]['cardTitle']=request.form.get('cardTitle');
        # infose[0]['cardText']=request.form.get('cardText')
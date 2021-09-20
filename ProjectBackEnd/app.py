from flask import Flask,redirect,url_for,render_template,request

HomeInf=[
    'We make beautiful websites for all people.']



infose =[
    {
        'cardTime':'December 25.07.21`',
        'cardTitle':'how to become a web developer',
        'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
    },
    {
        'cardTime':'December 25.07.21`',
        'cardTitle':'how to become a web developer',
        'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
    }

]




app=Flask(__name__)
@app.route('/')
def main():
    return render_template('include/maxwill.html',infos=infose,homeinfoes=HomeInf)


@app.route('/project')
def project():
    return render_template('include/will-project.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        HomeInf[0] =request.form.get('HomeTitleText');

        infose[0]['cardTime']=request.form.get('cardTime');
        infose[0]['cardTitle']=request.form.get('cardTitle');
        infose[0]['cardText']=request.form.get('cardText')
        return redirect('/admin')
    return render_template('controlpanel.html')


if __name__ == '__main__':
    
    app.run(debug=True)
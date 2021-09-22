from flask import Flask,redirect,render_template,request
from app import *



@app.route('/')
def main():
    hinfolen=len(Homein.query.all())-1
    homeinfoall=Homein.query.all()
    homeinfo=homeinfoall[hinfolen]

    leng=len(Projectin.query.all())-4
    home = Projectin.query.all()
    home =home[::-1]
    return render_template('maxwill.html',home=home,len=leng,homeinfo=homeinfo)


@app.route('/project')
def project():
    return render_template('will-project.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        homeinfo=Homein(
            info=request.form.get('HomeTitleText'),
            infoimg=filename
        )
        
        db.session.add(homeinfo)
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/adminpanel.html')



# @app.route('/admin',methods=['GET','POST'])
# def adminpro():
#     if request.method=='POST':
#         file = request.files['pfile']
#         print(file)
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         proinfo=Projectin(
#             protime=request.form.get('cardTime'),
#             protitle=request.form.get('cardTitle'),
#             prosortcut=request.form.get('cardText'),
#             aboutinfoimg=filename
#         )
#         db.session.add(proinfo)
#         db.session.commit()
#         return redirect('/admin')
    
#     return render_template('admin/adminpanel.html')




if __name__ == '__main__':
    app.run(debug=True)




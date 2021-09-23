from re import A
from flask import Flask,redirect,render_template,request
from app import *






# -------------------Main Website----------------------
@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        contact=Contactin(
            fulname=request.form.get('fulname'),
            email=request.form.get('email'),
            message=request.form.get('massege')
        )
        
        db.session.add(contact)
        db.session.commit()
        return redirect('/')

# ---------------Home Iformasion ---------------------
    
    homeinfoall=Homein.query.all()
    hinfolen=len(homeinfoall)-1
    homeinfo=homeinfoall[hinfolen]

# ---------------About Iformasion ---------------------
    
    aboutinfoall=Aboutin.query.all()
    ainfolen=len(aboutinfoall)-1
    aboutinfo=aboutinfoall[ainfolen]


# ----------------MyProject Iformasion -----------------
    
    proje = Projectin.query.all()
    c=len(proje)-1
    leng=c-3
    prostatic=[proje[c],proje[c-1],proje[c-2],proje[c-3]]
    proje =proje[::-1]
    shadowbox=[]
    a=0;
    for infora in proje:
        a+=1
        if a>4 :
            shadowbox.append(infora)
    
    return render_template('maxwill.html',projec=shadowbox,homeinfo=homeinfo,prostatic=prostatic,aboutinfo=aboutinfo)




# ----------------------Project Website-----------------
@app.route('/project')
def project():
    return render_template('will-project.html')



# ----------------Admin Panel Main Iformation----------------------

@app.route('/admin',methods=['GET','POST'])
def adminmain():
    contact=Contactin.query.all()
    return render_template('admin/adminmain.html',contact=contact)


# ----------------Admin Panel Home Iformation----------------------
@app.route('/adminhome',methods=['GET','POST'])
def adminhome():
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
        return redirect('/adminhome')
    
    return render_template('admin/adminpanelhome.html')


# ---------------------Admin Panel Project Iformaton---------------
@app.route('/adminpro',methods=['GET','POST'])
def adminpro():
    if request.method=='POST':
        file = request.files['pfile']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        proinfo=Projectin(
            protime=request.form.get('cardTime'),
            protitle=request.form.get('cardTitle'),
            prosortcut=request.form.get('cardText'),
            proimg=filename
        )
        db.session.add(proinfo)
        db.session.commit()
        return redirect('/adminpro')
    
    return render_template('admin/adminpanelpro.html')

# ---------------------Admin Panel About Iformaton---------------

@app.route('/adminabout',methods=['GET','POST'])
def adminabout():
    if request.method=='POST':
        file = request.files['afile']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        aboutinfo=Aboutin(
            aboutinfo1=request.form.get('info1'),
            aboutinfo2=request.form.get('info2'),
            disgen1=request.form.get('disgen1'),
            disgen1interest=request.form.get('disgen1interest'),
            disgen2=request.form.get('disgen2'),
            disgen2interest=request.form.get('disgen2interest'),
            disgen3=request.form.get('disgen3'),
            disgen3interest=request.form.get('disgen3interest'),
            disgen4=request.form.get('disgen4'),
            disgen4interest=request.form.get('disgen4interest'),
            disgen5=request.form.get('disgen5'),
            disgen5interest=request.form.get('disgen5interest'),
            aboutinfoimg=filename
        )
        db.session.add(aboutinfo)
        db.session.commit()
        return redirect('/adminabout')
    
    return render_template('admin/admipanelabout.html')



# ----------------------Debug Mod ------------------------

if __name__ == '__main__':
    app.run(debug=True)




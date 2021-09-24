from flask import Flask,redirect,render_template,request,url_for
from werkzeug.utils import secure_filename
from . models import Homein,Aboutin,Projectin,Contactin
from postd import app,db,os






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






# -------------------------Project Website-------------------------

@app.route('/project')
def project():
    return render_template('will-project.html')







# ----------------Admin Panel Login Iformation----------------------

@app.route('/admin',methods=['GET','POST'])
def login():
    return render_template('admin/login.html')







# ----------------Admin Panel Main Iformation----------------------

@app.route('/admin/main',methods=['GET','POST'])
def adminmain():
    contact=Contactin.query.all()
    contact=contact[::-1]
    home=Homein.query.all()
    home=home[::-1]
    project=Projectin.query.all()
    project=project[::-1]
    about=Aboutin.query.all()
    about=about[::-1]
    return render_template('admin/adminmain.html',contact=contact,home=home,about=about,project=project)

# ---------------------Admin Panel Contact Delete-------------------
@app.route('/admin/Contact-delete/<int:id>', methods=['GET','POST'])
def concactdelete(id):
    contact = Contactin.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('adminmain'))




# ----------------Admin Panel Home Iformation----------------------
@app.route('/admin/home',methods=['GET','POST'])
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
        return redirect(url_for('adminmain'))
    
    return render_template('admin/adminpanelhome.html')

# ----------------Admin Panel Home Delete----------------------------
@app.route('/admin/home-delete/<int:id>', methods=['GET','POST'])
def homedelete(id):
    home = Homein.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('adminmain'))


# ---------------------Admin Panel Project Iformaton----------------
@app.route('/admin/pro',methods=['GET','POST'])
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
        return redirect(adminhome)
    
    return render_template('admin/adminpanelpro.html')



# ---------------------Admin Panel Project Delete-------------------
@app.route('/admin/Project-delete/<int:id>', methods=['GET','POST'])
def projectdelete(id):
    proje = Projectin.query.get_or_404(id)
    db.session.delete(proje)
    db.session.commit()
    return redirect(url_for('adminmain'))





# ---------------------Admin Panel About Iformaton---------------

@app.route('/admin/about',methods=['GET','POST'])
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
        return redirect(url_for('adminmain'))
    
    return render_template('admin/admipanelabout.html')


# ----------------Admin Panel About Delete----------------------------
@app.route('/admin/about-delete/<int:id>', methods=['GET','POST'])
def aboutdelete(id):
    home = Aboutin.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('adminmain'))



# -----------------------Admin Panel Home  Edit----------------------
@app.route('/admin/home/edit/<int:id>', methods=['GET','POST'])
def edithome(id):
    home = Homein.query.get_or_404(id)
    if request.method == 'POST':
       file = request.files.get('file')
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       home.info = request.form.get('title')
       home.infoimg = filename
       db.session.commit()
       return redirect(url_for("adminmain"))
    return render_template('admin/edithome.html', home=home)

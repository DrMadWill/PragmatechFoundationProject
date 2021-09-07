
class User:
    def __init__(self,_ad,_soyad,_email,_tel):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.tel=_tel
    def showUserData(self):
        print(f'{self.ad} | {self.soyad} | {self.email} | {self.tel}')

users=[]
def addUser():
    while True:
        ad=input('Ad : ')
        soyad=input('Soyad : ')
        email=input('Email : ')
        tel=input('Telefon : ')
        user=User(ad,soyad,email,tel)
        users.append(user)
        emr=input('Yeni telebe etmek isteyirsiniz mi? (Y/N) :')
        if emr=='N':
            break

addUser()
def showAllUsers():
    for user in users:
        user.showUserData()
showAllUsers()


class user{
    constructor(_id,_ad,_Soyad){
        this.id =_id,
        this.ad = _ad,
        this.soyad = _Soyad

    }
}

let user1 = new user(1,'Nofel','Salahov');
let user2 = new user(2,'Ramin','Semedov');
let user3 = new user(3,'Nijat','Bagirov');
let user4 = new user(4,'Ferid','Priyev');
let user5 = new user(5,'Elnar','Memmedov')

console.log(user1.ad)// innerHtml burada
let users;
users = [user1,user2,user3,user4,user5]



let istead = window.prompt('Istenen ad')

console.log(istead)

for (let i=0 ; i<=users.length;i++){
    let a
    a= users[i];
    
    if (istead === a.ad){

        let cardtitle = document.querySelector('.card-title')
    cardtitle.innerHTML=`Ad:${a.ad} | Soyad:${a.soyad}    | ID:${a.id} `

    }
    

}


let cardtext = document.querySelector('.card-text')
cardtext.innerHTML='Learn,Learn,Learn infertility--(DR-MadWill)'
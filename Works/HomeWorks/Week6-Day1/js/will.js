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




let istead = window.prompt('Istenen ad')

console.log(istead)

if (istead === user1.ad){

    let cardtitle = document.querySelector('.card-title')
cardtitle.innerHTML=`Ad:${user1.ad} | Soyad:${user1.soyad}    | ID:${user1.id} `

} else if (istead === user2.ad){

    let cardtitle = document.querySelector('.card-title')
cardtitle.innerHTML=`Ad:${user2.ad} |  Soyad:${user2.soyad}   |  ID:${user2.id} `
    
}else if (istead === user3.ad){

    let cardtitle = document.querySelector('.card-title')
cardtitle.innerHTML=`Ad:${user3.ad} | Soyad:${user3.soyad} |ID:${user3.id} `

}else if (istead === user4.ad){
    let cardtitle = document.querySelector('.card-title')
cardtitle.innerHTML=`Ad:${user4.ad} | Soyad:${user4.soyad} |ID:${user4.id} `
}else if (istead === user5.ad){
    let cardtitle = document.querySelector('.card-title')
cardtitle.innerHTML=`Ad:${user5.ad} | Soyad:${user5.soyad} |ID:${user5.id} `
}


// let cardtitle = document.querySelector('.card-title')
// cardtitle.innerHTML='Nofel' 

let cardtext = document.querySelector('.card-text')
cardtext.innerHTML='Learn,Learn,Learn infertility--(DR-MadWill)'
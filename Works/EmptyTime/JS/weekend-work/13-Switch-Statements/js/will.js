// Switch Statements



let category = 'manga';

switch(category){

    case 'telefon':
       console.log('telefon kategorisi');
    break;

    case 'manga':
       console.log('you are otaku');
    break;   

    default:
       console.log('yanlış kategori');
}


let  day ;


switch(new Date().getDay()){
    case 0:
        day = ('bazar');
    break;

    case 1:
        day = ('1-ci');
    break;

    case 2:
        day = ('II');
    break;

    case 3:
        day = ('III');
    break;

    case 4:
        day = ('IV');
    break;

    case 5:
        day = ('V');
    break;

    case 6:
        day = ('VI');
    break;

}

console.log(`bu gun heftenin ${day}`)

let  dayhaf ;


switch(new Date().getDay()){
    case 0:
    case 6:
        dayhaf = ('Hefte sonu');
    break;

    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        dayhaf = ('hefte ici');
    break;

    


}

console.log(`bu gun ${dayhaf}`)

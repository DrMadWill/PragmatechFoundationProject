// Operatorlar

let wil;
const a = 20;
const b = 10;
const c= 0;
const e= 10;
let  d=5;

// Aritmetik operator

    wil=a+b;
    console.log(wil);
    console.log(typeof wil);

    wil=a-b;
    console.log(wil);
    console.log(typeof wil);

    wil=a*b;
    console.log(wil);
    console.log(typeof wil);

    wil=a/b;
    console.log(wil);
    console.log(typeof wil);

    wil = a/c
    console.log(wil);
    console.log(typeof wil);

    wil = a%b
    console.log(wil);
    console.log(typeof wil);    //% mod nedir


    wil = d++;
    console.log(wil,'d++');
    console.log(d,'d++');
    console.log(typeof wil);

    wil = ++d;
    console.log(wil,'++d');
    console.log(d,'++d');
    console.log(typeof wil);

    wil = d--;
    console.log(wil,'d--');
    console.log(d,'d--');
    console.log(typeof wil);

    wil = --d;
    console.log(wil,'--d');
    console.log(d,'--d');
    console.log(typeof wil);



// Atama opertor

    wil = a;
    wil+=a ; //metiq wil=wil+a;
    console.log(wil);
    console.log(typeof wil);

    wil = a;
    wil-=a ; //metiq wil=wil-a;
    console.log(wil);
    console.log(typeof wil);

    wil = a;
    wil*=a ; //metiq wil=wil*a;
    console.log(wil);
    console.log(typeof wil);

    wil = a;
    wil/=a ; //metiq wil=wil/a;
    console.log(wil);
    console.log(typeof wil);

//Karsilasitma opertor

    wil = a == b;
    console.log(wil);
    console.log(typeof wil);


    wil = b == e;// deger kontrolu
    console.log(wil);
    console.log(typeof wil);


    wil = b === e;// deger kontrolu & data type
    console.log(wil);
    console.log(typeof wil);

    wil = a == '20';
    console.log(wil);
    console.log(typeof wil);

    wil = a === '20';
    console.log(wil);
    console.log(typeof wil);


    wil = a != b;//feqlidirmi
    console.log(wil);
    console.log(typeof wil);


    wil = a>b;
    console.log(wil);
    console.log(typeof wil);

    wil = a<b;
    console.log(wil);
    console.log(typeof wil);

    wil = a >= b;
    console.log(wil);
    console.log(typeof wil);

    wil = 5 >= '5';
    console.log(wil);
    console.log(typeof wil);

    wil = 5 <= '4';
    console.log(wil);
    console.log(typeof wil);

// Matiksal opertor

    // && (and) ikisde dogrudrmu ve ya yanlisdirmi (coklu soru)

    wil=(a>b) && (a>c)
    console.log(wil);
    console.log(typeof wil);


    wil=(a<b) && (a<c)//qalan veziyyetlerde false
    console.log(wil);
    console.log(typeof wil);

    // || (or) tek biri dogrudursa hepsi dogru

    wil=(a>b) || (a>c)
    console.log(wil);
    console.log(typeof wil);

    wil=(a>b) || (a<c)
    console.log(wil);
    console.log(typeof wil);

    wil=(a<b) || (a>c)
    console.log(wil);
    console.log(typeof wil);


    // ! (Not) butun deyerler aksidir

    wil=!(a>b)
    console.log(wil);
    console.log(typeof wil);




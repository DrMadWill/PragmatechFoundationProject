// ** Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    // ** Müşteri adı
    // ** Müşteri soyadı
    // ** Müşteri tc kimlik
    // ** Müşteri sipariş toplamı
    // ** Müşteri cinsiyet
    // ** Müşteri adres bilgisi
    // ** Müşteri hobiler

    let card = {
        Müşteriadı:'Wil',
        Müşterisoyadı:'Mad',
        Müşteritckimlik:12345,
        Müşterisipariştoplamı:12,
        // true kisi false qadin
        Müştericinsiyet:true,
        Müşteriadresbilgisi:adres={
            city:'Dream',
            discrict:'floor 7',
            body:'you sleep'
        },
        Müşterihobiler:['kod yazmaq','Mad Problem Solving','Opinon create']
    }

    console.log(card);


    class restoran  {
        constructor(_Müşteriadı,_Müşterisoyadı,_Müşteritckimlik,_Müşterisipariştoplamı,_Müştericinsiyet,_Müşteriadresbilgisi,_Müşterihobiler){

        this.Müşteriadı = _Müşteriadı,
        this.Müşterisoyadı = _Müşterisoyadı,
        this.Müşteritckimlik = _Müşteritckimlik,
        this.Müşterisipariştoplamı = _Müşterisipariştoplamı,
        // true kisi false qadin
        this.Müştericinsiyet = _Müştericinsiyet,
        this.Müşteriadresbilgisi = _Müşteriadresbilgisi,
        this.Müşterihobiler = _Müşterihobiler
        }
        
    }
    
    let mert = new restoran('mert','yildiz',12234,5,true,'koceli','jump');
    console.log(mert);


// ** Aşağıdaki siparişlerin toplamını hesaplayınız.

    let order1=Number('100');
    let order2=Number('150');
    
    console.log(order1+order2)


// ** Aşağıdaki siparişlerin toplamını hesaplayınız.

    var order3=Number('100.2');
    var order4=Number('150.5');
    order3=parseFloat(order3);
    order4=parseFloat(order4);

    console.log( order3+order4,'ondaliq');


// ** Aşağıdaki siparişlerin toplamını tam sayı olarak hesaplayınız.

    var order5=parseInt('100.2');
    var order6=parseInt('150.7');
    order5=parseInt(order5);
    order6=parseInt(order6);

    console.log( order5+order6,'yuvarlaq');

// ** Aşağıda verilen doğum yılına göre yaş hesaplayınız.

const yearOfBirth = 1986;

let c = 2021 - yearOfBirth;

console.log(c,'tebrikler')



// ** Aşağıdaki string ifadenin karakter sayısını bulunuz.

    let course = 'Modern Javascript Kursu';
    console.log(course.length,'karakter sayısı');

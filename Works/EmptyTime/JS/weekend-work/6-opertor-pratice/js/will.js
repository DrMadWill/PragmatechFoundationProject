

// ** Aşağıdaki siparişlerin toplamını hesaplayınız.
// Demo : Operators

// 1 - Can ve Ada 'nın boy ve kg bilgilerini alın.

    let indexAda;
    let indexCan

    const kgAda=65;
    const kgCan=78;

    const heightAda=1.70;
    const heightCan=1.85;


// 2 - Alınan bilgilere göre kilo indekslerini hesaplayınız.
//  ** Formül : Kişinin Kilosu / Boy Uzunluğunun Karesi
    indexAda = (kgAda)/(heightAda*heightAda)
    console.log(indexAda);
    indexCan = (kgCan)/(heightCan*heightCan);
    console.log(indexCan);


// 3 - Hesaplanan indeks bilgisine göre karşılaştırma yapınız.
    let kars= indexCan > indexAda;
    console.log(kars);
    kars = indexCan < indexAda
    console.log(kars);

// 4 - Aşağıdaki tabloya göre can ve ada hangi gruba giriyor.


// 0 - 18,4: Zayıf
// 18,5 - 24,9: Normal
// 25,0 - 29,9: Fazla Kilolu
// 30,0 - 34,9: Şişman (Obez)

    // Ada
    let positonAda = (indexAda > 0) && (indexAda < 18.4)
    console.log(positonAda,'Ada---Zayıf');

    positonAda = (indexAda > 18.4) && (indexAda < 24.9 )
    console.log(positonAda,'Normal');

    positonAda = (indexAda >25.0) && (indexAda < 29.9)
    console.log(positonAda,'Fazla Kilolu');

    positonAda = (indexAda >30.0) && (indexAda < 34.9)
    console.log(positonAda,'Şişman (Obez)');

    // Can
    let positonCan = (indexCan > 0) && (indexCan < 18.4)
    console.log(positonCan,'Can--Zayıf');

    positonCan = (indexCan > 18.4) && (indexCan < 24.9 )
    console.log(positonCan,'Normal');

    positonCan = (indexCan >25.0) && (indexCan < 29.9)
    console.log(positonCan,'Fazla Kilolu');

    positonCan = (indexCan >30.0) && (indexCan < 34.9)
    console.log(positonCan,'Şişman (Obez)');
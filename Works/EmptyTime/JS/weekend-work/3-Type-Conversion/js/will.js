// Tur dönüşmü

// string toplamam birlestirir


    let nm1 = '5'
    let nm2 = '72'

    console.log(nm1+nm2)
    console.log(typeof nm1)

// Donusum 

    // number
    let nm3 = Number('5')
    let nm4 = Number('72')

    let total= nm3+nm4;
    console.log(total);
    console.log(typeof total);
    
    // string
    let car

    car = String(20)

    console.log(car,'--car');
    console.log(typeof car);
    console.log(car.length);

    // boolean

    car=String(true )

    console.log(car,'--car');
    console.log(typeof car);
    console.log(car.length);

    // object

    car = String(new Date);

    console.log(car,'--car');
    console.log(typeof car);
    console.log(car.length)

    // array to string vergul de sayilir

    car = String([1,2,3,4]);

    console.log(car,'--car');
    console.log(typeof car);
    console.log(car.length);


    //string to number
    car = Number('80');
    console.log(car,'--string');
    console.log(typeof car);

    //boolen to number
    car = Number(false);
    console.log(car,'--boolen');
    console.log(typeof car);

    //null to number
    car = Number(null);
    console.log(car,'--null');
    console.log(typeof car);

    //cevrilemeceyk deyer to number
    car = Number('a');
    console.log(car,'--cevrilemeceyk deyer');
    console.log(typeof car);

    //array to number
    car = Number([1,2.3,4]);
    console.log(car,'--array');
    console.log(typeof car);

    //number method
    car = parseInt('10');
    console.log(car,'--number method');
    console.log(typeof car);


    //number tam ondaliq method
    car = parseFloat('10.5');
    console.log(car,'--number tam ondaliq method');
    console.log(typeof car);
    
    //number yuvarlaq method
    car = parseInt('10.5')
    console.log(car,'--yuvarlaq');
    console.log(typeof car);






let a;
let b = 25.1234567

a= b.toPrecision(6)
console.log(a)
console.log(typeof a)

a= b.toFixed(6)
console.log(a)
console.log(typeof a)

a=isNaN('10')
console.log(a)
console.log(typeof a)

a= isNaN('aa')
console.log(a)
console.log(typeof a)

a= Math.PI;
console.log(a)
console.log(typeof a)

a= Math.round(2.6)
console.log(a)
console.log(typeof a)

a=Math.random();// radom 0-1 aras;
console.log(a,'radom')
console.log(typeof a)

a=Math.floor(Math.random()*10)
console.log(a,'radom 1-10')
console.log(typeof a)

a= Math.round(25.9)// yuvarla
console.log(a)
console.log(typeof a)

a=Math.ceil(2.1)// yuxar yuvar
console.log(a)
console.log(typeof a)

a= Math.floor(2.7);// asaqiya yuvarla
console.log(a)
console.log(typeof a)

a= Math.sqrt(81)// kok al
console.log(a)
console.log(typeof a)

a= Math.pow(2,4)// 2 ustu 4
console.log(a)
console.log(typeof a)


a= Math.abs(-100)// hemse musbet
console.log(a)
console.log(typeof a)


a= Math.min(3,7,2,9)// en kicik deyer
console.log(a)
console.log(typeof a)

a= Math.max(6,7,5,3,0,9);// en boyuk deyer
console.log(a)
console.log(typeof a)
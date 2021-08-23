// document.getElementById("dr-box").style.top = "50%";
// document.getElementById("dr-box").style.left = "50%";
// document.getElementById("dr-box").style.transform = "translate(-50%,-50%)";


// let a = document.querySelector("#body");
// a= a.offsetWidth
// b= a.offsetHeight
// console.log(a)
// console.log(b)



let d=document.documentElement
let body = d.body
let bodygenis=window.innerWidth/2
let bodyhundur=window.innerHeight/2
console.log("body-genislik:",bodygenis)
console.log("body-hundurluk:",bodyhundur)

let div = document.getElementById('dr-box')
let divgenis=div.clientWidth/2
let divhundur=div.clientHeight/2
console.log("div-genislik:",divgenis)
console.log("div-hundurluk:",divhundur)

let elmtGenis = bodygenis-divgenis
let elmtHundur = bodyhundur - divhundur

console.log("verilmeli-genislik:",elmtGenis)
console.log("verilmeli-hundurluk:",elmtHundur)
// verilmeli hündürlük və genişlik marginlə versek olarmı
// body height niyə mənfi alıram 

let innerContainer=document.querySelector('.innerContainer');
let boxCount=document.querySelectorAll('.item').length
for(let i=0;i<boxCount;i++){
    document.querySelectorAll('.item')[i].innerHTML=i+1
}
innerContainer.style.width=`${boxCount*320}px`
pos=0;

function goNext(){
    innerContainer.style.left=`${pos}px`
    pos+=-320
}

function goPrev(){
    innerContainer.style.left=`${pos}px`
    pos+=320
}
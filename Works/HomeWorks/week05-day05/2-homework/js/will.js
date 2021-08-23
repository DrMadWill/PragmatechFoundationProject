let box=document.getElementsByClassName("dr-box");

// random fuciton


function mad(){
    let a=Math.random()*10
    a=Math.floor(a)
    console.log(a);
    box[a].addEventListener('click',function(){
        document.querySelector('.boxContainer').removeChild(this)
    })
}
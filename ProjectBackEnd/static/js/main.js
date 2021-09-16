let a,
b,
c;
a= true;
d=document.getElementById("lost"); 
c=document.getElementById('lost1');

let m
m=window.innerWidth
if (m<768){
    d.style.display='none'
    c.style.display='none'
}


function iconclick(){
    
    if (a===true){
        
        a=false;
        d.style.display='flex'
        c.style.display='flex'
        
    }else{
        a=true;
        d.style.display='none'
        c.style.display='none'
        

    }
}




function will(){
    let f

    f=window.innerWidth

    if (f>768){
        d.style.display='flex'
        c.style.display='flex'
    }else{
        d.style.display='none'
        c.style.display='none'
    }


}




const header=document.querySelector('header')
header.style.backgroundColor='transparent'
header.style.boxShadow='0 0 0 0 blue'

window.addEventListener('scroll',()=>{
    if (document.documentElement.scrollTop>=50){
        header.style.backgroundColor='#f1f1f1'
    }else{
        header.style.backgroundColor='transparent'
        header.style.boxShadow='0 0 0 0 blue'
        document.querySelectorAll('.pr-link')
    }
})

// while (2>1){
//     l=l.offsetTop
//     if (l==0){
//         let t
//         t=document.querySelector('header')

//     }
// }



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
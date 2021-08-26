let a,
b,
c;
a= true;
d=document.getElementById("lost"); 
c=document.getElementById('lost1');

function iconclick(){
    
    if (a===true){
        
        a=false;
        d.style.display='none'
        c.style.display='none'
        console.log(a);
    }else{
        a=true;
        d.style.display='inline-block'
        c.style.display='inline-block'
        console.log("twoe click")

    }
}
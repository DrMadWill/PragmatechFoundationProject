let a,
b,
c;
a= true;
d=document.getElementById("lost"); 
c=document.getElementById('lost1');

const header=document.querySelector('header')
header.style.backgroundColor='transparent'
header.style.boxShadow='0 0 0 0 blue'
const headlink = document.querySelectorAll('.header-link')


let m
m=window.innerWidth


if (m<768){
    d.style.display='none'
    c.style.display='none'
    header.style.backgroundColor='#f1f1f1'
    headlink[0].style.color="#000"
    for(i=1;i<=headlink.length;i++){
            headlink[i].style.color="rgba(63, 59, 59,0.83)"
    }
}

// ekran ölçüləri dəyişdikdə dispeyin flex olma hali 

function will(){
    let f

    f=window.innerWidth
    console.log('bu genislik deyerdi',f)

    if (f>768){
        d.style.display='flex'
        c.style.display='flex'

        header.style.backgroundColor='transparent'
        header.style.boxShadow='0 0 0 0 blue'
        
        for(i=0;i<=headlink.length;i++){
            headlink[i].style.color='white'
        }
        
    }else{
        d.style.display='none'
        c.style.display='none'
        header.style.backgroundColor='#f1f1f1'
        headlink[0].style.color="#000"
        for(i=1;i<=headlink.length;i++){
            headlink[i].style.color='rgba(63, 59, 59,0.83)'
        }
    }

    


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





window.addEventListener('scroll',()=>{
    if (document.documentElement.scrollTop<=50){
        header.style.backgroundColor='transparent'
        header.style.boxShadow='0 0 0 0 blue'
        
        for(i=0;i<=headlink.length;i++){
            headlink[i].style.color="#fff"
        }
    }else{
        
        header.style.backgroundColor='#f1f1f1'
        headlink[0].style.color="#000"
        for(i=1;i<=headlink.length;i++){
            headlink[i].style.color="rgba(63, 59, 59,0.83)"
            
        

        

        }
    }
})








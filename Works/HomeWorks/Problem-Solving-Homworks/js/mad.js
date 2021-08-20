function mad(){
    let dr=document.getElementsByClassName('dr-box')
    

    let a=0;
    let btn = document.getElementById("btn");

    btn.onclick = function bar(){
        a++;
        console.log(a);
        return a;
    }
    dr[a].style.visibility = "visible";

}


/*
for (i=0;i=a;i++){
   div ementinin təkrak funksiyasi  
}
*/ 


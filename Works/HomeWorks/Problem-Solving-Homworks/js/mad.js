function mad(){
    let dr=document.getElementsByClassName('dr-box')
    

    let a=0;
    let btn = document.getElementById("btn");

    btn.onclick = function tar(){
        a++;
        console.log(a);
        return a;
    }
    dr[a].style.visibility = "visible";


}




/*
let a=5

for (i=0;i=a;i++){
   console.log(i);   
}
*/ 


// Loops

// For Loops

    for (let i=0;i<10;++i){
        if (i==7){
            console.log('sevilen--'+i)
            continue;// hemin dovur sonlandirir novre kecirir
        }
        
        if(i==6){
            console.log("sevilmeyen------",i)
            break;// tum donguler sonlanir
        }
        console.log(i)
    
    }

//   while Loops

    let a = 5;
    while(a<10){
        console.log("while coooool loops----",a)
        a++
    }


//  do whihle 


    let c = 15; 
    do {
        console.log("do loops haha------",c)
        c++
    }while(c<20)


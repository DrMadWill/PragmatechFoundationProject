// Data Object 
    

    let d = new Date();
    let adgun = new Date(2010,1,8)

    let c = d.getFullYear() - adgun.getFullYear();
    console.log(c,'adgunu')
    
    // Get Method info want
    console.log(d.getDate());// gun
    console.log(d.getDay());// hefte gun
    console.log(d.getFullYear());//il
    console.log (d.getHours())// saat
    console.log(d.getMonth())//ay
    console.log(d.getSeconds())//saniyye

    console.log(d,'--');
    console.log(typeof d);

    // Set Method info order
    
    d.setDate(12)//gun
    d.setFullYear(2015)//il
    d.setHours(21)//saat


    console.log(d.getDate(),"deyis  gun");// gun
    console.log(d.getDay(),"hefte gun");// 
    console.log(d.getFullYear(),"il");//il
    console.log (d.getHours(),"saat")// saat
    console.log(d.getMonth(),"ay")//ay
    console.log(d.getSeconds(),"saniyyen")//saniyye






   


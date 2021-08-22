// ** Şimdiki tarihin gün ay ve yıl bilgisini yazdırınız.
    let e = new Date() 
    console.log(e)
// ** Tarih ve saat bilgisini içeren bir Date objesi oluşturunuz.
    let b = new Date(2010,1,1)
    console.log(b)
// 1/1/1990 tarihinden bir gün öncesini gösteriniz. 
    let c = new Date('1/1/1990')
    let r = c.getDate()
    c.setDate(r-1)
    console.log(c)
// iki tarih arasındaki geçen zamanı bulunuz.
    let geczam = b-c;
    let saniye = geczam/1000
    let dakika = saniye/60
    let saat = dakika / 60
    let gun = saat / 24
    let yil = gun /365
    console.log(geczam)
    console.log(saniye)
    console.log(dakika)
    console.log(saat)
    console.log(gun)
    console.log(yil)


    

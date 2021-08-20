# HTML DOM Reference three method research in object

 1. **  The HTML DOM Attr Object**
 2. ** Window Object **
 3. ** The Document Object **

## The HTML DOM Attr Object
 1. #### document.getElementById("") Method 
  1. Return funcition.Dəyər verilmədikdə > null qayatarırı;
  2. HTML təqlərindən uyğun id-li _elmet_-i çağırmaq üçün istifadə olunur;
  3. ```<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
            <style>
            #will{
                height: 60px;
                width: 60px;
                background-color: indigo;
                margin: 0 60px;
            }
            </style>
        </head>
        <body class="d-flex justify-content-center align-items-center vh-100"  >
            
            <button onclick="mad()" class="btn btn-primary">Click me</button>

            <div id="will">
                
            </div>

            <script>
                function mad(){
                    document.getElementById("will").style.backgroundColor = "yellowgreen"
                }
            </script>


        </body>
        </html>    
     ```
 2. #### document.getElementsByClassName() Method 
    1. Return funcition.Dəyər object-dir.
    2. HTML təqlərindən uyğun class-lı _elmetləri_ çağırmaq üçün istifadə olunur.
    3. ```
            <button onclick="mad()" class="btn btn-primary">Click me</button>

            <div class="will">
                
            </div>

            <div class="will">
                
            </div>
            <div class="will">
                
            </div>
            <script>
                function mad(){
                    let dr=document.getElementsByClassName('will')
                    dr[0].style.backgroundColor = "yellowgreen";
                    dr[1].style.backgroundColor = "yellowgreen";
                    dr[2].style.backgroundColor = "yellowgreen";

                }
            </script>
        ```
 3. ####  getElementsByTagName() Method
    1. Return funcition.Dəyər object-dir.
    2. HTML təqlərindən uyğun təqlərə müraciyyət etmək üçün isitfadə olnur.
    3. ```
            <div style="background-color: indigo;
                        padding: 60px;
                        margin: 60px;">Coffee</div>
            <div style="background-color: indigo;
                            padding: 60px;
                            margin: 60px;">Coffee</div>
            <div style="background-color: indigo;
                            padding: 60px;
                            margin: 60px;">Coffee</div>




            <button onclick="mad()">Try it</button>


            <script>
            function mad() {
            let dr = document.getElementsByTagName("DIV");
            dr[1].style.backgroundColor = "yellowgreen";
            }
            </script>

        ```
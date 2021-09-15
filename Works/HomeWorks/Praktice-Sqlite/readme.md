# My SQLite Cod

```
    C:\Users\nofel\OneDrive\Desktop\db>sqlite3 maxwill.db
    SQLite version 3.36.0 2021-06-18 18:36:39
    Enter ".help" for usage hints.
    sqlite> .tables
    sqlite> .tables
    Aqro     COMPANY  Prodact
    sqlite> .table Aqro
    Aqro
    sqlite> .schema Aqro
    CREATE TABLE Aqro(
            ID PRIMARY KEY UNIQUE  NOT NULL,
            Name TEXT NOT NULL,
            Asit TEXT NOT NULL,
            Aqrocompany TEXT NOT NULL,
            Money INT NOT NULL);
    sqlite> .shema COMPANY
    Error: unknown command or invalid arguments:  "shema". Enter ".help" for help
    sqlite> .schema COMPANY
    CREATE TABLE COMPANY(
    ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
    AGE            INT     NOT NULL,
    ADDRESS        CHAR(50),
    SALARY         REAL
    );
    sqlite> DROP TABLE COMPANY;
    sqlite> .tables
    Aqro     Prodact
    sqlite> CREATE TABLE COMPANY(
    ...>    ID INT PRIMARY KEY     NOT NULL,
    ...>    NAME           TEXT    NOT NULL,
    ...>    AGE            INT     NOT NULL,
    ...>    ADDRESS        CHAR(50),
    ...>    SALARY         REAL
    ...> );
    sqlite> .tables
    Aqro     COMPANY  Prodact
    sqlite> .schema Aqro
    CREATE TABLE Aqro(
            ID PRIMARY KEY UNIQUE  NOT NULL,
            Name TEXT NOT NULL,
            Asit TEXT NOT NULL,
            Aqrocompany TEXT NOT NULL,
            Money INT NOT NULL);
    sqlite> INSERT INTO Aqro (ID,Name,Asit,Aqrocompany,Money) VALUES (1,'Fosetrin','Tricpella','Tarkim','25');
    sqlite> INSERT INTO Aqro (ID,Name,Asit,Aqrocompany,Money) VALUES (2,'Avrimec','Abamectin','Koruma',10)
    ...> ;
    Error: database is locked
    sqlite> INSERT INTO Aqro (ID,Name,Asit,Aqrocompany,Money) VALUES (2,'Avrimec','Abamectin','Koruma',10);
    Error: database is locked
    sqlite> INSERT INTO Aqro (ID,Name,Asit,Aqrocompany,Money) VALUES (2,'Avrimec','Abamectin','Koruma',10);
    sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
    ...> VALUES (1, 'Paul', 32, 'California', 20000.00 );
    sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
    ...> VALUES (2, 'Allen', 25, 'Texas', 15000.00 );
    sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
    ...> VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );
    sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
    ...> VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
    sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
    ...> VALUES (5, 'David', 27, 'Texas', 85000.00 );
    sqlite> INSERT INTO Aqro VALUES (3,'Siperkor','Supermetrin','Koruma',12);
    sqlite> INSERT INTO Aqro VALUES (4,'Kimetrin','Supermetrin','Tarkim',12);
    sqlite> INSERT INTO Aqro VALUES (5,'Ultimatium','Supermetrin','Dva',22);
    sqlite> select * from aqro
    ...> ;
    1|Fosetrin|Tricpella|Tarkim|25
    2|Avrimec|Abamectin|Koruma|10
    3|Siperkor|Supermetrin|Koruma|12
    4|Kimetrin|Supermetrin|Tarkim|12
    5|Ultimatium|Supermetrin|Dva|22
    sqlite> select Name from aqro;
    Fosetrin
    Avrimec
    Siperkor
    Kimetrin
    Ultimatium
    sqlite> select name from  company
    ...> ;
    Paul
    Allen
    Teddy
    Mark
    David
    sqlite> select * from company
    ...> ;
    1|Paul|32|California|20000.0
    2|Allen|25|Texas|15000.0
    3|Teddy|23|Norway|20000.0
    4|Mark|25|Rich-Mond |65000.0
    5|David|27|Texas|85000.0
    sqlite> select age,id from company
    ...> ;
    32|1
    25|2
    23|3
    25|4
    27|5
    sqlite> .tables
    Aqro     COMPANY  Prodact
    sqlite>
    sqlite> .schame prodact
    Error: unknown command or invalid arguments:  "schame". Enter ".help" for help
    sqlite> .schema prodact
    CREATE TABLE Prodact(
            ID PRIMARY KEY    NOT NULL,
            Name TEXT NOT NULL,
            Price INT NOT NULL,
            Img_url TEXT );
    sqlite> insert into prodact values(1,Samsung s7,2000);
    Error: near "s7": syntax error
    sqlite> insert into prodact values(1,Samsungs7,2000);
    Error: no such column: Samsungs7
    sqlite> insert into prodact values(1,'Samsungs7',2000);
    Error: table prodact has 4 columns but 3 values were supplied
    sqlite> insert into prodact values(1,'Samsungs7',2000,'');
    sqlite> insert into prodact values (2,'Ipone 7',2000,'');
    sqlite> insert into prodact values(3,'Redme 7a',1000,'' );
    sqlite> select * from prodact
    ...> ;
    1|Samsungs7|2000|
    2|Ipone 7|2000|
    3|Redme 7a|1000|
    sqlite> .width 10,20,10
    sqlite> select * from prodact
    ...> ;
    1|Samsungs7|2000|
    2|Ipone 7|2000|
    3|Redme 7a|1000|
    sqlite> .width 10, 20, 10
    sqlite> select * from  company;
    1|Paul|32|California|20000.0
    2|Allen|25|Texas|15000.0
    3|Teddy|23|Norway|20000.0
    4|Mark|25|Rich-Mond |65000.0
    5|David|27|Texas|85000.0
    sqlite> select name from company where age>27;
    Paul
    sqlite>

```
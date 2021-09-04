#String 
a='Kralla, kralin oturduğu at arasindakı fərq nədir ? ' #str dəyişən

print(type(a))
print(a)


b="""Sualin cavabi birin at olmasi birin insan olmasi kimi az düşünülmüş cavab deyil 
At və kral eyni bacariğa,eyni bədən quruluşuna sahib olsayidi  belə 
Yenə biri döyüşü idarə edən kral biri isə kralı daşıyan at olardı.Kralla at arasindakı fərq nədir"""

print(b)

print(a[0])


# Number

print(type(2)) #int
print(type(2.5))#float
print(type(10/5))#float
print(type(2+3j))#complex

#Sequence 

d=[1,2,7,'Mad',"Will"] #list
print(type(d))

e=('Instink',1,3+4)
print(type(e))
print(e[0:3])
#e[1]=2;#error assignment


# Mapping

y={
    'will':'MadWill', 
    'road':'Domation'
}
print(y)
print(type(y))
y['will']='Dr.MadWill'
print(y['will'])
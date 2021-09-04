# Data type conversion

a=input()
print(type(a))
a=int(a)#int type conversion
print(type(a))



s = 'Dr.MadWill'
c = tuple(s)#tuple type conversion
print (c)

d='Gələcəkdə əldə etmək istədiyi bir şey olmayan bir varlıq bu dəyişkən gercəklikdə dəyişkənliyin onun daxilindəki stabiliyi yuyub aparmasina məhkumdur '

d=list(d)#list type conversion 
print(d)






v=['Dəyişkənlikdə','əlində','sabit','olmayan','deklemde','sabit','olan','bizlər','tərfindən','qorxulmağa','məhkumdur']

l=tuple(v)#tuple type conversion
print(l)

n=True
n=int(n)#int type conversion 
print(n)



m=15
j=bool(m)
print(j)

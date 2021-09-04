strs='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# str daxilində neçə sait və neçə samit olduğunu ekrana çap edin
# str daxilində son iki sözü silən metod yazın
# str ni vergülə görə ayırıb iki string halına gətirin
# stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın


strs=list(strs)
for a in strs:
    if a==' ':
        strs.remove(' ')

strs.remove(',')

herfsayi=0
for a in strs:
    herfsayi+=1
print("herfsayi - ",herfsayi)


saitsayi=0
saitlər=['a','i','ı','o','u','e','ə','ö','ü']

for sait in saitlər:
    for star in strs:
        if sait==star:
            saitsayi+=1

samitsayi=herfsayi-saitsayi

print('Saitsayi - ',saitsayi)
print('Samit sayi - ',samitsayi)

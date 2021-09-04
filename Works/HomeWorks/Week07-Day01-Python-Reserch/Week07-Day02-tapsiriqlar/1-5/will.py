strs='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# str daxilində son iki sözü silən metod yazın
# str ni vergülə görə ayırıb iki string halına gətirin
# stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın


d=strs.split(' ')

c=len(d)-1
e=c-1;

d.remove(d[c])
d.remove(d[e])

star=""
for a in d:
    star+=f" {a}"

print(star)

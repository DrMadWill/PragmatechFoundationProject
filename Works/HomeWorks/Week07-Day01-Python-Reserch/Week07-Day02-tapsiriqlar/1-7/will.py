strs='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın

d=strs.split(',')

a=d[0]+d[1]
print(a)

sozler=a.split(' ')
istene=input()
def stringSearch(h):
    global sozler
    for soz in sozler:
        if soz == h:
            print("var")
            

stringSearch(istene)

if stringSearch(istene) == True:
    pass
else:
    print('yoxdur')

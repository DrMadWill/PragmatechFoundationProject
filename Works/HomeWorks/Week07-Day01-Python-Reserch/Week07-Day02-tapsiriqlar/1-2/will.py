strs='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# str daxilində neçə hərf olduğunu ekrana yazdırın

strs=list(strs)

for a in strs:
    if a==' ':
        strs.remove(' ')


strs.remove(',')
m=0
for a in strs:
    m+=1
print(m)
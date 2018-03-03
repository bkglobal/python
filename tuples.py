genders = ('male','female','others')
a,b,c = genders
print(a,b,c)

for gender in genders:
    print(gender)
index= genders.index('others')
print(index)
print('others' in genders)
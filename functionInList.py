def make_great(magicians):
    for magician in range(0,len(magicians)):
        magicians[magician] = 'great ' + magicians[magician]
    return magicians

magicians = ['ronald','vick','john','doe']
print(make_great(magicians))

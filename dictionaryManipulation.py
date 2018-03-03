alien_o = {'color':'green','points':'5'}
print(alien_o['color'])
print(alien_o['points'])

alien_o['position'] = 'left'
print(alien_o)

alien2 = alien_o


print(alien2)
del alien2

for key, value in alien_o.items():
    print('key: ',key,' Value : ',value)

print(set(alien_o.values()))

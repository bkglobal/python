bicycle = ['trek','connadola','merrecy']
temp = [2,3,4,5,6,7,8,9]
print(temp[0])

for tmp in range(1,len(temp)):
    print(temp[tmp])

temp.append(20)
print('After Append')
for tmp in temp:
    print(tmp)


temp.insert(2,50)
print('After Insert')
for tmp in temp:
    print(tmp)

x = temp.pop(2)
print('After pop at index 2 the poped value is : ',x,' and list values are: ')
for tmp in temp:
    print(tmp)

unsorted_list = [5,6,8,2,8,1,3,3,2,4]
print("Unsorted list: ",unsorted_list)
sorted_list = sorted(unsorted_list)
print("Sorted List: ", sorted_list)
reversed_sroted_list = sorted(unsorted_list,reverse=True)
print("Reversed Sorted List: ",reversed_sroted_list)
z=1
b='kok'
print(f'sdgsag:{z},sfasd:{b}')

for i in range(1,6):

    a=(2*i-1)*'*'
    b=(5-i)*' '
    print(b+a)

list_one=[]
for j in range(1,6):
    a=(5-j)*' '+   (2*j-1)*'*'
    list_one.append(a)
print('\n'.join(list_one))



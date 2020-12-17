#Andrea Magro IT-20
#14.12.20
#iseseisevtöö

#kolmnurgad ülesanne 12
def uzor (arr):
    for i in arr:
        print('*'*i)

    print('    ')

uzor([1,3,5,3,1])
uzor([5,4,3,2,1])
uzor([1,2,3,4,5])
uzor([5,4,3,2,1,2,3,4])

input()
#arvud 1-66 reana ülesnne 9
def number_summ (n):
    c = 1
    str = ''
    while c <= n:
        str += f'{c}'
        c += 1

    print(str)


number_summ(66)

input()
#ma armastan javat ülesanne 8
def reverse (str):
    arr = str.split()
    arr.reverse()
    string = ''
    for i in arr:
        string += f'{i} '

    return string.strip()


string = 'Ma armastan Javat'

print(reverse(string))

input()
#ülesanne 5





input()
#eesti lipp ülesanne 4
def printlipp (c, n):
    print(c * n)
    print(c * n)
    print(c * n)

printlipp('¤',46)
printlipp('=',46)
printlipp('-',46)


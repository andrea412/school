#Andrea Magro IT-20
#15.01.21
#Ülesanded 1-10


#1.Korrutamise kontrollimine
#programm esitab korrutustehte
import random
n = 0
while n <= 10:
    a = random.randrange(0, 9)
    b = random.randrange(0, 9)
#ootab kasutajalt vastuse sisestamist
    print(f'{a} * {b} = ')
    i = input()
#väljastab, kas vastus oli õige või väär.
    if a * b != int(i):
        print('no')
#kontrollib vastuse õigsust
    else:
        print('ok')
    n += 1


#2.Vanused
#loon vanuste loend
ages = [1, 12, 34, 56, 32, 45, 64, 82, 12, 14]
#leiab numbrite suurim ja väikseim arv, kogusumma ja keskmine 
tot = 0
for i in ages: tot += i
result = tot / len(ages)
print(int(result))


#3.Positiivsed ja negatiivsed
#teen kaks loendit positiivsete ja negatiivsete arvude hoidmiseks
pos = []
neg = []
n = 0
#kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
while n < 5:
    i = input()
#nulli lisamisel ei tehta midagi
    if int(i) > 0:
        pos.append(i)
    else:
        neg.append(i)
    n += 1
#väljasta mõlemad loendit
print(f'Positive: {pos},  Negative: {neg}')


#4.List less than ten 
a = [1, 2, 3, 2, 4, 5, 10, 12, 15]
res = []
i = input()
for n in a:
    if n < int(i):
        res.append(n)
print(res)


#5.Shopping list
shopping_list = []
while True:
    item = input()
    if item == '':
        break
    shopping_list.append(item)
print(shopping_list)


#6.Eurokalkulaator, koostan programmi, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või vastupidi
ekk_rate = 15.6466
#kuvatakse veateade, kui kasutaja tegi valiku valesti
while True:
    print('to convert EUR --> EEK press 1 \n''to convert EEK --> EUR press 2''\n Press "Enter" to Quit')
    i = input()
#küsitakse valuuta kogust ja tehakse arvutused
    if i == str(1):
        print('write the amount to convert')
        n = input()
        result = int(n) * ekk_rate
        print(f'Your EEK amount: {round(result, 2)} \n')
        pass
    elif i == str(2):
        print('write the amount to convert')
        n = input()
        result = int(n) / ekk_rate
        print(f'Your EUR amount: {round(result, 2)} \n')
        pass
    elif i == '':
        break
    else:
        print('I don t understand you, maybe you have entered a wrong key\n')
        pass


#7.Täringud
import random
print(' Enter the amount of Eur you wanna play')
bank = int(input())

while True:
    print('make a Bet')
    print(f'Your Bank: {bank}')
    bet = int(input())
#kasutaja võistleb kahe täringuga arvuti vastukasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endal
    if bet > bank:
        print(f'too big bet, Your bank is {bank}, to add chips press add')
        add = input()
        if add == 'add':
            print('add chips amount')
            amount = int(input())
            bank += amount
            print(f'Your bank now {bank}')
    elif bet <= bank:
        players_first = random.randrange(1, 6)
        players_second = random.randrange(1, 6)
        Players_summa = players_second + players_first
        print(f'{players_first}, {players_second}, Your sum == {Players_summa}  bet was {bet}')

        PC_first = random.randrange(1, 6)
        PC_second = random.randrange(1, 6)
        PC_summa = PC_first + PC_second
        print(f'{PC_first}, {PC_second}, PC sum == {PC_summa}')

        if PC_summa > Players_summa:
            print('you lost')
            print(f'Your bank was  {bank} now is {bank - bet}')
            bank = bank - bet
        elif PC_summa < Players_summa:
            print('you win')
            print(f'Your bank was {bank} now is {bank + bet}')
            bank = bank + bet
        elif PC_summa == Players_summa:
            print('Repeat because of Draw')
    else:
        print(f'something went wrong your input: "{bet}" Try again')
        pass
    print('Press any key to quit or Enter to continue')
    key = input()
    if key != '':
        break


#8.Emaili kontroll
#programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll
email = 'andrea.magro@gmail.com'
point = email.find('.')
dog = email.find('@')
if point != -1 and dog != -1 and len(email) > 12:
    name = email[0:point]
    surname = email[point+1: dog]
    domain = email[dog:]
    print(f'Name:{name}, Surname:{surname}, Domain:{domain}')


#9.Kaugushüpe
import math
import numpy
i = 0
data = []
#kasutaja sisestab 3 kaugushüppe tulemust
while i < 3:
#programm leiab ning väljastab parima ja keskmise tulemuse
    print('write the jump distance')
    jump = float(input())
    data.append(jump)
    print('write one more')
    i += 1
print(f'Your best or three jumps is {max(data)}, your average jump distance is {numpy.mean(data)}')


#10.Salakeel
def encoded (sms):
    alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','a','b','c','d','e','f','g','h','i','j','k','l','m')
    alphabet2 =('N','O','P','Q','R','S','T','U','V','W','X','Y','Z','n','o','p','q','r','s','t','u','v','w','x','y','z')
    encoded = ''
    if sms in data:
        return data[sms]
#kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks
    for i in sms:
        if i not in alphabet and i not in alphabet2:
            encoded += i

        if i not in alphabet:
            for s in alphabet2:
                if i == s:
                    index = alphabet2.index(i)
                    encoded += alphabet[index]
#kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks
        elif i not in alphabet2:
            for c in alphabet:
                if i == c:
                    index = alphabet.index(i)
                    encoded += alphabet2[index]

    data.update({encoded: sms})
    return encoded, data


data = {}

while True:
    string = input()
    print(encoded(string))
    

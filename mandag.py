import random

'''
Oppgave 1
VELG RIKTIG OUTPUT
alternative 1 = 'none'
alternative 2 = 'invalid syntax'
alternative 3 = 'the cat on the roof'
'''
word = 'the cat on the roof'
print(word)
#koden sender alternativ 3

'''
Oppgave 2
VELG RIKTIG OUTPUT
alternative 1 = 'Eureka'
alternative 2 = 'IM- Åssiden vgs'
alterbative 3 = 'none'
'''
a =1
b =1
c =7
d =5

result = a + b + d
if result < c:
    print('Eureka')
else:
    print('IM- Åssiden vgs')
#koden sender IM- Åssiden vgs

'''
Oppgave 3 
Hvor mange ganger skal følgende loop kjøres?
VELG RIKTIG SVAR
 alternative 1 = 150
 alternative 2 = 50
 alternative 3 = 30
 alterbative 4 = uendelig mange ganger.
'''

r = 150
while r <= 200:
    print(r)
    r+=5
#alternativ 2

'''
oppgave 4
forklar linje for linje hva er det som skjer i funksjonen oddTall.
 VIKTIG!!!!! Forklar linjene først, før du tester den i editoren din.
'''

def oddeTall():
    num1 = random.randint(1,10) #tar tilfeldig tall mellom 1 og 10
    num2 = random.randint(2,9) #tar tilfeldig tall mellom 2 og 9
    if num1%num2 ==0: #om tallet er et oddetall
        result = num1/num2 #resultat er tilfeldig tall mellom 1 og 10 delt på tilfeldig tall mellom 2 og 9    
    
    return result #viser resultat variabelen i terminalen

oddeTall()

#får error local variable result referenced before assignment pga return metoden er ikke i if
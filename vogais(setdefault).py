import time

vogais = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
palavra = str (input('qual seu nome?? '))
enc = []
f = {}
print ('legal, {}. Belo nome. Deixe-me pensar nas vogais dele...'
       .format(palavra))

time.sleep(3)
print ('bom...')
for letter in palavra:
    if letter in enc:
        print ( letter + " já foi")
        f[letter] += 1
    else:
        time.sleep(2)
        if letter in vogais:
            f.setdefault(letter, 1)
            print (letter + " é vogal")
            enc.append(letter)
        elif letter == " ":
            print('isso é espaço né, po kkkk')
        else :
            print(letter + " é consoante")
            
time.sleep(5)
            
print (enc) 
time.sleep(1)
print ('essas foram as vogais que achei')
for k,v in sorted (f.items()):
    if f[k] == 1:
        print ('{} apareceu {} vez'.format (k,v))
    else:
        print ('{} apareceu {} vezes'.format (k,v))
time.sleep(2)
print ('foi legal jogar contigo')
time.sleep(2)
print ('até mais!!')
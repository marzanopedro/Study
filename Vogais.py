import time

vogais = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
palavra = str (input('qual seu nome?? '))
enc = []
f = {}
print ('legal, {}. Belo nome. Deixe-me pensar nas vogais dele...'
       .format(palavra))

time.sleep(3)
print ('bom...')
#testa cada letra na palavra
for letter in palavra:
#verifica se a letra já foi encontrada
    if letter in enc:
        print ( letter + " já foi")
#adiciona 1 à frequência da vogal encontrada
        f [letter] += 1
#indentifica vogais, consoantes e espaços
    else:
        time.sleep(2)
        if letter in vogais:
           
            print (letter + " é vogal")
            enc.append(letter)
#coloca a letra no dicionário com valor inicial de 1
            f [letter] = 1
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

vogais = ['a','e','i','o','u']
palavra = input('Qual seu nome? ')
enc = []

for letter in palavra:
    if letter not in enc:
        if letter in vogais:
            enc.append(letter)
            print ('{} é vogal'.format(letter))
        else:
            print('{} é consoante'.format(letter))
    else:
        print('{} essa já foi'.format(letter))
print (enc)
        
vogais_frequencia = {'a':0,
          'e':0,
          'i':0,
          'o':0,
          'u':0,}
vogais = ['a','e','i','o','u']
palavra = input('qual a palavra ')
pl = list(palavra)

for n in pl:
    if n in vogais:
        vogais_frequencia[n] += 1
        print (n)
    elif n ==' ':
        print ('espacinho maroto')
    else:
        print ('não é vogal')
        
for n,v in vogais_frequencia.items():
    
    print (n, 'apareceu', v, 'vezes')

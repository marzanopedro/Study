# =============================================================================
# Primeiro código estudado pelo livro "Use a Cabeça! - Python" para fins
#didáticos
#Pedro Marzano 2019
# =============================================================================

#importação de um módulo da biblioteca padrão do python.
from datetime import datetime

#EStabelecimento de uma variável em forma de lista. A lista comporta valores
#diversos inclusive em diferentes formatos.
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
        , 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59
        ]


# importado o submódulo datetime, aplica-se o método "today" na forma
# apresentada. Seria possível criar uma variável temporária "time" e dela
# extrair os minutos para outra variável. Entretanto, o pyhton não recomenda
# este tipo de variável temporária.

right_this_minute = datetime.today().minute


# O operador "in" verifica se o valor da variável está contido na variável 
# "odds" definida anteriormente, retornando valor "True" ou "False".
# O python utiliza o recúo unido aos dois pontos para identificar blocos, aqui
# chamados de suítes.

if right_this_minute in odds:
    print ("this minute seems a little odd")
else:
    print ("not odd")

# Há também o elif, utilizado quantas vezes forem necessárias para análise
# de outras condições


# =============================================================================
# odd.py versão aprimorada com loop
# =============================================================================
from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
        , 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# A ferramenta for, nesta atuação, permite a execução do suíte com base no
# número apresentado no range.
for i in range (5) :
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print ("this minute seems a little odd")
    else:
        print ("not odd")



# =============================================================================
# Aprimoramento do código odd agora com a função de tempo estabelecida pelo 
#módulo "time"
# ===================================================================

#importando módulo "time"
import time

from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
        , 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range (100) :
    #utilização da função sleep, que determina o tempo de "congelamento" do
    #código em segundos.
    time.sleep(0.01)
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print ("this minute seems a little odd")
    else:
        print ("not odd")
        
# =============================================================================
# Aprimoramento do código com a possibilidade de escolha aleatória do
# tempo de espera
# =============================================================================

#Importando o pacote "random" da biblioteca python
import time, random

from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
        , 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range (5) :
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print ("this minute seems a little odd")
    else:
        print ("not odd")
#    defindo o tempo de espera para um número aleatório entre 1 e 60 segundos 
#    através da função "randint" do método importado "random"
    
    time.sleep(random.randint(1,60))
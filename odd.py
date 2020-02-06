# =============================================================================
# Primeiro código estudado pelo livro "Use a Cabeça! - Python" para fins
#didáticos
#Pedro Marzano 2019
# =============================================================================
#
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

# =============================================================================
# O operador "in" verifica se o valor da variável está contido na variável 
# "odds" definida anteriormente, retornando valor "True" ou "False".
# O python utiliza o recúo unido aos dois pontos para identificar blocos, aqui
# chamados de suítes.
# =============================================================================
if right_this_minute in odds:
    print ("this minute seems a little odd")
else:
    print ("not odd")
# =============================================================================
# Há também o elif, utilizado quantas vezes forem necessárias para análise
# de outras condições
# =============================================================================

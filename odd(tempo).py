
# =============================================================================
# Aprimoramento do código odd agora com a função de tempo estabelecida pelo 
#módulo "time"
# ===================================================================

#importando módulo "time"
import time

from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
        , 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range (10) :
    #utilização da função sleep, que determina o tempo de "congelamento" do
    #código em segundos.
    time.sleep(1)
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print ("this minute seems a little odd")
    else:
        print ("not odd")
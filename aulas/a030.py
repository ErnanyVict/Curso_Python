''' CONTANTE = "Variaveis que não vão mudar
muitas condições no mesmo if é ruim
    <- contagem de complexidade
'''

velocidade = 30
local_carro = 101

RADAR_1 = 60 # <- constantes, não vão mudar
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_1)and \
    local_carro <= (LOCAL_1 + RADAR_1)

if vel_carro_pass_radar_1:
    print('velocidade do carro passou do radar 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print("Carro multado em radar 1")



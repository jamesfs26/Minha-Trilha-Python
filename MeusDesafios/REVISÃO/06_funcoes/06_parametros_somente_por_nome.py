

# Argumentos Hibrido "*" (nome) e "/" (posição)
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

print(" ")

# * exclusivamente por nome (keyword only)
def comodos_casa(*, entrada, sala, quartos, sala_de_jantar, cozinha, banheiro, area_de_servico, garagem, quintal, area_de_lazer):
    print(entrada, sala, quartos, sala_de_jantar, cozinha, banheiro, area_de_servico, garagem, quintal, area_de_lazer)

comodos_casa(entrada="Espaço vazio ", sala="sofás, tV e cadeiras ", quartos="Camas, guarda-roupas, e comôda ", sala_de_jantar="Computador ", cozinha="Fogão, mesa, geladeira, armario, pia e banheiro ", banheiro="Sanitario, chuveiro e espelheira ", area_de_servico="Maquina de lavar, armario, mini-estante e tanque ", garagem="ferramentas ", quintal="plantas ", area_de_lazer="Piscina ")





# BLOCO DE EXPLICAÇÃO - Inicio

# * keyword Only (Exclusivamente por nome) = Parâmetros Nomeados
# / Positional only (Exlusivamente por posição)
# ** (Dicionario{Chave-valor}) parâmetros variáveis

# BLOCO DE EXPLICAÇÃO - Final













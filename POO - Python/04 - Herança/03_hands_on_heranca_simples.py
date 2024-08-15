# Hands On - Herança Simples

# Classe Pai == Moveis 
# Classes Filhas: Armario, Guarda-Roupas, Geladeira, Máquina de Lavar e Tv.

class moveis:
    def __init__(self, cor, tamanho, valor, usa_energia, material, peso):
        self.cor = cor
        self.tamanho = tamanho
        self.valor = valor
        self.usa_energia = usa_energia
        self.material = material
        self.peso = peso
        
    def funcao(self):
        print("Função: Ajudar em casa")
               
    def usado_na_sala(self, usado):
        if usado:
            print("Este móvel é usado na sala!")
        else:
            print("Não é usado na sala!")
    
    def __str__(self) -> str:
        return self.cor
    
    def exibir_informacoes(self):
        info = (f"Cor: {self.cor}, Tamanho: {self.tamanho}, Valor: {self.valor}, "
                f"Usa Energia: {'Sim' if self.usa_energia else 'Não'}, "
                f"Material: {self.material}, Peso: {self.peso}")
        print(info)
    
    
# Herdando Atributos e Implementos   
    
# Armario   
class armario(moveis):
    def __init__(self, cor, tamanho, valor, usa_energia, material, peso):
        super().__init__(cor, tamanho, valor, usa_energia, material, peso)
             
    def dispensa(self):
        print("O armario está carregado de comida!")
    
    def bateria(self):
        print("O armario está carregado de panelas e estojos!")
          
    def gavetas(self):
        print("O armario está carregado de utensilios de cozinha: talheres, garfos, facas.")
            
    def prateleiras_superiores(self):
        print("O armario está carregado com recipientes de vidro: pratos, copos, xícaras etc.")
            
    def prateleiras_inferiores(self):
        print("Dispensa de comida!")     

# Guarda-Roupas
class guarda_roupas(moveis):
    def __init__(self, cor, tamanho, valor, possui_portas, quantidade_portas, material, peso):
        super().__init__(cor, tamanho, valor, False, material, peso)
        self.possui_portas = possui_portas
        self.quantidade_portas = quantidade_portas
                
    def estado(self):
        print("O Guarda-roupas está cheio.") 
        
    def varao_cabide(self):
        print("O Varal de Cabide está ocupado guardando camisetas sociais, Blazers e Palétos.")
        
    def prateleiras(self):
        print("As Prateleiras estão reservadas para roupas dobradas.")
        
    def gavetas(self):
        print("O Guarda-Roupa possui 3 gavetas")
        
    def gaveta_1(self):
        print("Gaveta 1: Está reservada para roupas íntimas [cuecas e meias].")

    def gaveta_2(self):
        print("Gaveta 2: Está reservada para roupas de baixo [calção, calça e bermuda].")

    def gaveta_3(self):
        print("Gaveta 3: Está reservada para camisetas casuais.")
        
        
class geladeira(moveis):
    def __init__(self, cor, tamanho, valor, quantidade_portas, quantidade_grelhas, material, peso):
        super().__init__(cor, tamanho, valor, True, material, peso)
        self.quantidade_portas = quantidade_portas
        self.quantidade_grelhas = quantidade_grelhas
        
    def exibir_informacoes(self):
        info = (f"Cor: {self.cor}, Tamanho: {self.tamanho}, Valor: {self.valor}, Quantidade de Portas: {self.quantidade_portas}, Quantidade de Grelhas: {self.quantidade_grelhas}, "
                f"Usa Energia: {'Sim' if self.usa_energia else 'Não'}, "
                f"Material: {self.material}, Peso: {self.peso}")
        print(info)
        
    def quantidade_gavetas(self):
        print("A geladeira possui 2 gavetas")
     
    def gaveta_superior(self):
        print("Gaveta Superior: Reservada para laticínios (queijos, manteiga, iogurte), sobras de comidas em recipientes bem fechados, condimentos e molhos.")
      
    def gaveta_inferior(self):
        print("Gaveta Inferior: Frutas (maçãs, peras, uvas, kiwi, melancia e morangos), verduras (alface, espinafre, couve) legumes (cenoura, pimentões, cebola, alhos, abobrinha).")
              
    def porta_principal(self):
        print("Prateleiras: Uso geral")
        print("Compartimentos da Porta: Bebidas (água, cerveja, sucos, refrigerantes), condimentos (tempero completo, molhos, maionese, ketchup) ovos, manteigas e queijos.")
        
    def congelador(self):
        print("Reservado para alimentos frescos (carnes, peixes, frango, linguiças, salsichas) ou congelados (polpas de frutas, sucos, frutas, legumes ou verduras já cortados) e alimentos já cozidos (arroz, feijão, macarrão, sopas e etc.).")
        

class maquina_lavar(moveis):
    pass

class tv(moveis):
    pass


# Chamada do Armário
cozinha = armario("azul com preto", "1 metro e 80 cm", "R$ 2.700,00", False, "metal reforçado", "140 Kg")
print("Armário:")
cozinha.funcao()
cozinha.dispensa()
cozinha.bateria()
cozinha.gavetas()
cozinha.prateleiras_inferiores()
cozinha.prateleiras_superiores()
print(" ")

# Chamada do Guarda-Roupas
print("Guarda-Roupas:")
gr = guarda_roupas("preto e branco", "2 metros e 10 cm", "R$ 2.500,00", True, "4 Portas", "Madeira Prensada", "160 Kg")
gr.funcao()
gr.estado() 
gr.varao_cabide()
gr.prateleiras()
gr.gavetas()
gr.gaveta_1()
gr.gaveta_2()
gr.gaveta_3()
print(" ")

# Chamada da Geladeira
print("Geladeira:")
refrigerador = geladeira("prata", "1 metro e 80 cm", "R$ 3.200,00", "2 Portas: Principal e Congelador", "4 Grelhas", "Aço Inox", "120 Kg")
refrigerador.funcao()
print("Descrição do Móvel:")
refrigerador.exibir_informacoes()
refrigerador.usado_na_sala(False)
refrigerador.quantidade_gavetas()
refrigerador.gaveta_superior()
refrigerador.gaveta_inferior()
refrigerador.porta_principal()
refrigerador.congelador()
print(" ")



# cor, tamanho, valor, quantidade_portas, quantidade_grelhas, material, peso

# Chamada da Maquina de Lavar
#movel_4 = maquina_Lavar("branca", "50 cm", "R$ 1.400,00", True, "Metalão", "80 Kg")
#print(movel_4)
#movel_4.funcao
#print(" ")

# Chamada da TV
#televisao = tv("cinza com bordas pretas", "50 Polegadas", "R$ 2.400,00", True, "Plastico reforçado", "25 Kg")
#print(televisao)
#televisao.funcao


#movel_5.usado_na_sala(usado=tv)











# EXPLICAÇÃO:
# Uma "classe filha" herda os comportamentos e caracteristicas de uma "Classe Pai". Entretanto o Python permite a alteração...
# Desses comportamentos e caracteristicas, "subescrevendo" por outras informações.









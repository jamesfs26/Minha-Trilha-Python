
# sort(*, key=None, reverse=False): Ordena os itens da lista.
# Os argumentos key e reverse podem ser usados para personalizar a ordem.

# Lista 1

lista1 = [7, 2, 8, 4, 1, 5, 3, 9, 6]
lista1.sort() # Organiza em Ordem númerica crescente
print("Lista 1", lista1)

# Lista 2

lista2 = ["Leão", "Macaco", "Porco", "Zebra", "Tamanduá", "Rato", "Foca", "Gato"]
lista2.sort(reverse=True) # Reverteu em Ordem Alfabetica Regressiva
print("Lista 2:", lista2)


# Lista 3

lista3 = [7, 2, 8, 4, 1, 5, 3, 9, 6]
lista3.sort(reverse=False) # Organiza em Ordem númerica crescente
  
print("Lista 3:", lista3)

# Organizou em Ordem Alfabetica crescente

lista4 = ["Abelha", "Lontra", "Corsa", "Vaca", "Pato", "Égua", "Onça", "Cachorro"]
lista4.sort(key=len)
print("Lista 4:", lista4)


# Lista 5

lista5 = [752.0, 54.2, 87.63, 754, 9821, 4125, 1423, 589, 46]
lista5.sort(key=lambda x: -x)
print("Lista 5:", lista5)


# lista6 = ["carro", "moto", "bicicleta", "skate", "patinete", "patins", "mobilete", "ônibus", "caminhão"]



#.sort(key=lambda x: -x = Reverte lista de valor númerico
# .sort(key=len) = (Strings) Organiza os valores por tamanho (quantidade de caracteres).
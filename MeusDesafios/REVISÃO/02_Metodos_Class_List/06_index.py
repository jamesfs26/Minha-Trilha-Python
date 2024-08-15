
# index(x, [start, [end]]): Retorna o índice da primeira ocorrência do item. 
# Opcionalmente, pode-se especificar um intervalo (start, end) para a busca. 
# Lança um ValueError se o item não for encontrado.

animais = ["python", "jacaré", "serpente", "caracol", "javali", "tubarão", "javali", "python", "jacaré", "serpente",]

javali = animais.index("javali")	
python = animais.index("python")
caracol = animais.index("caracol")
jacare = animais.index("jacaré")
StartEnd = animais.index("serpente", 0, 9)
#error = animais.index("abelha")

print(animais)
print(javali)
print(python)
print(caracol)
print(jacare)
#print(error)
print(StartEnd)



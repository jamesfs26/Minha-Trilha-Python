
# Retorna uma nova lista ordenada a partir dos elementos da lista original, sem modificar a lista original.
# Você pode usar os argumentos key e reverse para personalizar a ordenação.

animais = ["python", "jacaré", "serpente", "caracol", "javali", "tubarão"]
print("Original:", animais)

ordenada = sorted(animais)
print("Ordenada:", ordenada)

ordenada_reversa = sorted(animais, reverse=True)
print("Ordenada reversa:", ordenada_reversa)

# Ordenação com uma função chave
ordenada_por_comprimento = sorted(animais, key=len)
print("Ordenada por comprimento:", ordenada_por_comprimento)

















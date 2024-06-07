# Implementação do algoritmo de ordenação Bubble Sort

def bubble_sort(lista):
    
    n = len(lista)

    for elemento in range(n):
  
        for posicao in range(0, n - elemento - 1):
    
            if lista[posicao] > lista[posicao + 1]:
 
                troca = lista[posicao]
                lista[posicao] = lista[posicao + 1]
                lista[posicao + 1] = troca
                
    return lista
        
tamanho_lista = int(input("Insira o tamanho da lista: "))

lista = []

for numero in range(tamanho_lista):
    num = int(input("Insira um número: "))
    lista.append(num)

lista_ordenada = bubble_sort(lista)

print("Lista ordenada: ", lista_ordenada)            
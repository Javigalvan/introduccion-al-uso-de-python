def main():
    lista_frutas1 = ['Manzana', 'Pera', 'Melocotón']
    lista_frutas2 = ['Kiwi', 'Sandia', 'Melón']
    lista_frutas1.extend(lista_frutas2)
    print("Último elemento de la lista:", lista_frutas1[-1])
    
    tupla_numeros = (3, 5, 7)
    print("Primer elemento de la tupla:", tupla_numeros[0])

    inicio = int(input("Introduce el valor de inicio: "))
    fin = int(input("Introduce el valor de fin: "))
    salto = int(input("Introduce el valor de salto: "))
    
    rango = range(inicio, fin, salto)

    print("El rango generado es:", list(rango))

if __name__ == "__main__":
    main()
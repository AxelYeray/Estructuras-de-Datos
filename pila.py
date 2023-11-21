
class Pila:
    #constructor
    def __init__(self):
        self.elementos = []

    #Insertar un elemento
    def insertar(self,dato):
        self.elementos.append(dato)

    #Esta vacia?
    def esta_Vacia(self):
        return len(self.elementos) == 0

    #Sacar un Elemento
    def quitar(self):
        if self.esta_Vacia():
            print("La lista esta vacia!! Retorna None...")
            return None
        return self.elementos.pop()
    
    #Limpiar la pila
    def limpiar(self):
        del self.elementos[:]

    #Cima de la pila
    def cima(self):
         if self.esta_Vacia():
            print("La lista esta vacia!! Retorna None...")
            return None
         return self.elementos[-1]

    #Tamaño de la pila
    def tamanho(self):
        return len(self.elementos)
    
    #Mostrar elementos de la pila
    def mostrarElementos(self):
        print("Los elementos de la pila son:")
        print(self.elementos)


def menu_pila():
    pila = Pila()
    
    while True:
        print("\nMenu Pila:")
        print("1. Insertar elemento")
        print("2. Sacar elemento")
        print("3. Mostrar cima")
        print("4. Mostrar tamaño")
        print("5. Mostrar elementos")
        print("6. Limpiar pila")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            dato = input("Ingrese el elemento a insertar: ")
            pila.insertar(dato)
            print(f"{dato} ha sido insertado en la pila.")

        elif opcion == "2":
            elemento = pila.quitar()
            if elemento is not None:
                print(f"Elemento sacado de la pila: {elemento}")

        elif opcion == "3":
            cima = pila.cima()
            if cima is not None:
                print(f"Cima de la pila: {cima}")

        elif opcion == "4":
            tamaño = pila.tamanho()
            print(f"Tamaño de la pila: {tamaño}")

        elif opcion == "5":
            pila.mostrarElementos()

        elif opcion == "6":
            pila.limpiar()
            print("La pila ha sido limpiada.")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_pila()        

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
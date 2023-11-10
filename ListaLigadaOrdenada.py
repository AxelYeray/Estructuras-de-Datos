class Node:
    '''Nodo para usar con lista doblemente enlazada'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''Una lista ordenada de elementos doblemente enlazada, desde el más bajo (cabeza de lista) hasta el más alto (final de la lista)'''

    def __init__(self):
        '''Utilice UN nodo ficticio como se describe en la clase
            ***Sin otros atributos***
            NO tenga un atributo para realizar un seguimiento del tamaño'''
        dummy = Node(None)
        dummy.next = dummy
        dummy.prev = dummy
        self.head = dummy


    def is_empty(self):
        '''Devuelve Verdadero si OrderedList está vacío
             DEBE tener un rendimiento O(1)'''
        return self.head.next == self.head

    def add(self, item):
        '''Agrega un artículo a OrderedList, en la ubicación adecuada según el orden de los artículos
            desde el más bajo (al principio de la lista) al más alto (al final de la lista) y devuelve Verdadero.
            Si el elemento ya está en la lista, no lo vuelva a agregar y devuelva False.
            DEBE tener un rendimiento de caso promedio O(n). Suponga que todos los elementos agregados a su
            La lista se puede comparar usando el operador < y se puede comparar en términos de igualdad/desigualdad.
            No hagas otras suposiciones sobre los elementos de tu lista.'''
        new_node = Node(item)

        place_found = False
        current = self.head.next
        while not place_found:
            if current.item == new_node.item:
                return False

            if current == self.head:
                new_node.prev = self.head.prev
                new_node.next = self.head
                self.head.prev.next = new_node
                self.head.prev = new_node
                return True

            if new_node.item < current.item:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                return True

            else:
                current = current.next


    def remove(self, item):
        '''Elimina la primera aparición de un artículo de OrderedList. Si el artículo se elimina (estaba en la lista)
            devuelve Verdadero. Si el elemento no se eliminó (no estaba en la lista), devuelve Falso
            DEBE tener un rendimiento de caso promedio O(n)'''
        current = self.head.next
        while current != self.head:
            if current.item == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            else:
                current = current.next
        return False



    def index(self, item):
        '''Devuelve el índice de la primera aparición de un elemento en OrderedList (suponiendo que el encabezado de la lista sea el índice 0).
            Si el artículo no está en la lista, devuelva Ninguno
            DEBE tener un rendimiento de caso promedio O(n)'''
        current = self.head.next
        index = 0
        while current != self.head:
            if current.item == item:
                return index
            else:
                current = current.next
                index +=1
        return None

    def pop(self, index):
        '''Elimina y devuelve el elemento en el índice (suponiendo que el encabezado de la lista sea el índice 0).
            Si el índice es negativo o >= tamaño de la lista, genera IndexError
            DEBE tener un rendimiento de caso promedio O(n)'''
        if index >= self.size() or index < 0:
            raise IndexError
        else:
            current = self.head.next
            for i in range(index):
                current = current.next
            return_val = current.item
            current.prev.next = current.next
            current.next.prev = current.prev
            return return_val


    def search(self, item):
        '''Busca un artículo en OrderedList, devuelve True si el artículo está en la lista, False en caso contrario".
            Para practicar la recursividad, este método debe llamar a un método RECURSIVO que
            buscará en la lista
            DEBE tener un rendimiento de caso promedio O(n)'''
        return self.search_helper(self.head.next, item)

    def python_list(self):
        '''Devuelve una representación de lista Python de OrderedList, de principio a fin
            Por ejemplo, una lista con números enteros 1, 2 y 3 devolvería [1, 2, 3]
            DEBE tener rendimiento O(n)'''
        running_list = []
        current = self.head.next

        while current != self.head:
            running_list.append(current.item)
            current = current.next
        return running_list


    def python_list_reversed(self):
        '''Devuelve una representación de lista de Python de OrderedList, desde el final hasta el principio, usando recursividad
            Por ejemplo, una lista con números enteros 1, 2 y 3 devolvería [3, 2, 1]
            Para practicar la recursividad, este método debe llamar a un método RECURSIVO que
            devolverá una lista invertida
            DEBE tener rendimiento O(n)'''
        return self.reverse_helper(self.head.prev)

    def size(self):
        '''Devuelve el número de artículos en OrderedList
            Para practicar la recursividad, este método debe llamar a un método RECURSIVO que
            contará y devolverá el número de elementos de la lista
            DEBE tener rendimiento O(n)'''
        return self.size_helper(self.head.next)
    def size_helper(self, current_node):
        if current_node == self.head:
            return 0
        else:
            return(1 + self.size_helper(current_node.next))

    def search_helper(self, current_node, item):
        if current_node == self.head:
            return False
        if current_node.item == item:
            return True
        else:
            return self.search_helper(current_node.next, item)

    def reverse_helper(self, current_node):
        if current_node == self.head:
            return []
        else:
            return([current_node.item] + self.reverse_helper(current_node.prev))
        
def main():
    ordered_list = OrderedList()

    while True:
        print("\nMenú:")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Buscar elemento")
        print("4. Imprimir lista ordenada")
        print("5. Imprimir lista en reversa")
        print("6. Tamaño de la lista")
        print("0. Salir")

        choice = input("Elije una opción: ")

        if choice == "1":
            item = input("Introduce el elemento a agregar: ")
            if ordered_list.add(item):
                print(f"'{item}' ha sido agregado a la lista.")
            else:
                print(f"'{item}' ya existe en la lista y no se ha agregado.")

        elif choice == "2":
            item = input("Introduce el elemento a eliminar: ")
            if ordered_list.remove(item):
                print(f"'{item}' ha sido eliminado de la lista.")
            else:
                print(f"'{item}' no se encontró en la lista y no se ha eliminado.")

        elif choice == "3":
            item = input("Introduce el elemento a buscar: ")
            if ordered_list.search(item):
                print(f"'{item}' se encuentra en la lista.")
            else:
                print(f"'{item}' no se encuentra en la lista.")

        elif choice == "4":
            print("Lista ordenada:")
            print(ordered_list.python_list())

        elif choice == "5":
            print("Lista en reversa:")
            print(ordered_list.python_list_reversed())

        elif choice == "6":
            print(f"Tamaño de la lista: {ordered_list.size()}")

        elif choice == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
        main()

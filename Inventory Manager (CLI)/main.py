from product import creat_product,remove_product,search_product
from storage import lista

def menu():
    
    while True:
        try:
            print('''
                  
===menu===
(A)dicionar
(R)emolver
(L)istar
(B)uscar
(S)air
''')
            Usuario = input('Digite:').upper()

            if Usuario.startswith('A'): # verifica primeira letra
                creat_product()
            elif Usuario.startswith('R'):
                print(remove_product())
            elif Usuario.startswith('L'):
                if len(lista) >= 1: 
                    print([item for item in lista]) #usando comprehension
                else:
                    print('==nada para listar==')

            elif Usuario.startswith('B'):
                for search_item in search_product():
                    print(search_item)
                    
            elif Usuario.startswith('S'):
                return 'encerrando...'
            
            else:
                print(f'{Usuario} letra inesistente')
        except ValueError:
            print('Apenas Letras')
            ...



print(menu())

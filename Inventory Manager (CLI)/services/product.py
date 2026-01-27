from storage import list_product,lista
from os import system
from utils import tax_calculate


def creat_product():
    list_product['ID'] = len(lista) 
    list_product['Name'] = input('Digite nome do produto:').replace('.','')

    while not len(list_product['Name'].strip()) or list_product['Name'].isdigit(): # validacao de nomes
        print('==Deve conter uma letra==')
        list_product['Name'] = input('Digite nome do produto:').strip().replace('.','')

    while True:
        try: 
            list_product['price'] = float(input('Digite valor do produto:'))
            list_product['tax'] = float(input('Digite taxa do produto:'))

            #calculando taxa
            add_tax = tax_calculate(list_product['price']) 
            list_product['price'] = add_tax(list_product['tax']) #adicionando novo valor com a taxa

            lista.append(list_product.copy())
            break
        except ValueError:
            print('Erro apenas numero!!')


def remove_product():
    while True:
        try:
            print('=====remoção de produto====')
            if len(lista) < 1:
                return 'Não há produtos para remolver'
            
            user_remove = int(input('Digite o ID valido: '))

            lista.pop(user_remove)
            break

        except ValueError:
            system('cls')
            print('====apenas numero!====')
        except IndexError:
            system('cls')
            print('====ID nao valido====')

    #oraganizar IDs
    for i,product in enumerate(lista):
        product['ID'] = i 
    return '====Item Remolvido===='




def search_product(): # buscar produtos de forma limpa e eficiente , usando generator
    if len(lista) < 1:
        yield '==Nenhum item para Buscar=='
        return # encerrar generator
    item_found = False
    user = input('qual nome do item?').lower()
    for product in lista:
        if user in product['Name'].lower():
            item_found = True
            yield product
    if not item_found:
        yield '==item nao encontrado!=='

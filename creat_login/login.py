def creat_login(accounts):
    while True:
        try:
            user_creat = [{'name':input('Digite nome: ') , 'age':int(input('Digite idade: '))}]

            if len(accounts) > 0:
                name_users = [value['name'] for value in accounts] # salva apenas nomes do dic_pricipal
                if not user_creat[0]['name'] in name_users: # verifica com o dic_pricipal
                    accounts.append(*user_creat)
                    return '"User added"'
            else:
                accounts.append(*user_creat)
                return '"User added"'                
            return '"Invalid user"'
        except ValueError:
            print('Digite int')

dic_account = []

for i in range(4):
    print(creat_login(dic_account))

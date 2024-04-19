import random

lista_1 =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

listas_juntas = list(zip(lista_1, lista_2))

random.shuffle(listas_juntas)

def senha_com_8(senha):
    if len(senha) == 8:
        return True
    else:
        return False

def senha_com_10(senha):
    if len(senha) == 10:
        return True
    else:
        return False

def adicionar_senha_arquivo(escreva):
    # Abrir o txt
    with open('senhas.txt', 'a') as arquivo:
        # Escrever a senha
        arquivo.write(escreva + '\n')

def listar_senhas_arquivo():
    print('Senhas registradas:')
    # Abrir o arquivo com senhas(leitura)
    with open('senhas.txt', 'r') as arquivo:
        # Ler as senhas do arquivo
        for linha in arquivo:
            print(linha.strip()) # .strip() remove os espaços

def Protetor_de_Senhas():
    print('''
    Bem-Vindo
        ao
    programa
'Protetor de senhas'
          
Temos as seguintes funções:
Senhas com oito digitos(8)
Senhas com dez digitos(10)

Caso já tenha a senha adicionada:
Ver senhas(V)
''')
    resposta = input('Digite o número função:').upper()
    if resposta == '8':
        print('Ok, agora a senha!')
        senha = input('Senha:')
        if senha_com_8(senha):
            listas_embaralhadas = listas_juntas[:8]
            random.shuffle(listas_embaralhadas)
            nova_senha_1 = ''.join(str(e[0]) + str(e[1]) for e in listas_embaralhadas)
            print(f'A senha está pronta {nova_senha_1}')
            escreva = f'{nova_senha_1} = {senha}'
            adicionar_senha_arquivo(escreva)
    elif resposta == '10':
        print('Ok, agora a senha!')
        senha = input('Senha:')
        if senha_com_10(senha):
            listas_embaralhadas = listas_juntas[:10]
            random.shuffle(listas_embaralhadas)
            nova_senha_2 = ''.join(str(e[0]) + str(e[1]) for e in listas_embaralhadas)
            print(f'A senha está pronta {nova_senha_2}')
            escreva = f'{nova_senha_2} = {senha}'
            adicionar_senha_arquivo(escreva)

    elif resposta == 'V':
        print('Ok, agora vamos mostrar as senhas já registradas!')
        listar_senhas_arquivo()


Protetor_de_Senhas()

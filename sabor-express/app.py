import os

restaurantes = [{'nome':'Pac-man', 'categoria':'Pizza', 'ativo':True}]

def exibir_nome_programa(): 
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
    ''' Exibe as opções do menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do app '''

    exibir_subtitulo('Finalizar app')

def retornar_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal '''

    input('Digite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    ''' Exibe a mensagem de opção inválida e retorna ao menu principal '''

    print('Opçåo inválida!\n')
    retornar_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela '''

    os.system('clear')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar novos restaurantes 

    Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes

    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    retornar_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista '''

    exibir_subtitulo('Restaurantes listados')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status') 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    retornar_menu_principal()

def alternar_estado_resturante():
    ''' Altera o estado ativo/desativado de um restaurante '''

    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    retornar_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_estado_resturante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """ Função principal que inicia o programa """
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
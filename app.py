import os

restaurantes = [{"nome": "Madame Sushi", "categoria": "Japonesa", "ativo": False},
                {"nome": "Madame e Pasta", "categoria": "Italiano", "ativo": True},
                {"nome": "Madame Mex", "categoria": "Mexicano", "ativo": False}]

def mostrar_nome_app():
    """Essa função mostra o nome do app no início da aplicação"""

    print("""

█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀▄ █▀▀ █── ─▀─ ▀█─█▀ █▀▀ █▀▀█ █──█
█─▀─█ █▄▄█ █──█ █▄▄█ █─▀─█ █▀▀ 　 █──█ █▀▀ █── ▀█▀ ─█▄█─ █▀▀ █▄▄▀ █▄▄█
▀───▀ ▀──▀ ▀▀▀─ ▀──▀ ▀───▀ ▀▀▀ 　 ▀▀▀─ ▀▀▀ ▀▀▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀ ▄▄▄█
      """)

def mostrar_opcoes():
    """Essa função mostra as opções do app"""

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """Essa função mostra a mensagem ao finalizar o app"""
    exibir_subtitulo("App Finalizado!")

def retornar_ao_menu_principal():
    """Essa função mostra uma mensagem pedindo ao usuário para apertar uma tecla para retornar ao menu principal"""
    input("\nDigite uma tecla para voltar ao menu principal. ")
    main()

def exibir_subtitulo(texto):
    """"Essa função exibe o subtitulo das opções que o usuário escolher"""

    os.system("clear")
    linha = "=" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print("Opção inválida!\n")
    retornar_ao_menu_principal()

def cadastrar_novo_restaurante():
    """Essa função cadastra um novo restaurante no app"""

    exibir_subtitulo("Cadastro de novos restaurantes!")
    nome_do_restaurante = input("Digite o nome do restaurante a ser cadastrado: ")
    categoria = input(f"Digite a categoria do {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Parabéns! O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")

    retornar_ao_menu_principal()

def listar_restaurantes():
    """"Essa função mostra uma lista dos restaurantes cadastrados"""

    exibir_subtitulo("Listando os restaurantes: ")
    titulo_colunas = (f'{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | "Status"')
    contorno = "˜" * len(titulo_colunas)

    print(contorno)
    print(titulo_colunas)
    print(contorno)

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    retornar_ao_menu_principal()

def alterar_estado_restaurante():
    """"Essa função altera o estado dos restaurantes de ativado para desativado e vice-versa"""

    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!!"
            print(mensagem)
    if not restaurante_encontrado:
        print("Esse restaurante não foi encontrado!")

    retornar_ao_menu_principal()

def escolher_opcao():
    """"Essa função mostra o menu de opções que o usuário tem ao abrir o app"""

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("clear")
    mostrar_nome_app()
    mostrar_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

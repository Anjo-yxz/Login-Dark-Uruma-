import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = """
▓█████▄  ▄▄▄      ██▀███   ██ ▄█▀     █    ██  ██▀███   █    ██  ███▄ ▄███▓ ▄▄▄     
▒██▀ ██▌▒████▄   ▓██ ▒ ██▒ ██▄█▒      ██  ▓██▒▓██ ▒ ██▒ ██  ▓██▒▓██▒▀█▀ ██▒▒████▄   
░██   █▌▒██  ▀█▄ ▓██ ░▄█ ▒▓███▄░     ▓██  ▒██░▓██ ░▄█ ▒▓██  ▒██░▓██    ▓██░▒██  ▀█▄ 
░▓█▄   ▌░██▄▄▄▄██▒██▀▀█▄  ▓██ █▄     ▓▓█  ░██░▒██▀▀█▄  ▓▓█  ░██░▒██    ▒██ ░██▄▄▄▄██
░▒████▓ ▒▓█   ▓██░██▓ ▒██▒▒██▒ █▄    ▒▒█████▓ ░██▓ ▒██▒▒▒█████▓ ▒██▒   ░██▒▒▓█   ▓██
 ▒▒▓  ▒ ░▒▒   ▓▒█░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▒   ▓▒█
 ░ ▒  ▒ ░ ░   ▒▒   ░▒ ░ ▒ ░ ░▒ ▒░    ░░▒░ ░ ░   ░▒ ░ ▒ ░░▒░ ░ ░ ░  ░      ░░ ░   ▒▒ 
 ░ ░  ░   ░   ▒    ░░   ░ ░ ░░ ░      ░░░ ░ ░   ░░   ░  ░░░ ░ ░ ░      ░     ░   ▒  
   ░          ░     ░     ░  ░          ░        ░        ░            ░         ░  """


banco_de_dados = {
    "user123":"12345",
    "rafael":"ratodeacademia",
    #ADM acesso
    "rafa":"3244"
}

def opçao_login():
    print("---- 𝚂𝚒𝚜𝚝𝚎𝚖𝚊 𝚍𝚎 𝙻𝚘𝚐𝚒𝚗 ----")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in banco_de_dados and banco_de_dados[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

def registar_usuario():
    print("---- 𝚁𝚎𝚐𝚒𝚜𝚝𝚛𝚘 𝚍𝚎 𝙽𝚘𝚟𝚘 𝚄𝚜𝚞𝚊́𝚛𝚒𝚘 ----")
    novo_usuario = input("Digite o nome de usuário desejado: ")
    if novo_usuario in banco_de_dados:
        print("Nome de usuário já existe. Tente outro.")
        return
    nova_senha = input("Digite a senha desejada: ")
    banco_de_dados[novo_usuario] = nova_senha
    print("Usuário registrado com sucesso!")

while True:
    print(logo)
    print("\n")
    print("𝙱𝚎𝚖-𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝚜𝚒𝚜𝚝𝚎𝚖𝚊!")
    escolhas = input("1 - login\n2 - Registrar novo usuário\n3 - sair\nEscolha uma opção: ").lower()
    clear()

    if escolhas == "1":
        opçao_login()
    
    elif escolhas == "2":
        registar_usuario()

    elif escolhas == "3":
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida.")
    input("Pressione Enter para volta...")
    clear()

# Validação de entrada com tratamento de exceção
def verificar_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0:
                print("Idade Inválida")
            elif idade >= 18:
                print("Maior de idade")
            else:
                print("Menor de idade")
            break
        except ValueError:
            print("Erro: Somente número inteiro!.")
verificar_idade()
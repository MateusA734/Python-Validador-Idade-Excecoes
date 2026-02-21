# Validação de entrada com tratamento de exceção.
def verificar_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0:
                raise ValueError("Idade não pode ser negativa.")
            elif idade >= 18:
                print("Maior de idade")
            else:
                print("Menor de idade")
            break
        except ValueError as e:
            print(f"Erro: {e}")
verificar_idade()
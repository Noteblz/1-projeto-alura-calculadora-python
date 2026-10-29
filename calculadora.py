# ==========================================
# CALCULADORA SIMPLES EM PYTHON
# Operações: Adição, Subtração, Multiplicação e Divisão
# ==========================================

# 1. DEFINIÇÃO DAS FUNÇÕES MATEMÁTICAS
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão do primeiro pelo segundo. Protege contra divisão por zero."""
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# 2. LAÇO PRINCIPAL DO PROGRAMA (LOOP)
while True:
    print("\n" + "="*30)
    print("      CALCULADORA PYTHON      ")
    print("="*30)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair do programa")
    print("="*30)

    # 3. ENTRADA DA ESCOLHA DO USUÁRIO
    opcao = input("Escolha uma opção (1-5): ")

    # Condição para encerrar o programa
    if opcao == '5':
        print("\nObrigado por usar a calculadora! Até logo.")
        break

    # Verifica se a opção digitada é válida
    if opcao in ('1', '2', '3', '4'):
        try:
            # 4. CAPTURA DOS NÚMEROS (CONVERTENDO PARA FLOAT)
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\n[!] Erro: Por favor, digite apenas números válidos!")
            continue

        # 5. PROCESSAMENTO E EXIBIÇÃO DO RESULTADO
        if opcao == '1':
            resultado = somar(num1, num2)
            print(f"\n-> Resultado: {num1} + {num2} = {resultado}")
        elif opcao == '2':
            resultado = subtrair(num1, num2)
            print(f"\n-> Resultado: {num1} - {num2} = {resultado}")
        elif opcao == '3':
            resultado = multiplicar(num1, num2)
            print(f"\n-> Resultado: {num1} x {num2} = {resultado}")
        elif opcao == '4':
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                print(f"\n-> {resultado}")
            else:
                print(f"\n-> Resultado: {num1} / {num2} = {resultado}")
    else:
        print("\n[!] Opção inválida! Escolha um número entre 1 e 5.")

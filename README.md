# Imersão Engenharia de Software: Dev na Era da IA 🚀
## Desafio: Criando uma Calculadora com Google AI Studio

Repositório criado para registrar os testes e aprendizados desenvolvidos durante a Imersão Engenharia de Software da Alura, utilizando inteligência artificial para auxiliar no desenvolvimento de software.

---

## 📝 O Desafio
O objetivo do desafio consistia em:
1. Pedir para a IA do Google AI Studio criar uma calculadora simples em Python que realizasse as 4 operações básicas.
2. Continuar conversando com a IA para aprofundar o entendimento: pedir para explicar partes do código, identificar variáveis ou mostrar a lógica de tomada de decisão do programa.

---

## 🤖 Resposta e Explicação da IA
Abaixo está o detalhamento técnico fornecido pela IA explicando o funcionamento e os conceitos aplicados em cada parte da aplicação.

### 1. Criando as Funções Matemáticas (`def` e `return`)
```python
def somar(a, b):
    return a + b
```
* **`def` (definir):** Pense em uma função como uma ferramenta em uma caixa ou uma receita pronta. Você dá um nome para ela (`somar`) e diz que ela precisa de dois ingredientes: `a` e `b` (chamados de parâmetros).
* **Os dois pontos (`:`):** Indicam o início do que a função faz.
* **O espaço à esquerda (indentação):** O Python é muito organizado. Tudo que tem 4 espaços de recuo à direita pertence à função.
* **`return` (retornar):** É o resultado que a função devolve para você. Se você passar `5` e `3`, a função calcula `5 + 3` e "entrega" o número `8` de volta para quem chamou.

### 2. A Proteção na Divisão
```python
def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b
```
* Na matemática, não existe divisão por zero (tente dividir 10 balas para 0 crianças, não faz sentido).
* Se o Python tentar fazer `10 / 0`, o programa trava e desliga na hora.
* Por isso colocamos um aviso prévio: *"Se o segundo número (`b`) for igual a 0, nem tente calcular: devolva uma mensagem de erro!"*.

### 3. O Laço de Repetição (`while True` e `break`)
```python
while True:
    # Mostra o menu...
    if opcao == '5':
        break
```
* **`while True`:** Significa literalmente: *"Enquanto a verdade for verdadeira, repita tudo o que está aqui dentro"*. Ou seja, é um loop contínuo.
* **Por que usamos isso?** Sem o `while`, o programa faria apenas uma única conta e fecharia imediatamente. Com o `while`, ele faz a conta e volta para o menu para você poder fazer outra conta.
* **`break` (quebrar):** É o "freio de emergência". Quando o usuário escolhe a opção `'5'`, o `break` quebra o loop e encerra o programa.

### 4. A Entrada de Dados: `input()` e `float()`
```python
num1 = float(input("Digite o primeiro número: "))
```
Essa linha faz duas coisas de dentro para fora:
* **`input("...")`:** Pausa o programa e espera o usuário digitar algo e apertar Enter.
* **`float(...)`:** Aqui está o segredo mais importante de um iniciante! O `input()` sempre lê o que você digita como texto (*string*). Se o usuário digitar `5` e você fizer `"5" + "5"`, o Python junta os textos e o resultado vira `"55"`, e não `10`! Por isso usamos `float()`. A palavra *float* significa "número de ponto flutuante" (número decimal, como `7.5` ou `10.0`). Ele converte o texto em número real para podermos fazer contas de verdade.

### 5. O Escudo contra Travamentos (`try` e `except`)
```python
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Digite apenas números válidos!")
    continue
```
* **`try` (tentar):** O Python avisa: *"Tente converter o que o usuário digitou em número"*.
* **`except ValueError` (exceto se der erro de valor):** Se o usuário digitar "banana" em vez de um número, a conversão `float("banana")` geraria um erro fatal. Se isso acontecer, em vez de travar o programa com mensagens vermelhas feias, ele entra no `except`, mostra uma mensagem educada de aviso e usa o `continue` para voltar ao início do menu!

### 6. As Decisões: `if`, `elif` e `else`
```python
if opcao == '1':
    resultado = somar(num1, num2)
elif opcao == '2':
    resultado = subtrair(num1, num2)
...
else:
    print("Opção inválida!")
```
* **`==` (dois iguais):** Um sinal de igual (`=`) guarda um valor numa variável (ex: `x = 10`). Dois sinais (`==`) servem para perguntar se algo é igual (ex: *"A opção é igual a '1'?"*).
* **`if` (se):** Se a opção for `'1'`, chama a função `somar`.
* **`elif` (senão se):** Se não for a 1, mas for a `'2'`, chama a função `subtrair`.
* **`else` (senão):** Se não for nenhuma das opções anteriores (por exemplo, se a pessoa digitou 9), avisa que a opção é inválida.

### 7. Exibindo o Resultado Formatado (`f-strings`)
```python
print(f"Resultado: {num1} + {num2} = {resultado}")
```
* A letra `f` antes das aspas indica uma *f-string* (string formatada).
* Ela permite colocar variáveis diretamente dentro do texto usando chaves `{ }`.
* O Python substitui `{num1}`, `{num2}` e `{resultado}` pelos seus valores reais de forma limpa e legível.

---

## 💻 Código Completo Gerado
Este é o código final em Python resultante da interação com a IA:

```python
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
```

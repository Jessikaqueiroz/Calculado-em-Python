def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return  x / y

print("\nSelecione o número da operação desejada: \n")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

escolha = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\ndigite o primeiro número: "))
num2 = int(input("\ndigite o segundo número: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("\nOpção inválida!\n")
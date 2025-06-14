num1 = int(input("Coloque o primeiro numero: "))
num2 = int(input("Coloque o segundo numero: "))

operador = input("Escolha o operador [+ - * /]: ")

if operador == "+":
    print(num1 + num2),
elif operador == "-":
    print(num1 - num2),
elif operador == "*":
    print(num1 * num2),
elif operador == "/":
    print(num1 / num2)
else:
    print("operação inválida")

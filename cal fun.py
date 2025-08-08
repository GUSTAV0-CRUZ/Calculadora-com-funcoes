# Funções
print("calculadora de funções")
def soma( numb1, numb2):
    return numb1 + numb2

def epar(numb1) :
    return numb1 % 2 == 0

def sinal (numb1):
    if numb1 > 0 :
        return f"Positivo"
    elif numb1 < 0 :
        return f"Negativo"
    else :
        return f"È zero"

def mul (numb1, numb2) :
    return numb1 * numb2

def sub (numb1, numb2) :
    return numb1 - numb2

def div (numb1, numb2) :
    if numb2 != 0:
     return numb1 / numb2 
    else :
        print("Não pode ser dividido por 0 ")

def mtx (n1, n2) :
    if n1 % n2 == 0 :
        return f"{n} é multiplo de {n2}."
    else :
        return f"{n} não é múltiplo de {n2}."

def raiz (n1) :
    n = n1
    import math
    while True :
        if n1 < 0 :
            return f"Número negativo não tem raiz quadrada."
            break
        rz = math.sqrt(n1)
        if rz.is_integer() :
            return f"A raiz quadrada de {n1} é {rz}"
        else :
            return f"A raiz quadrada de {n1} é {rz:.2f}"




# Testes aqui
while True:
    rep = input("Deseja sair ? S/N: ")
    if rep.lower () == "s":
        break
    
    n1 = int(input("Número :"))
    
    print("Escolha uma operação: +, -, *, /, % . ")
    while True :
        op = input("Digite a operação desejada. ")
        if op in ["+", "-", "*", "/", "%"] :
            break
        else :
            print(op,"não é um sinal.")
            continue
            
    if op == "%" :
        n = raiz(n1)
        print(n)
        continue
    else :
        n2 = int(input("Número :"))
        if op == "/":
            if n2 != 0 :
                n = div(n1, n2)
            else :
                print("Não é possível dividir por 0. ")
                continue

        elif op == "+":
            n = soma(n1, n2)
        elif op == "-":
            n = sub(n1 , n2)
        elif op == "*" :
            n = mul(n1 , n2)
        else :
            print("Operação invalida")

    raiz()    
    print (n)
    print("Deseja escolher um número para saber se o resultado é múltiplo dele ?, s/n")
    q = input("Sim ou não ? ")
    if q.lower() == "s" :
            x = int(input("Número :"))
            print(mtx(n, x))
    else :
        print(n)

    if epar (n):
        print("È par")
    else :
        print("É impar")

    print(sinal(n))

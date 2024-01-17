# EXERCICIO 4
# USANDO OPERADORES ARITIMETICOS COM PYAUTOGUI
import pyautogui
import time
pyautogui.PAUSE = 0.3

yesorno = str(input("Você quer saber todas interações possiveis de 2 numeros? "))

if yesorno == 'sim':
    num1 = int(input('Digite um numero : '))
    num2 = int(input('Digite outro numero : '))
    s = num1 + num2
    sub = num1 - num2
    m = num1 * num2
    d = num1 / num2
    di = num1 // num2
    p = num1 ** num2
    rd = num1 % num2
    print('A soma dos dois é : \n {} \n a subtração é : \n {} \n o produto é : \n {} \n a divisão é :  \n {:.2f} \n a divisão inteira é : \n {} \n o resto da divisão é \n {}\n a potencia é : \n {} \n'.format(s, sub, m, d, di, rd, p ))
else:
    print('ta blz se ta ferrado comecando em 3, 2, 1 ')
    time.sleep(3)
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    pyautogui.write('eu sou um bobao e vou apartir de agora vou querer saber todas a interacoes de 2 numeros')

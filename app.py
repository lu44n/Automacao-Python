import pyautogui
from time import sleep

# Adicionar o usuário
pyautogui.click(958,540)
pyautogui.write('jhonatan')

sleep(1)

# Adicionar a senha
pyautogui.click(956,568)
pyautogui.write('123456')

sleep(1)

# Clicar no botão Entrar
pyautogui.click(867,598)

# Extrair cada produto do txt
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(683,528)
        pyautogui.write(produto)
        sleep(0.5)

        pyautogui.click(688,554)
        pyautogui.write(quantidade)
        sleep(0.5)

        pyautogui.click(687,579)
        pyautogui.write(preco)
        sleep(0.5)
        
        pyautogui.click(602,738)

        sleep(1)
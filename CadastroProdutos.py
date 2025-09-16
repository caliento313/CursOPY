import time
from multiprocessing.reduction import send_handle

import pyautogui
import pandas
from time import sleep
#defina o tempo de espera entre as aberturas dos comandos pyautogui

pyautogui.PAUSE = 0.7



# abrir sistema
pyautogui.press('win')
pyautogui.write('microsoft edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)
#print(pyautogui.position())
#cadastrar senha

pyautogui.click(x=32, y=312)
pyautogui.write('andrecaliento@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(3)
#cadstrar produtos
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=57, y=256)
    #print(tabela)

    codigo = tabela.loc[ linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca  = tabela.loc[linha,'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo =tabela.loc[linha,'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    preço_unitario = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preço_unitario)
    pyautogui.press('tab')
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    obs = str(tabela.loc[linha,'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)




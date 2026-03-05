# Passo a passo do programa

# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados dos produtos
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 para os outros produtos

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Passo 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#tempo para o site carregar
time.sleep(3)

#Passo 2
pyautogui.click(x=426, y=409)
pyautogui.write("kauaexemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("enter")

time.sleep(3)

#Passo 3
tabela_produtos = pandas.read_csv("produtos.csv")

#Passo 4
for linha in tabela_produtos.index:
    pyautogui.click(x=424, y=284)
    codigo = tabela_produtos.loc[linha, "codigo"]
    marca = tabela_produtos.loc[linha, "marca"]
    tipo = tabela_produtos.loc[linha, "tipo"]
    categoria = tabela_produtos.loc[linha, "categoria"]
    preco_unitario = tabela_produtos.loc[linha, "preco_unitario"]
    custo = tabela_produtos.loc[linha, "custo"]
    obs = tabela_produtos.loc[linha, "obs"]
    
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
    
print("✅ Todos os produtos foram cadastrados!")
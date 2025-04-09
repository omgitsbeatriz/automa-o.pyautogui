import pyautogui
import time
import pandas as pd

# Configura uma pausa padrão entre as ações do PyAutoGUI
pyautogui.PAUSE = 2

# Abre o navegador e acessa o site
pyautogui.press('win')                # Abre o menu iniciar
pyautogui.write('chrome')             # Digita "chrome"
pyautogui.press('enter')              # Abre o navegador
pyautogui.hotkey('ctrl', 'n')         # Abre uma nova janela
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')              # Acessa o link

# Aguarda o site carregar
time.sleep(5)

# Login no site
pyautogui.click(x=856, y=400)         # Clica no campo de e-mail
pyautogui.write('email.ficticio@gmail.com')  # Digita o e-mail
pyautogui.press('tab')                # Vai para o campo de senha
pyautogui.write('senhaficticia')      # Digita a senha
pyautogui.press('tab')                # Vai para o botão de login
pyautogui.press('enter')              # Realiza o login

# Leitura da planilha de produtos
tabela = pd.read_csv(r'produtos.csv')

# Preenche o formulário para cada produto
for linha in tabela.index:
    pyautogui.click(x=868, y=288)  # Clica no primeiro campo do formulário
    
    campos = [
            'codigo', 'marca', 'tipo', 'categoria',
            'preco_unitario', 'custo', 'obs'
        ]

    for campo in campos:
            valor = str(tabela.loc[linha, campo])
            pyautogui.write(valor)
            pyautogui.press('tab')

    pyautogui.press('enter')  # Envia o formulário
    time.sleep(1)
    pyautogui.press('home')   # Volta ao topo

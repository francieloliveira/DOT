from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time

# Função para verificar se o horário atual é um dos horários alvo
def verificar_horario(horarios_alvo):
    horario_atual = datetime.now().strftime("%H:%M:%S")
    print("Hora atual:", horario_atual)
    
    # Verifica se o horário atual é igual a um dos horários alvo
    if horario_atual in horarios_alvo:
        return True
    return False

service = Service('/Users/franciel/Desktop/workspace/chromedriver-mac-x64/chromedriver')

# Horários alvo
horarios_alvo = ["07:55:00", "15:34:00"]
executados_hoje = set()

# Loop infinito para ficar verificando o horário
while True:
    # Verifica se o horário atual é um dos horários alvo
    if verificar_horario(horarios_alvo):
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # Verifica se o horário já foi executado hoje
        if horario_atual not in executados_hoje:
            print(f"Horário alvo atingido. Executando o WebDriver...")

            # Executa o WebDriver e realiza as ações
            driver = webdriver.Chrome(service=service)

            # Carregar a página HTML local
            driver.get("file:///Users/franciel/Desktop/workspace/PythonForDataScience/DICON/pagina_teste.html")

            # Preencher o campo de Usuário
            usuario_input = driver.find_element(By.ID, "ext-135")  # ID do campo de usuário
            usuario_input.send_keys("2732559")

            # Preencher o campo de Senha
            senha_input = driver.find_element(By.ID, "ext-137")  # ID do campo de senha
            senha_input.send_keys("minhaSenha")

            # Clicar no botão de Marcação
            marcacao_button = driver.find_element(By.ID, "ext-139")  # ID do botão "Marcação"
            marcacao_button.click()

            # Aguardar o alert aparecer e capturá-lo
            time.sleep(2)  # Espera o alert aparecer
            alert = driver.switch_to.alert
            print(alert.text)  # Exibe o texto do alert no console
            alert.accept()  # Fecha o alert

            # Fechar o navegador após completar a ação
            driver.quit()

            # Adiciona o horário atual ao conjunto de horários executados hoje
            executados_hoje.add(horario_atual)

    # Verifica se já passamos para um novo dia e reseta os horários executados
    if len(executados_hoje) == len(horarios_alvo):
        if datetime.now().strftime("%H:%M:%S") == "00:00:00":
            executados_hoje.clear()

    # Espera 60 segundos antes de verificar novamente
    time.sleep(1)

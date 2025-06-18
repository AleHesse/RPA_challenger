import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_desafio():

    with webdriver.Chrome() as driver:

        driver.get("https://rpachallenge.com/?lang=EN")

        time.sleep(1)

        df = pd.read_excel('./challenge.xlsx', sheet_name="Sheet1")
        df.columns = df.columns.str.strip()  # remove espaços extras

        for index, row in df.iterrows(): # Observações:
                                         # index → índice da linha (pode ser 0, 1, 2…)
                                         # row → linha completa (como um dicionário)
                                         # Você acessa os campos como row["nome_da_coluna"]

            nome = row["First Name"]
            sobrenome = row["Last Name"]
            empresa = row["Company Name"]
            cargo = row["Role in Company"]
            endereco = row["Address"]
            email = row["Email"]
            fone = row["Phone Number"]

            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]').send_keys(nome)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]').send_keys(sobrenome)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]').send_keys(empresa)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]').send_keys(cargo)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]').send_keys(endereco)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]').send_keys(email)
            driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]').send_keys(fone)
            
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '.btn.uiColorButton').click()

            # Explicação do seletor CSS:
            # Usando By.CSS_SELECTOR (recomendado para múltiplas classes):
            # driver.find_element(By.CSS_SELECTOR, '.btn.uiColorButton').click()
            # O ponto (.) representa a classe.
            # .btn.uiColorButton encontra um elemento que tem as duas classes btn e uiColorButton.

            # Usando By.CLASS_NAME (só funciona com uma classe por vez):
            # driver.find_element(By.CLASS_NAME, "btn").click()
            # ⚠️ Mas isso só funciona se não houver outras classes com o mesmo nome.


        # time.sleep(5)

run_desafio()

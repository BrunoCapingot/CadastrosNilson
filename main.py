from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


def cadastrarDados(csvPath: str, siteLink: str) -> None:
    driver = webdriver.Edge()
    driver.get(siteLink)
    time.sleep(3)
    torre_em_cadastro = ''
    unidade_em_cadastro = ''
    lista_comparacao_de_final = ['14', '16', '18', '19', '17', '13']
    df = pd.read_excel(csvPath)
    for index, row in df.iterrows():
        identificadorUnidade = str(row['identificadorUnidade'])
        identificadorUnidade = identificadorUnidade.replace(' ', '')
        if  '/' in identificadorUnidade:
            torre_em_cadastro = 'B'
        else:
            torre_em_cadastro = 'A'

        ####Elemento Torre ####
        elemento = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div/input')
        time.sleep(0.3)
        elemento.click()
        time.sleep(0.3)
        elemento.clear()
        time.sleep(0.3)
        if '/' in str(identificadorUnidade):
            elemento.send_keys('B')
            pass
        else:
            elemento.send_keys('A')
        time.sleep(0.3)
        #### Elemento Unidade ####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div/input')
        time.sleep(0.3)
        elemento.click()
        time.sleep(0.3)
        elemento.clear()
        time.sleep(0.3)
        elemento.send_keys(identificadorUnidade)
        time.sleep(0.3)
        #### Fim Elemento Unidade####
        #### Elemento Quartos ####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div[4]/div/input')
        time.sleep(0.3)
        elemento.click()
        time.sleep(0.3)
        elemento.clear()
        time.sleep(0.3)
        if '/' in identificadorUnidade:
            data = identificadorUnidade.split('/')[0]
            print(data)
            if data.__len__() == 4:
                for numero_final_apartamento in lista_comparacao_de_final:
                    type_aparmento = '{}'.format(str(data[-2:]))
                    if numero_final_apartamento == type_aparmento:
                        elemento.send_keys(2)
                        break
                    else:
                        elemento.send_keys(1)
                        break
            elif data.__len__() == 3:
                for numero_final_apartamento in lista_comparacao_de_final:
                    type_aparmento = '{}'.format(str(data[-2:]))
                    if numero_final_apartamento == type_aparmento:
                        elemento.send_keys(2)
                        break
                    else:
                        elemento.send_keys(1)
                        break
        #### Fim Elemento Quartos####

        #### Elemento Andar####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div[5]/div/input')
        time.sleep(1)
        elemento.click()
        time.sleep(1)
        elemento.clear()
        time.sleep(1)
        if '/' in identificadorUnidade:
            data = identificadorUnidade.split('/')[0]
            print(data)
            if data.__len__() == 4:
                type_aparmento = '{}{}'.format(str(data[0]),str(data[1]))
                elemento.send_keys(type_aparmento)
            elif data.__len__() == 3:
                type_aparmento = '{}'.format(str(data[0]))
                elemento.send_keys(type_aparmento)
        time.sleep(0.3)
        #### Fim Elemento Andar####

        #### Elemento Tipo de Unidade####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div[6]/div/input')
        time.sleep(0.3)
        elemento.click()
        time.sleep(0.3)
        elemento.clear()
        time.sleep(0.3)
        if str(torre_em_cadastro) == 'A':
            elemento.send_keys(1)
        elif str(torre_em_cadastro) == 'B':
            elemento.send_keys(2)
        time.sleep(0.3)
        #### Fim Elemento Tipo de Unidade####
        #### Elemento Butao Cadastrar####
        elemento = driver.find_element(By.XPATH, '//form[@action="cls_new_unidade.php"]')
        elemento.submit()
        #### Fim Elemento Butao cadastrar####
        #### Elemento Tipo de Nome do Propietario####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[1]/form/div[1]/div[1]/div/input')
        nome_para_cadastro = row['Nome']
        time.sleep(1)
        elemento.click()
        time.sleep(1)
        elemento.clear()
        time.sleep(1)
        elemento.send_keys(nome_para_cadastro)
        time.sleep(1)
        #### Fim Elemento Tipo de Nome do Propietario####
        #### Elemento Tipo Unidade 2####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[1]/form/div[1]/div[3]/div/input')
        time.sleep(1)
        elemento.click()
        time.sleep(1)
        elemento.clear()
        time.sleep(1)
        elemento.send_keys(identificadorUnidade)
        time.sleep(1)
        #### Fim Elemento Unidade 2####
        #### Fim Elemento Cadastrar Proprietários####
        elemento = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[1]/form/input').submit()
        time.sleep(5)
        #### Fim Elemento Botao Cadastrar Proprietários####

if __name__ == '__main__':
    cadastrarDados(csvPath=r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Relatorio geral de clientes 18-10-2023.xlsx',siteLink='http://plannextsistema.com.br/frm_unidade.php?transaction=0')
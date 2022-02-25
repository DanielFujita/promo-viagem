from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import promocoes_smiles

def cotacao_milhas():
        
    driver = webdriver.Chrome(ChromeDriverManager().install())

    URL = 'https://www.hotmilhas.com.br'

    driver.get(URL)
    time.sleep(3)
    # driver.maximize_window()

    programas = [1, 3]

    for opcao in programas:

        # --- Hotmilhas SMILES
        # Preenche email
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/form/div[1]/div[1]/input").send_keys("teste@teste.com")

        # Seleciona o programa
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]").click()
        driver.find_element_by_xpath(
            f"/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[{opcao}]").click()

        # Seleciona qtd
        time.sleep(3)
        if opcao == 1:
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[2]/div[1]").click()
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[2]/div[2]/div[2]/ul/li[81]").click()
        else:
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[4]/div[1]").click()
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[4]/div[2]/div[2]/ul/li[81]").click()
        # time.sleep(2)

        # Envia
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button").click()

        # Nova cotação
        if opcao == 1:
            time.sleep(3)
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/div/div[1]/div/a[1]").click()
            time.sleep(3)
        else:
            driver.quit()
            promocoes_smiles.promocao_smiles()
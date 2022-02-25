import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def promocao_smiles():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    URL = 'https://www.smiles.com.br/promocao'

    driver.get(URL)
    time.sleep(5)
    driver.maximize_window()

    def S(X): return driver.execute_script(
        'return document.body.parentNode.scroll'+X)

    # May need manual adjustment
    driver.set_window_size(S('Width'), S('Height'))
    curr_date = datetime.today().strftime('%Y-%m-%d')
    file_name = "smiles"+curr_date + ".png"
    driver.find_element_by_tag_name('body').screenshot(file_name)

    driver.quit()
    #
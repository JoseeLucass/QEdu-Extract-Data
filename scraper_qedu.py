from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time


driver = webdriver.Chrome()

workbook = Workbook()
sheet = workbook.active
sheet.title = "Dados Raspados"
sheet.append(["Nome da Escola", "Endereço", "Telefone", 
              "Código INEP", "Localização", "Dependência Administrativa", "Etapas"])

try:
    driver.get("https://qedu.org.br/")
    time.sleep(3)
    
    try:
        welcome_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[1]/a'))
        )
        welcome_button.click()
        time.sleep(2)
    except:
        print("Nenhum popup de 'Bem-vindo' detectado.")
    
    # Lista de termos de pesquisa
    
    search_terms = [
  "17020603", "17020581", "17051002", "17045045", "17006449", "17001013", "17050545", "17069009", "17010926", "17021103",
  "17007828", "17016231", "17054133", "17034574", "17012295", "17012350", "17018307", "17021367", "17007895", "17018510",
  "17027993", "17013372", "17021588", "17038359", "17052360", "17029163", "17028795", "17044081", "17002370", "17029449",
  "17014530", "17030439", "17043255", "17034620", "17030773", "17026300", "17026547", "17026369", "17002648", "17043867",
  "17019400", "17035449", "17009707", "17023122", "17069203", "17035830", "17019729", "17051770", "17051061", "17024790",
  "17025117", "17045185", "17003393", "17048249", "17036895", "17002877", "17003016", "17039185", "17003555", "17040035",
  "17049644", "17053757", "17038855", "17037921", "17020824", "17026946", "17052432", "17047862", "17004209", "17004314",
  "17004799", "17047781", "17004322"
]



    for search_text in search_terms: 
        try:
            # Localizar a barra de pesquisa e realizar a busca
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-element"]'))
            )
            search_box.clear()
            search_box.send_keys(search_text)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            
            result_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="busca-header"]/div/div[2]/div[4]/div[2]/div[1]/a'))
            )
            result_link.click()
            print(f"Pesquisou por '{search_text}' e clicou no resultado.")
            time.sleep(5)
            
            # Raspar o nome da escola
            nome_escola = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/section/div/div[2]/div[1]/h1/a'))
            ).text
            
            # Raspar dados principais da página
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/main/section/summary'))
                )
                html_content = element.get_attribute('outerHTML')
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Raspar os itens da lista
                list_items = soup.find_all("li")
                endereco, telefone, codigo_inep, localizacao, dependencia_adm, etapas = "", "", "", "", "", ""
                
                # Raspar o Endereço 
                try:
                    endereco_element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/main/section/summary/ul/li[1]/div")
                    endereco = endereco_element.text.strip() if endereco_element else "Não encontrado"
                except Exception as e:
                    print(f"Erro ao raspar o endereço: {e}")
                    endereco = "Não encontrado"
                
                # Raspar o Telefone 
                try:
                    telefone_element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/main/section/summary/ul/li[2]/div/a")
                    telefone = telefone_element.text.strip() if telefone_element else "Não encontrado"
                except Exception as e:
                    print(f"Erro ao raspar o telefone: {e}")
                    telefone = "Não encontrado"
                
                print(f"Dados para '{search_text}':")
                for item in list_items:
                    text = item.text.strip()
                    if "Código INEP" in text:
                        codigo_inep = text.replace("Código INEP: ", "")
                    elif "Localização" in text:
                        localizacao = text.replace("Localização: ", "")
                    elif "Dependência Adm." in text:
                        dependencia_adm = text.replace("Dependência Adm.: ", "")
                    elif "Etapas" in text:
                        etapas = text.replace("Etapas: ", "")
                
                # Adicionar os dados na planilha
                sheet.append([nome_escola, endereco, telefone, codigo_inep, localizacao, dependencia_adm, etapas])
            
            except Exception as e:
                print(f"Erro ao localizar ou raspar o elemento para '{search_text}': {e}")
        
            driver.back()
            time.sleep(3)
        
        except Exception as e:
            print(f"Erro durante a busca por '{search_text}': {e}") 
            driver.back()
            time.sleep(3)
        
finally:
    
    workbook.save("dados_raspados_TO.xlsx")
    print("Dados salvos no arquivo 'dados_raspados.xlsx'.")
    driver.quit()

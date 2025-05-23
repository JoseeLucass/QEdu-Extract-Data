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
  "15065790", "15066037", "15067041", "15064417", "15066282", "15170713", "15576396", "15066606", "15066789", "15064654",
  "15116190", "15079481", "15079465", "15078981", "15079910", "15155900", "15079430", "15079074", "15078388", "15080102",
  "15078205", "15543870", "15024032", "15023168", "15022854", "15022790", "15549399", "15579549", "15005739", "15145166",
  "15005828", "15544583", "15558029", "15005356", "15562832", "15544737", "15006344", "15006719", "15005550", "15016773",
  "15017648", "15017303", "15017109", "15148025", "15105580", "15104761", "15575357", "15584380", "15559998", "15211045",
  "15105610", "15105563", "15105695", "15568806", "15538036", "15024385", "15024237", "15141969", "15537773", "15550702",
  "15538133", "15142043", "15539555", "15515613", "15034380", "15571955", "15035662", "15034666", "15582671", "15542947",
  "15108341", "15558614", "15105075", "15055973", "15055264", "15540049", "15521532", "15055370", "15151220", "15151131",
  "15567400", "15055531", "15087573", "15543293", "15539326", "15018920", "15019128", "15067491", "15067262", "15067386",
  "15560309", "15067254", "15067475", "15036367", "15143155", "15515753", "15036391", "15036120", "15042928", "15040496",
  "15042510", "15140759", "15040569", "15042880", "15040860", "15521125", "15042790", "15038505", "15166813", "15014010",
  "15014479", "15147878", "15015092", "15200604", "15548988", "15043665", "15537412", "15559190", "15559203", "15576078",
  "15519902", "15106276", "15106497", "15543129", "15106195", "15106322", "15126650", "15564487", "15545385", "15025535",
  "15025543", "15677737", "15024954", "15563243", "15025454", "15044645", "15028941", "15028747", "15098214", "15544818",
  "15098141", "15570550", "15547647", "15070417", "15072207", "15587878", "15069265", "15547701", "15070255", "15583988",
  "15520595", "15069583", "15069222", "15531155", "15069710", "15068390", "15069290", "15580881", "15165868", "15126366",
  "15556573", "15059995", "15536734", "15089258", "15553396", "15046532", "15045811", "15046524", "15045820", "15577520",
  "15582345", "15582302", "15578798", "15165396", "15582400", "15578747", "15520137", "15582299", "15048667", "15048780",
  "15048543", "15545156", "15134997", "15134520", "15081818", "15081044", "15081516", "15157580", "15565360", "15560660",
  "15026981", "15027090", "15006867", "15542360", "15159728", "15586090", "15048985", "15588491", "15586081", "15550362",
  "15116948", "15125203", "15137066", "15150569", "15135748", "15135926", "15135608", "15090086", "15089720", "15089835",
  "15089797", "15586677", "15118487", "15118320", "15118665", "15118410", "15019594", "15020070", "15530167", "15060942",
  "15523160", "15073963", "15073092", "15072916", "15074285", "15074668", "15554880", "15073238", "15573745", "15046842",
  "15168743", "15157024", "15090493", "15090680", "15090736", "15092089", "15538729", "15092178", "15091007", "15091856",
  "15538877", "15165000", "15091481", "15092275", "15091724", "15564096", "15101622", "15101185", "15573290", "15583260",
  "15104532", "15101428", "15100464", "15525791", "15530655", "15100383", "15101142", "15101533", "15101029", "15101037",
  "15583244", "15560023", "15111938", "15112209", "15547965", "15152090", "15104362", "15000265", "15075745", "15075435",
  "15075710", "15529606", "15536700", "15092976", "15128792", "15546411", "15555046", "15166104", "15577406", "15050416",
  "15165949", "15051269", "15050343", "15050009", "15051102", "15050092", "15051544", "15051625", "15579093", "15168115",
  "15021173", "15020959", "15566650", "15077004", "15082938", "15084019", "15568873", "15082423", "15083144", "15083004",
  "15084213", "15083624", "15540138", "15589650", "15013669", "15572609", "15007782", "15545679", "15545717", "15555224",
  "15007855", "15008339", "15572099", "15172945", "15007677", "15555232", "15583619", "15201007", "15153843", "15560392",
  "15030300", "15542114", "15093190", "15574296", "15061680", "15061299", "15061361", "15061736", "15564320", "15570851",
  "15002233", "15002454", "15526623", "15001946", "15104290", "15002624", "15002160", "15077667", "15077039", "15004368",
  "15003400", "15003914", "15004406", "15003000", "15556018", "15093859", "15093972", "15587339", "15109143", "15158349",
  "15533654", "15108333", "15108503", "15158306", "15550419", "15541029", "15118991", "15569594", "15540960", "15540944",
  "15119459", "15553574", "15104141", "15125866", "15574458", "15166619", "15160467", "15554589", "15577309", "15021645",
  "15021971", "15141365", "15021556", "15021947", "15568644", "15574890", "15141608", "15018032", "15527700", "15010856",
  "15097463", "15009645", "15542939", "15010457", "15152812", "15010600", "15062201", "15062252", "15096424", "15131360",
  "15131130", "15118045", "15104176", "15169456", "15103897", "15154475", "15052346", "15052540", "15052249", "15161773",
  "15033031", "15588742", "15159876", "15561836", "15047326", "15047016", "15558193", "15046729", "15094294", "15094529",
  "15063313", "15062848", "15062929", "15524655", "15156770", "15011372", "15013260", "15140849", "15013626", "15147991",
  "15012115", "15540650", "15015955", "15567044", "15011712", "15589404", "15013049", "15011232", "15170080", "15015084",
  "15011690", "15589919", "15011674", "15063658", "15048365", "15048047", "15047997", "15047890", "15048322", "15052915",
  "15052923", "15522512", "15095550", "15094901", "15081257", "15535592", "15138587", "15121879", "15573028", "15122018",
  "15064174", "15064204", "15064000", "15133273", "15133117", "15053440", "15053679", "15053563", "15142094", "15096149",
  "15095843", "15096912", "15027864", "15028135", "15028259", "15167410", "15109178", "15584607", "15109194", "15164500",
  "15033783", "15084647", "15084884", "15549127", "15004864", "15004830", "15219143", "15169316", "15587045", "15120112",
  "15120120", "15058913", "15057348", "15058026", "15104524", "15104443", "15115739", "15120490", "15524779", "15214010",
  "15159175", "15109844", "15054381", "15054357", "15098524", "15098435", "15098273", "15111040", "15105920", "15111270",
  "15134296"
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
    
    workbook.save("dados_raspados_PA.xlsx")
    print("Dados salvos no arquivo 'dados_raspados.xlsx'.")
    driver.quit()

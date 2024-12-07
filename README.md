# Web Scraper para Dados de Escolas no QEdu

Este script realiza a raspagem de dados de escolas no site [QEdu](https://qedu.org.br) com base em termos de pesquisa fornecidos. Ele extrai informações como nome da escola, endereço, telefone, código INEP, localização, dependência administrativa e etapas de ensino.

---

##  Funcionalidades

- **Automação com Selenium**: O script navega no site do QEdu, realiza buscas por códigos específicos e extrai os dados.
- **Extração de Dados com BeautifulSoup**: Obtém informações detalhadas a partir do conteúdo HTML da página.
- **Armazenamento em Excel**: Os dados raspados são salvos em uma planilha Excel (`dados_raspados.xlsx`).

---

##  Requisitos

Antes de executar o script, certifique-se de que seu ambiente atenda aos seguintes requisitos:

1. **Python 3.x** instalado.
2. **Bibliotecas Python necessárias**:
   - `selenium`
   - `beautifulsoup4`
   - `openpyxl`
3. **Driver do Selenium**: Baixe o ChromeDriver compatível com a versão do seu navegador e adicione-o ao PATH do sistema.

### Instalação de Dependências
 
Execute o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install selenium beautifulsoup4 openpyxl  
---
 
## Como Usar

1. **Clone ou Baixe o Repositório**: Faça o download ou clone este repositório para o seu computador.

2. **Configure o Script**:
   - Altere os termos de pesquisa e as configurações de busca no script conforme necessário.
   - Certifique-se de que o **ChromeDriver** está corretamente configurado e compatível com a versão do seu navegador.

3. **Execute o Script**: Rode o script Python para iniciar a raspagem de dados:

    ```bash
    python scraper_qedu.py
    ```

4. **Resultado**: O script gerará um arquivo Excel chamado `dados_raspados.xlsx` com os dados das escolas encontradas.

---

## Estrutura do Script

- **scraper_qedu.py**: Arquivo principal do script que realiza a automação de busca e extração.
- **dados_raspados.xlsx**: Arquivo Excel gerado contendo os dados das escolas.

---

## Considerações

- O tempo de execução pode variar dependendo do número de resultados e da velocidade de conexão com a internet.
- O QEdu pode alterar sua estrutura de página, o que pode afetar o funcionamento do script. Atualizações regulares podem ser necessárias para manter a compatibilidade.
 

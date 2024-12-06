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

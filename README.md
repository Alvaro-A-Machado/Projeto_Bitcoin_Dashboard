# Bitcoin Tracker Dashboard

Um ecossistema automatizado de extração, armazenamento e visualização de dados financeiros, construído de ponta a ponta com Python.

**Acesse o painel em tempo real:** [Bitcoin Dashboard no Streamlit](https://bitcoindashboard-p001.streamlit.app)

---

## Sobre o Projeto
Este projeto foi desenvolvido para consolidar os fundamentos de **Engenharia e Ciência de Dados**, simulando um ambiente real de produção. A aplicação não é estática; ela opera através de um pipeline CI/CD autônomo (ETL) que coleta, armazena e exibe o histórico de preços do Bitcoin (em Dólar e Real) sem qualquer intervenção humana.

## Tecnologias e Ferramentas
* **Linguagem:** Python 3
* **Manipulação de Dados:** `pandas`
* **Banco de Dados:** SQLite3 (`banco_join.db`)
* **Visualização Web:** Streamlit
* **Coleta de Dados:** API Pública da Blockchain.info via `requests`
* **Automação (CI/CD):** GitHub Actions
* **Deploy de Cloud:** Streamlit Community Cloud

## Arquitetura e Fluxo de Dados
A infraestrutura deste projeto foi desenhada para ser 100% autônoma na nuvem:

1. **Gatilho Temporal:** Diariamente, o GitHub Actions inicializa um servidor Linux temporário na nuvem.
2. **Extração:** O script `Missao_5.py` é executado, consumindo a API da Blockchain.info para contornar bloqueios geográficos e capturar a cotação exata do segundo.
3. **Armazenamento:** Os dados são estruturados e inseridos numa tabela relacional dentro do banco de dados SQLite.
4. **Entrega Contínua (Push):** O GitHub Actions realiza automaticamente o *commit* do banco atualizado de volta para o repositório principal.
5. **Visualização:** O Streamlit Cloud detecta a atualização no banco de dados e recarrega o dashboard, alimentando o gráfico temporal de comparação (BRL vs USD) para o usuário final.

## Como Executar Localmente

Caso deseje clonar e rodar o projeto na sua máquina:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Alvaro-A-Machado/Projeto_Bitcoin_Dashboard.git](https://github.com/Alvaro-A-Machado/Projeto_Bitcoin_Dashboard.git)

2. Instale as dependencias:
   ```bash
   pip install -r requirements.txt
3. Execute o script para extrair a cotação do momento e salvar no banco local:
   ```bash
   python Missao_5.py
4. Inicie o painel interativo:
   ```bash
   python -m streamlit run dashboard.py

### Autor

**Álvaro A. Machado**

Projeto construído como demonstração prática de habilidades em SQL, Automação Cloud e Desenvolvimento Web com Python.

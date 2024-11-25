# **Desafio-Selenium**

![Desafio Selenium](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

Um projeto desenvolvido para automatizar tarefas, analisar dados e gerar relatório utilizando Selenium, análise de arquivos CSV, gráficos com Matplotlib, e envio de emails com relatórios em PDF. 🚀

---

## **Visão Geral**
Este projeto combina automação web com manipulação de dados e geração de relatórios. Com ele, é possível:

1. **Automatizar a coleta de dados** de um site de citações.
2. **Gerar arquivos CSV** com informações do site.
3. **Analisar os dados coletados**, como autores mais recorrentes e tags mais populares.
4. **Criar relatórios visuais** com gráficos de pizza.
5. **Enviar resultados por email** com o CSV e o PDF anexados.

---

## **Funcionalidades**
1. **Automação com Selenium**:
   - Acessa um site de citações.
   - Coleta citações, autores e tags.
   - Organiza os dados coletados em um arquivo CSV.

2. **Geração de Arquivos CSV**:
   - Cria um arquivo estruturado contendo as informações coletadas.

3. **Análise de Dados**:
   - Identifica o autor mais citado.
   - Mostra a tag mais utilizada.
   - Conta o número total de citações.

4. **Geração de Relatórios PDF**:
   - Cria gráficos de pizza para visualização dos autores mais citados e tags mais utilizadas.
   - Consolida as informações em um PDF completo.

5. **Envio de Emails**:
   - Envia o relatório em PDF e o arquivo CSV por email, com suporte a anexos.

---
## **Como Usar**

### **Executar o Projeto**

1. **Configure as credenciais de email no arquivo `envioEmail.py`:**
   Abra o arquivo `src/envioEmail.py` e insira o seu email e senha:
   ```python
   sender_email = "seuemail@gmail.com"
   sender_password = "suasenha"

2. **Execute o arquivo principal:** 
  Rode o script principal para executar todo o fluxo do projeto:
 
  `python src/run.py`

3. **Saída Gerada após a execução do script:**

- Os dados coletados serão salvos no arquivo assets/citacoes.csv.
- O relatório com gráficos será salvo no arquivo assets/resultado_analise.pdf.
- Um email será enviado ao destinatário configurado, contendo o PDF e o CSV como anexos.

## **Estrutura do Projeto**
```plaintext
Desafio-Selenium/
│
├── src/                   # Código-fonte principal
│   ├── criarCSV.py        # Criação do arquivo CSV
│   ├── envioEmail.py      # Envio de email com anexos
│   ├── gerarPDF.py        # Geração do relatório em PDF
│   ├── leitorCSV.py       # Leitura e análise dos dados do CSV
│   ├── script.py          # Automação com Selenium
│
├── run.py                 # Ponto de entrada principal
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação do projeto

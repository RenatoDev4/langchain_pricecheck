# Projeto Busca de Melhores Preços

Link do aplicativo : https://langchainpricecheck.streamlit.app/

## Descrição

Este é um projeto que busca os melhores preços de um produto escolhido pelo usuário. A aplicação utiliza a API do Google para realizar a busca e um modelo de linguagem da OpenAI para analisar os resultados. O usuário recebe uma resposta contendo o menor preço encontrado e um link direto para o produto.

## Funcionalidades

1. **Busca de Preços:** A aplicação permite que o usuário especifique o produto desejado para buscar os melhores preços online.

2. **Integração com API do Google:** Utilizando a API do Google, o projeto realiza a busca pelos preços do produto especificado.

3. **Análise com Modelo de Linguagem da OpenAI:** Os resultados da busca são analisados por um modelo de linguagem da OpenAI para identificar e extrair as informações relevantes sobre o menor preço encontrado.

4. **Resposta ao Usuário:** O usuário recebe uma resposta clara, contendo o menor preço identificado e um link direto para o produto.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone git@github.com:RenatoDev4/langchain_pricecheck.git

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

3. **Configuração da API do Google:** No meu caso usei o https://serpapi.com/ e então obtenha as credenciais da API e configure-as como uma váriavel de ambiente.

4. **Configuração do Modelo de Linguagem da OpenAI:** Obtenha as credenciais ou chave de API da OpenAI e configure-as e configure-as como uma váriavel de ambiente.

5. **Execute o projeto:**

   ```bash
   streamlit run main.py

## Configuração

1. **Váriaveis de ambiente:**

   ```bash
   OPENAI_API_KEY="SuaChaveAqui"
   SERPAPI_KEY="SuaChaveAqui"

Configure as credenciais da API do Google e da OpenAI como uma váriavel de ambiente, como por exemplo em um arquivo .env


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para discutir novas funcionalidades, relatar bugs ou enviar um pull request.

## Licença

Este projeto está licenciado sob a **Licença MIT.**

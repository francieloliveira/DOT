Se você deseja utilizar o `BeautifulSoup` para realizar o web scraping, ele é ideal para extrair dados de uma página HTML já carregada. No entanto, o `BeautifulSoup` não consegue interagir com a página da mesma forma que o Selenium (como preencher formulários ou clicar em botões). Para simular uma requisição que submete um formulário, seria necessário usar a biblioteca `requests`.

Neste caso, o `BeautifulSoup` será útil se você já tiver o conteúdo HTML da página depois de realizar a requisição (que poderia ser feita com `requests`). No entanto, como o formulário envolve o envio de uma senha e outras interações dinâmicas, essa parte seria gerida por `requests`.

Aqui está um exemplo básico usando `requests` e `BeautifulSoup` para coletar o conteúdo de uma página. No entanto, para realizar a automação de login e o envio do formulário, precisamos enviar uma requisição POST simulando os dados de login.

### Exemplo com `requests` e `BeautifulSoup`:

```python
import requests
from bs4 import BeautifulSoup

# URL da página de login
url = 'https://cliente.apdata.com.br/dicon/'

# Dados de login (preencha com seus dados)
login_data = {
    'matricula': '2732559',  # Coloque o nome correto do campo no formulário
    'senha': 'sua_senha_aqui'  # Substitua pela senha
}

# Headers para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

# Realize a requisição POST para enviar os dados de login
with requests.Session() as s:
    response = s.post(url, data=login_data, headers=headers)
    
    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML retornado
        soup = BeautifulSoup(response.content, 'html.parser')

        # Aqui você pode fazer a extração do conteúdo necessário
        print(soup.prettify())
    else:
        print("Falha ao acessar a página.")
```

### Passos:
1. **Instalar BeautifulSoup e Requests**:
   ```bash
   pip install beautifulsoup4 requests
   ```

2. **Identificar os campos corretos**: Você precisa verificar no formulário HTML quais são os `name` ou `id` corretos para os campos de `matrícula` e `senha`. Eles podem ser diferentes do XPath que você mencionou. O código acima usa `'matricula'` e `'senha'`, mas isso deve ser ajustado conforme os identificadores corretos no HTML da página.

### Limitações:
- **Interação Dinâmica**: Como o site pode usar JavaScript para tratar a submissão do formulário ou outras interações dinâmicas, o `requests` sozinho pode não ser suficiente. Nesse caso, `Selenium` seria mais apropriado.
- **Autenticação e Cookies**: Se o site usa cookies ou tokens de autenticação (como CSRF tokens), você precisará incluir isso na requisição para simular o comportamento de um navegador real.

Se o site for muito dinâmico e baseado em JavaScript, realmente a abordagem com Selenium seria mais direta.
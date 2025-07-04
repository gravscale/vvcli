# vvcli
A VVCLI permite que usuários autentiquem para acessar contas e contratos usando SDK ou CLI, além de gerenciar contratos de Armazenamento de Objetos. Com foco na criação de credenciais S3 para usuários e subusuários, a solução simplifica o gerenciamento de recursos através de uma experiência integrada e intuitiva.

## Requisitos
Python 3.8+

## Instalação
### Instalação via pip

Para instalar diretamente do repositório:

```sh
  pip install git+https://github.com/gravscale/vvcli
```
(em alguns casos pode precisar de permissão root: `sudo pip install git+https://github.com/gravscale/vvcli`)

Teste no terminal:
```sh
  vvcli --help
```

### Instalação via Setuptools
Instale usando [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
  python setup.py install --user
```
(ou `sudo python setup.py install` para instalar para todos usuários)


## Documentação 
Todos os recursos do SDK e CLI utilizam a API pública da Under: 
```
https://api.under.com.br/api/v1
```
---
**Fluxo de Autenticação CLI**:
1. Gere token na plataforma Under
2. Configure localmente:
   ```bash
   vvcli auth configure -t "API_TOKEN"
   ```
3. Valide com:
   ```bash
   vvcli auth info
   ```
**Documentação Detalhada CLI**:
- [CLI (Command line interface)](vvcli/README.md)

---

**Exemplo Prático SDK**:
```python
import vvcli_sdk
from vvcli_sdk.rest import ApiException
from pprint import pprint
import os

# Configuração básica
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/api/v1"
)

# Configuração de autenticação
configuration = vvcli_sdk.Configuration(
    access_token = os.environ["API_TOKEN"]
)

# Exemplo de uso da API
with vvcli_sdk.ApiClient(configuration) as api_client:
    api_instance = vvcli_sdk.AccountApi(api_client)
    try:
        api_response = api_instance.get_account()
        print("Resposta da API:\n")
        pprint(api_response)
    except ApiException as e:
        print("Erro na chamada da API: %s\n" % e)
```

**Documentação Detalhada SDK**:
- [SDK (Software Development Kit)](vvcli_sdk/README.md)


## Autor
Gravscale
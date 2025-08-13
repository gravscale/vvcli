
## SDK (Software Development Kit)

Após instalação, utilize o SDK com:

```python
import vvcli_sdk
from vvcli_sdk.rest import ApiException
from pprint import pprint
import os

# Configuração básica
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
)

# Configuração de autenticação
configuration = vvcli_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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

## Documentação dos Endpoints da API

Todos os endpoints são relativos a *https://api.under.com.br/v1*

Classe | Método | Requisição | Descrição
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_account**](docs/AccountApi.md#get_account) | **GET** /account/ | Obter Conta
*AccountApi* | [**list_accounts**](docs/AccountApi.md#list_accounts) | **GET** /account/all | Listar Todas as Contas
*AccountApi* | [**list_contracts**](docs/AccountApi.md#list_contracts) | **GET** /account/contracts | Listar Contratos
*AuthenticationApi* | [**info**](docs/AuthenticationApi.md#info) | **GET** /auth/info | Informações do Usuário Autenticado
*ObjectStorageApi* | [**create_client_user**](docs/ObjectStorageApi.md#create_client_user) | **POST** /object-storage/user | Criar Usuário S3 para Object Storage
*ObjectStorageApi* | [**create_subuser**](docs/ObjectStorageApi.md#create_subuser) | **POST** /object-storage/subuser | Criar Subusuário para Object Storage
*ObjectStorageApi* | [**get_client_user**](docs/ObjectStorageApi.md#get_client_user) | **GET** /object-storage/user | Obter Usuário em uso Object Storage
*ObjectStorageApi* | [**get_subusers**](docs/ObjectStorageApi.md#get_subusers) | **GET** /object-storage/subuser | Obter Subusuários em uso Object Storage

## Documentação dos Modelos

- [AccessPermissions](docs/AccessPermissions.md)
- [AccountSchema](docs/AccountSchema.md)
- [AuthInfoSchema](docs/AuthInfoSchema.md)
- [ContractSchema](docs/ContractSchema.md)
- [CreateSubUserObjStorageSchema](docs/CreateSubUserObjStorageSchema.md)
- [CredentialKey](docs/CredentialKey.md)
- [GetSubUserObjStorageSchema](docs/GetSubUserObjStorageSchema.md)
- [GetUserObjStorageSchema](docs/GetUserObjStorageSchema.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [NewSubUserObjStorageSchema](docs/NewSubUserObjStorageSchema.md)
- [NewUserObjStorageSchema](docs/NewUserObjStorageSchema.md)
- [PageAccountSchema](docs/PageAccountSchema.md)
- [PageContractSchema](docs/PageContractSchema.md)
- [PageGetSubUserObjStorageSchema](docs/PageGetSubUserObjStorageSchema.md)
- [ValidationError](docs/ValidationError.md)
- [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)

## Autor
Gravscale
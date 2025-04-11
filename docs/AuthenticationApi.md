# vvcli_sdk.AuthenticationApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_token**](AuthenticationApi.md#api_token) | **POST** /auth/token | Authenticate Api Token
[**info**](AuthenticationApi.md#info) | **GET** /auth/info | Authenticated User Information
[**refresh_token**](AuthenticationApi.md#refresh_token) | **POST** /auth/refresh | Refresh Access Token
[**sign_in**](AuthenticationApi.md#sign_in) | **POST** /auth/sign-in | Sign In
[**sign_up**](AuthenticationApi.md#sign_up) | **POST** /auth/sign-up | Sign Up


# **api_token**
> AuthorizationSchema api_token(token)

Authenticate Api Token

### Example


```python
import vvcli_sdk
from vvcli_sdk.models.authorization_schema import AuthorizationSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api/public
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api/public"
)


# Enter a context with an instance of the API client
with vvcli_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vvcli_sdk.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Authenticate Api Token
        api_response = api_instance.api_token(token)
        print("The response of AuthenticationApi->api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**AuthorizationSchema**](AuthorizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> AuthInfoSchema info()

Authenticated User Information

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.auth_info_schema import AuthInfoSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api/public
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = vvcli_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with vvcli_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vvcli_sdk.AuthenticationApi(api_client)

    try:
        # Authenticated User Information
        api_response = api_instance.info()
        print("The response of AuthenticationApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthInfoSchema**](AuthInfoSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> AuthorizationSchema refresh_token(refresh_token)

Refresh Access Token

### Example


```python
import vvcli_sdk
from vvcli_sdk.models.authorization_schema import AuthorizationSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api/public
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api/public"
)


# Enter a context with an instance of the API client
with vvcli_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vvcli_sdk.AuthenticationApi(api_client)
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Refresh Access Token
        api_response = api_instance.refresh_token(refresh_token)
        print("The response of AuthenticationApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | 

### Return type

[**AuthorizationSchema**](AuthorizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_in**
> AuthorizationSchema sign_in(login_schema)

Sign In

<p>Este endpoint é dedicado à autenticação dos usuários na API do serviço de contratação de servidores bare metal. Para realizar a autenticação, não são necessários parâmetros de consulta ou cabeçalho específicos. No entanto, espera-se um corpo de requisição do tipo \"application/json\" contendo um esquema JSON com os campos obrigatórios \"email\" e \"password\", ambos do tipo \"string\".</p>     <p>Os dados de autenticação devem ser fornecidos de maneira segura e estruturada no corpo da requisição para garantir a verificação correta da identidade do usuário.</p>     <p>Além disso, são definidos dois códigos de resposta HTTP para este endpoint, indicando diferentes situações ou resultados possíveis durante o processo de autenticação.</p>

### Example


```python
import vvcli_sdk
from vvcli_sdk.models.authorization_schema import AuthorizationSchema
from vvcli_sdk.models.login_schema import LoginSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api/public
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api/public"
)


# Enter a context with an instance of the API client
with vvcli_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vvcli_sdk.AuthenticationApi(api_client)
    login_schema = vvcli_sdk.LoginSchema() # LoginSchema | 

    try:
        # Sign In
        api_response = api_instance.sign_in(login_schema)
        print("The response of AuthenticationApi->sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_schema** | [**LoginSchema**](LoginSchema.md)|  | 

### Return type

[**AuthorizationSchema**](AuthorizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up**
> sign_up(login_schema)

Sign Up

<p>Este endpoint destina-se ao processo de registro de novos clientes na API do serviço de contratação de servidores bare metal. Durante a chamada deste endpoint, não são requeridos parâmetros de consulta ou cabeçalho específicos. No entanto, é fundamental fornecer um corpo de requisição no formato \"application/json\" contendo um esquema JSON estruturado.</p>     <p>No corpo da requisição, são esperados os campos obrigatórios \"email\" e \"password\", ambos do tipo \"string\". É essencial que as informações fornecidas sigam o formato adequado para garantir a correta criação do novo cadastro de cliente.</p>     <p>Ao utilizar este endpoint, é possível efetuar o registro de novos clientes de maneira eficiente e segura, permitindo a expansão da base de usuários do serviço de servidores bare metal.</p>

### Example


```python
import vvcli_sdk
from vvcli_sdk.models.login_schema import LoginSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api/public
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api/public"
)


# Enter a context with an instance of the API client
with vvcli_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vvcli_sdk.AuthenticationApi(api_client)
    login_schema = vvcli_sdk.LoginSchema() # LoginSchema | 

    try:
        # Sign Up
        api_instance.sign_up(login_schema)
    except Exception as e:
        print("Exception when calling AuthenticationApi->sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_schema** | [**LoginSchema**](LoginSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


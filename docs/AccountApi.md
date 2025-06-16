# vvcli_sdk.AccountApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountApi.md#get_account) | **GET** /account/ | Get Account
[**list_accounts**](AccountApi.md#list_accounts) | **GET** /account/all | List All Accounts
[**list_contracts**](AccountApi.md#list_contracts) | **GET** /account/contracts | List Contracts


# **get_account**
> AccountSchema get_account(uuid=uuid, client_id=client_id)

Get Account

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.account_schema import AccountSchema
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
    api_instance = vvcli_sdk.AccountApi(api_client)
    uuid = 'uuid_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)

    try:
        # Get Account
        api_response = api_instance.get_account(uuid=uuid, client_id=client_id)
        print("The response of AccountApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 

### Return type

[**AccountSchema**](AccountSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> PageAccountSchema list_accounts(page=page, size=size)

List All Accounts

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.page_account_schema import PageAccountSchema
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
    api_instance = vvcli_sdk.AccountApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List All Accounts
        api_response = api_instance.list_accounts(page=page, size=size)
        print("The response of AccountApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageAccountSchema**](PageAccountSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contracts**
> PageContractSchema list_contracts(uuid=uuid, client_id=client_id, product=product, contract_key=contract_key, page=page, size=size)

List Contracts

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.page_contract_schema import PageContractSchema
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
    api_instance = vvcli_sdk.AccountApi(api_client)
    uuid = 'uuid_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    product = 'product_example' # str |  (optional)
    contract_key = 'contract_key_example' # str |  (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List Contracts
        api_response = api_instance.list_contracts(uuid=uuid, client_id=client_id, product=product, contract_key=contract_key, page=page, size=size)
        print("The response of AccountApi->list_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **contract_key** | **str**|  | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageContractSchema**](PageContractSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# vvcli_sdk.ObjectStorageApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_user**](ObjectStorageApi.md#create_client_user) | **POST** /object-storage/user | Create Client User Object Storage
[**create_subuser**](ObjectStorageApi.md#create_subuser) | **POST** /object-storage/subuser | Create Subuser Object Storage
[**get_client_user**](ObjectStorageApi.md#get_client_user) | **GET** /object-storage/user | Get Client User Object Storage
[**get_subusers**](ObjectStorageApi.md#get_subusers) | **GET** /object-storage/subuser | Get Subusers Object Storage


# **create_client_user**
> NewUserObjStorageSchema create_client_user(client_id)

Create Client User Object Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.new_user_obj_storage_schema import NewUserObjStorageSchema
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
    api_instance = vvcli_sdk.ObjectStorageApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Create Client User Object Storage
        api_response = api_instance.create_client_user(client_id)
        print("The response of ObjectStorageApi->create_client_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->create_client_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**NewUserObjStorageSchema**](NewUserObjStorageSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subuser**
> NewSubUserObjStorageSchema create_subuser(create_sub_user_obj_storage_schema)

Create Subuser Object Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.create_sub_user_obj_storage_schema import CreateSubUserObjStorageSchema
from vvcli_sdk.models.new_sub_user_obj_storage_schema import NewSubUserObjStorageSchema
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
    api_instance = vvcli_sdk.ObjectStorageApi(api_client)
    create_sub_user_obj_storage_schema = vvcli_sdk.CreateSubUserObjStorageSchema() # CreateSubUserObjStorageSchema | 

    try:
        # Create Subuser Object Storage
        api_response = api_instance.create_subuser(create_sub_user_obj_storage_schema)
        print("The response of ObjectStorageApi->create_subuser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->create_subuser: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sub_user_obj_storage_schema** | [**CreateSubUserObjStorageSchema**](CreateSubUserObjStorageSchema.md)|  | 

### Return type

[**NewSubUserObjStorageSchema**](NewSubUserObjStorageSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_user**
> GetUserObjStorageSchema get_client_user(client_id)

Get Client User Object Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.get_user_obj_storage_schema import GetUserObjStorageSchema
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
    api_instance = vvcli_sdk.ObjectStorageApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Get Client User Object Storage
        api_response = api_instance.get_client_user(client_id)
        print("The response of ObjectStorageApi->get_client_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_client_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**GetUserObjStorageSchema**](GetUserObjStorageSchema.md)

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

# **get_subusers**
> PageGetSubUserObjStorageSchema get_subusers(client_id, page=page, size=size)

Get Subusers Object Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.page_get_sub_user_obj_storage_schema import PageGetSubUserObjStorageSchema
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
    api_instance = vvcli_sdk.ObjectStorageApi(api_client)
    client_id = 'client_id_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get Subusers Object Storage
        api_response = api_instance.get_subusers(client_id, page=page, size=size)
        print("The response of ObjectStorageApi->get_subusers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_subusers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageGetSubUserObjStorageSchema**](PageGetSubUserObjStorageSchema.md)

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


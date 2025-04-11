# vvcli_sdk.ObjectStorageApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](ObjectStorageApi.md#create_user) | **POST** /object-storage/user | Create Object Storage User
[**get_user**](ObjectStorageApi.md#get_user) | **GET** /object-storage/user | Get Object Storage


# **create_user**
> GetUserObjStorageSchema create_user(client_id)

Create Object Storage User

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
        # Create Object Storage User
        api_response = api_instance.create_user(client_id)
        print("The response of ObjectStorageApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->create_user: %s\n" % e)
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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserObjStorageSchema get_user(client_id)

Get Object Storage

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
        # Get Object Storage
        api_response = api_instance.get_user(client_id)
        print("The response of ObjectStorageApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_user: %s\n" % e)
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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


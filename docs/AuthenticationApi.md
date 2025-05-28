# vvcli_sdk.AuthenticationApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info**](AuthenticationApi.md#info) | **GET** /auth/info | Authenticated User Information


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


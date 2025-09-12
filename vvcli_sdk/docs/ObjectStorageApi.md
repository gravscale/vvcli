# vvcli_sdk.ObjectStorageApi

All URIs are relative to *https://api.under.com.br/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](ObjectStorageApi.md#create_bucket) | **POST** /object-storage/bucket | Create Bucket Object Storage
[**create_client_user**](ObjectStorageApi.md#create_client_user) | **POST** /object-storage/user | Create Client User Object Storage
[**create_subuser**](ObjectStorageApi.md#create_subuser) | **POST** /object-storage/subuser | Create Subuser Object Storage
[**delete_bucket**](ObjectStorageApi.md#delete_bucket) | **DELETE** /object-storage/bucket | Delete Bucket Object Storage
[**get_client_user**](ObjectStorageApi.md#get_client_user) | **GET** /object-storage/user | Get Client User Object Storage
[**get_subusers**](ObjectStorageApi.md#get_subusers) | **GET** /object-storage/subuser | Get Subusers Object Storage
[**list_buckets**](ObjectStorageApi.md#list_buckets) | **GET** /object-storage/bucket | List Buckets Object Storage


# **create_bucket**
> GetBucketObjStorageSchema create_bucket(client_id, create_bucket_obj_storage_schema)

Create Bucket Object Storage

**Authentication:** Bearer Token (JWT)   ### 📝 Description Creates a new bucket storage to a specific account. ### 🔗 Parameters (Query) - `client_id` (integer): Account client id.  ### 📥 Request Body The request body must be a JSON object with the following properties: - `bucket_name` (string): Bucket name. - `quota`:     - `maxSizeMb` (integer): Maximum bucket storage size in MB.     - `maxObjects` (integer): Maximum quantity of items in the bucket.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.create_bucket_obj_storage_schema import CreateBucketObjStorageSchema
from vvcli_sdk.models.get_bucket_obj_storage_schema import GetBucketObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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
    client_id = 56 # int | 
    create_bucket_obj_storage_schema = vvcli_sdk.CreateBucketObjStorageSchema() # CreateBucketObjStorageSchema | 

    try:
        # Create Bucket Object Storage
        api_response = api_instance.create_bucket(client_id, create_bucket_obj_storage_schema)
        print("The response of ObjectStorageApi->create_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **create_bucket_obj_storage_schema** | [**CreateBucketObjStorageSchema**](CreateBucketObjStorageSchema.md)|  | 

### Return type

[**GetBucketObjStorageSchema**](GetBucketObjStorageSchema.md)

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

# **create_client_user**
> NewUserObjStorageSchema create_client_user(client_id, size_quota)

Create Client User Object Storage

**Authentication:** Bearer Token (JWT)   ### 📝 Description Creates a new Object Storage user associated with a specific account. Generates unique access credentials for integration with cloud storage services. ### 🔗 Parameters (Query) - `client_id` (integer): Account client id. - `size_quota` (integer): User quota in gigabyte (GB). The value must be between 100 GB and 50000 GB.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.new_user_obj_storage_schema import NewUserObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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
    client_id = 56 # int | 
    size_quota = 56 # int | 

    try:
        # Create Client User Object Storage
        api_response = api_instance.create_client_user(client_id, size_quota)
        print("The response of ObjectStorageApi->create_client_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->create_client_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **size_quota** | **int**|  | 

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

**Authentication:** Bearer Token (JWT)   ### 📝 Description Create an object storage subuser with tight restrictions associated with an account. Subuser concept for granular management of bucket access and operations.  ### 📥 Request Body The request body must be a JSON object with the following properties: - `display_name` (string): Display name for the subuser. - `client_id` (integer): Account client id. - `access` (string): Valid Values for permissions (`read`, `write`, `read-write`)

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.create_sub_user_obj_storage_schema import CreateSubUserObjStorageSchema
from vvcli_sdk.models.new_sub_user_obj_storage_schema import NewSubUserObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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

# **delete_bucket**
> delete_bucket(client_id, bucket_name)

Delete Bucket Object Storage

**Authentication:** Bearer Token (JWT)   ### 📝 Description Delete a bucket storage from a specific account. ### 🔗 Parameters (Query) - `client_id` (integer): Account client id. - `bucket_name` (string): Bucket name.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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
    client_id = 56 # int | 
    bucket_name = 'bucket_name_example' # str | 

    try:
        # Delete Bucket Object Storage
        api_instance.delete_bucket(client_id, bucket_name)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **bucket_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_user**
> GetUserObjStorageSchema get_client_user(client_id)

Get Client User Object Storage

**Authentication:** Bearer Token (JWT)   ### 📝 Description Returns existing Object Storage user associated with a specific account. Provides access to active integration information. ### 🔗 Parameters (Query) - `client_id` (integer): Account client id.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.get_user_obj_storage_schema import GetUserObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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
    client_id = 56 # int | 

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
 **client_id** | **int**|  | 

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

**Authentication:** Bearer Token (JWT)   ### 📝 Description Lists all storage subusers associated with the authenticated user and per active account, with pagination and filters ### 🔗 Parameters (Query) - `client_id` (integer): Account client id.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.page_get_sub_user_obj_storage_schema import PageGetSubUserObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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

# **list_buckets**
> PageGetBucketObjStorageSchema list_buckets(client_id, page=page, size=size)

List Buckets Object Storage

**Authentication:** Bearer Token (JWT)   ### 📝 Description Lists all storage buckets registered to a specific account.  ### 🔗 Parameters (Query) - `client_id` (integer): Account client id.

### Example

* Bearer Authentication (HTTPBearer):

```python
import vvcli_sdk
from vvcli_sdk.models.page_get_bucket_obj_storage_schema import PageGetBucketObjStorageSchema
from vvcli_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.under.com.br/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vvcli_sdk.Configuration(
    host = "https://api.under.com.br/v1"
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
    client_id = 56 # int | 
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List Buckets Object Storage
        api_response = api_instance.list_buckets(client_id, page=page, size=size)
        print("The response of ObjectStorageApi->list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageGetBucketObjStorageSchema**](PageGetBucketObjStorageSchema.md)

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


# GetBucketQuotaSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**max_size_bytes** | **int** |  | 
**max_objects** | **int** |  | 

## Example

```python
from vvcli_sdk.models.get_bucket_quota_schema import GetBucketQuotaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetBucketQuotaSchema from a JSON string
get_bucket_quota_schema_instance = GetBucketQuotaSchema.from_json(json)
# print the JSON string representation of the object
print(GetBucketQuotaSchema.to_json())

# convert the object into a dict
get_bucket_quota_schema_dict = get_bucket_quota_schema_instance.to_dict()
# create an instance of GetBucketQuotaSchema from a dict
get_bucket_quota_schema_from_dict = GetBucketQuotaSchema.from_dict(get_bucket_quota_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



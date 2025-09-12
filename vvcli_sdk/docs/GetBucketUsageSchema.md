# GetBucketUsageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_utilized_bytes** | **int** |  | [optional] 
**num_objects** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.get_bucket_usage_schema import GetBucketUsageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetBucketUsageSchema from a JSON string
get_bucket_usage_schema_instance = GetBucketUsageSchema.from_json(json)
# print the JSON string representation of the object
print(GetBucketUsageSchema.to_json())

# convert the object into a dict
get_bucket_usage_schema_dict = get_bucket_usage_schema_instance.to_dict()
# create an instance of GetBucketUsageSchema from a dict
get_bucket_usage_schema_from_dict = GetBucketUsageSchema.from_dict(get_bucket_usage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



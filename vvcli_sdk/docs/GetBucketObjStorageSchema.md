# GetBucketObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**usage** | [**GetBucketUsageSchema**](GetBucketUsageSchema.md) |  | [optional] 
**quota** | [**GetBucketQuotaSchema**](GetBucketQuotaSchema.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from vvcli_sdk.models.get_bucket_obj_storage_schema import GetBucketObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetBucketObjStorageSchema from a JSON string
get_bucket_obj_storage_schema_instance = GetBucketObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(GetBucketObjStorageSchema.to_json())

# convert the object into a dict
get_bucket_obj_storage_schema_dict = get_bucket_obj_storage_schema_instance.to_dict()
# create an instance of GetBucketObjStorageSchema from a dict
get_bucket_obj_storage_schema_from_dict = GetBucketObjStorageSchema.from_dict(get_bucket_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



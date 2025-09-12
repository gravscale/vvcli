# PageGetBucketObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GetBucketObjStorageSchema]**](GetBucketObjStorageSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.page_get_bucket_obj_storage_schema import PageGetBucketObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageGetBucketObjStorageSchema from a JSON string
page_get_bucket_obj_storage_schema_instance = PageGetBucketObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(PageGetBucketObjStorageSchema.to_json())

# convert the object into a dict
page_get_bucket_obj_storage_schema_dict = page_get_bucket_obj_storage_schema_instance.to_dict()
# create an instance of PageGetBucketObjStorageSchema from a dict
page_get_bucket_obj_storage_schema_from_dict = PageGetBucketObjStorageSchema.from_dict(page_get_bucket_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



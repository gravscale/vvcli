# CreateBucketObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | 
**quota** | [**AddBucketQuotaSchema**](AddBucketQuotaSchema.md) |  | [optional] 

## Example

```python
from vvcli_sdk.models.create_bucket_obj_storage_schema import CreateBucketObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBucketObjStorageSchema from a JSON string
create_bucket_obj_storage_schema_instance = CreateBucketObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(CreateBucketObjStorageSchema.to_json())

# convert the object into a dict
create_bucket_obj_storage_schema_dict = create_bucket_obj_storage_schema_instance.to_dict()
# create an instance of CreateBucketObjStorageSchema from a dict
create_bucket_obj_storage_schema_from_dict = CreateBucketObjStorageSchema.from_dict(create_bucket_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



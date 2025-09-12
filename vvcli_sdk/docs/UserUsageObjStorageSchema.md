# UserUsageObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_bytes** | **int** |  | [optional] 
**num_objects** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.user_usage_obj_storage_schema import UserUsageObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageObjStorageSchema from a JSON string
user_usage_obj_storage_schema_instance = UserUsageObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(UserUsageObjStorageSchema.to_json())

# convert the object into a dict
user_usage_obj_storage_schema_dict = user_usage_obj_storage_schema_instance.to_dict()
# create an instance of UserUsageObjStorageSchema from a dict
user_usage_obj_storage_schema_from_dict = UserUsageObjStorageSchema.from_dict(user_usage_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



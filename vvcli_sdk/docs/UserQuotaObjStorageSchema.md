# UserQuotaObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_size_bytes** | **int** |  | [optional] 
**max_objects** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.user_quota_obj_storage_schema import UserQuotaObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuotaObjStorageSchema from a JSON string
user_quota_obj_storage_schema_instance = UserQuotaObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(UserQuotaObjStorageSchema.to_json())

# convert the object into a dict
user_quota_obj_storage_schema_dict = user_quota_obj_storage_schema_instance.to_dict()
# create an instance of UserQuotaObjStorageSchema from a dict
user_quota_obj_storage_schema_from_dict = UserQuotaObjStorageSchema.from_dict(user_quota_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetUserObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_srn** | **str** |  | 
**contract_key** | **str** |  | 
**client_id** | **str** |  | 

## Example

```python
from vvcli_sdk.models.get_user_obj_storage_schema import GetUserObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserObjStorageSchema from a JSON string
get_user_obj_storage_schema_instance = GetUserObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(GetUserObjStorageSchema.to_json())

# convert the object into a dict
get_user_obj_storage_schema_dict = get_user_obj_storage_schema_instance.to_dict()
# create an instance of GetUserObjStorageSchema from a dict
get_user_obj_storage_schema_from_dict = GetUserObjStorageSchema.from_dict(get_user_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



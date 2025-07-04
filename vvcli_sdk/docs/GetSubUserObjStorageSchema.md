# GetSubUserObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_srn** | **str** |  | 
**display_name** | **str** |  | 
**client_id** | **str** |  | 

## Example

```python
from vvcli_sdk.models.get_sub_user_obj_storage_schema import GetSubUserObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubUserObjStorageSchema from a JSON string
get_sub_user_obj_storage_schema_instance = GetSubUserObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(GetSubUserObjStorageSchema.to_json())

# convert the object into a dict
get_sub_user_obj_storage_schema_dict = get_sub_user_obj_storage_schema_instance.to_dict()
# create an instance of GetSubUserObjStorageSchema from a dict
get_sub_user_obj_storage_schema_from_dict = GetSubUserObjStorageSchema.from_dict(get_sub_user_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



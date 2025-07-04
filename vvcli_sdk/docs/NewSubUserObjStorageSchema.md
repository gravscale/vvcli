# NewSubUserObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_srn** | **str** |  | 
**display_name** | **str** |  | 
**client_id** | **str** |  | 
**keys** | [**List[CredentialKey]**](CredentialKey.md) |  | [optional] 

## Example

```python
from vvcli_sdk.models.new_sub_user_obj_storage_schema import NewSubUserObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NewSubUserObjStorageSchema from a JSON string
new_sub_user_obj_storage_schema_instance = NewSubUserObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(NewSubUserObjStorageSchema.to_json())

# convert the object into a dict
new_sub_user_obj_storage_schema_dict = new_sub_user_obj_storage_schema_instance.to_dict()
# create an instance of NewSubUserObjStorageSchema from a dict
new_sub_user_obj_storage_schema_from_dict = NewSubUserObjStorageSchema.from_dict(new_sub_user_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



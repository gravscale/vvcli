# CreateSubUserObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**display_name** | **str** |  | 
**access** | [**AccessPermissions**](AccessPermissions.md) |  | 

## Example

```python
from vvcli_sdk.models.create_sub_user_obj_storage_schema import CreateSubUserObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubUserObjStorageSchema from a JSON string
create_sub_user_obj_storage_schema_instance = CreateSubUserObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(CreateSubUserObjStorageSchema.to_json())

# convert the object into a dict
create_sub_user_obj_storage_schema_dict = create_sub_user_obj_storage_schema_instance.to_dict()
# create an instance of CreateSubUserObjStorageSchema from a dict
create_sub_user_obj_storage_schema_from_dict = CreateSubUserObjStorageSchema.from_dict(create_sub_user_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



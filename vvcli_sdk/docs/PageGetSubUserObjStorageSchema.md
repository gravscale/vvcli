# PageGetSubUserObjStorageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GetSubUserObjStorageSchema]**](GetSubUserObjStorageSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.page_get_sub_user_obj_storage_schema import PageGetSubUserObjStorageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageGetSubUserObjStorageSchema from a JSON string
page_get_sub_user_obj_storage_schema_instance = PageGetSubUserObjStorageSchema.from_json(json)
# print the JSON string representation of the object
print(PageGetSubUserObjStorageSchema.to_json())

# convert the object into a dict
page_get_sub_user_obj_storage_schema_dict = page_get_sub_user_obj_storage_schema_instance.to_dict()
# create an instance of PageGetSubUserObjStorageSchema from a dict
page_get_sub_user_obj_storage_schema_from_dict = PageGetSubUserObjStorageSchema.from_dict(page_get_sub_user_obj_storage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AuthInfoSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clerk_id** | **str** |  | 
**srn** | **str** |  | 
**email** | **str** |  | 
**nickname** | **str** |  | 

## Example

```python
from vvcli_sdk.models.auth_info_schema import AuthInfoSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInfoSchema from a JSON string
auth_info_schema_instance = AuthInfoSchema.from_json(json)
# print the JSON string representation of the object
print(AuthInfoSchema.to_json())

# convert the object into a dict
auth_info_schema_dict = auth_info_schema_instance.to_dict()
# create an instance of AuthInfoSchema from a dict
auth_info_schema_from_dict = AuthInfoSchema.from_dict(auth_info_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



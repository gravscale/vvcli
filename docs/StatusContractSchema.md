# StatusContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**label_client** | **str** |  | 
**name** | **str** |  | 
**name_client** | **str** |  | 

## Example

```python
from vvcli_sdk.models.status_contract_schema import StatusContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StatusContractSchema from a JSON string
status_contract_schema_instance = StatusContractSchema.from_json(json)
# print the JSON string representation of the object
print(StatusContractSchema.to_json())

# convert the object into a dict
status_contract_schema_dict = status_contract_schema_instance.to_dict()
# create an instance of StatusContractSchema from a dict
status_contract_schema_from_dict = StatusContractSchema.from_dict(status_contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



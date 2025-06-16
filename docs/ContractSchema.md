# ContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 
**key** | **str** |  | 
**surname** | **str** |  | 
**product** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from vvcli_sdk.models.contract_schema import ContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractSchema from a JSON string
contract_schema_instance = ContractSchema.from_json(json)
# print the JSON string representation of the object
print(ContractSchema.to_json())

# convert the object into a dict
contract_schema_dict = contract_schema_instance.to_dict()
# create an instance of ContractSchema from a dict
contract_schema_from_dict = ContractSchema.from_dict(contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



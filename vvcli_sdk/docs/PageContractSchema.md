# PageContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContractSchema]**](ContractSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.page_contract_schema import PageContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageContractSchema from a JSON string
page_contract_schema_instance = PageContractSchema.from_json(json)
# print the JSON string representation of the object
print(PageContractSchema.to_json())

# convert the object into a dict
page_contract_schema_dict = page_contract_schema_instance.to_dict()
# create an instance of PageContractSchema from a dict
page_contract_schema_from_dict = PageContractSchema.from_dict(page_contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



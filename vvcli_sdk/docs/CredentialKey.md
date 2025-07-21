# CredentialKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | 
**secret_key** | **str** |  | 

## Example

```python
from vvcli_sdk.models.credential_key import CredentialKey

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialKey from a JSON string
credential_key_instance = CredentialKey.from_json(json)
# print the JSON string representation of the object
print(CredentialKey.to_json())

# convert the object into a dict
credential_key_dict = credential_key_instance.to_dict()
# create an instance of CredentialKey from a dict
credential_key_from_dict = CredentialKey.from_dict(credential_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



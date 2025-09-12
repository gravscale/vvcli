# AddBucketQuotaSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_size_mb** | **int** |  | [optional] 
**max_objects** | **int** |  | [optional] 

## Example

```python
from vvcli_sdk.models.add_bucket_quota_schema import AddBucketQuotaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddBucketQuotaSchema from a JSON string
add_bucket_quota_schema_instance = AddBucketQuotaSchema.from_json(json)
# print the JSON string representation of the object
print(AddBucketQuotaSchema.to_json())

# convert the object into a dict
add_bucket_quota_schema_dict = add_bucket_quota_schema_instance.to_dict()
# create an instance of AddBucketQuotaSchema from a dict
add_bucket_quota_schema_from_dict = AddBucketQuotaSchema.from_dict(add_bucket_quota_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



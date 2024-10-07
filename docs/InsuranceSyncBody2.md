# InsuranceSyncBody2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[Insurance5]**](Insurance5.md) |  | 

## Example

```python
from procore_sdk.models.insurance_sync_body2 import InsuranceSyncBody2

# TODO update the JSON string below
json = "{}"
# create an instance of InsuranceSyncBody2 from a JSON string
insurance_sync_body2_instance = InsuranceSyncBody2.from_json(json)
# print the JSON string representation of the object
print(InsuranceSyncBody2.to_json())

# convert the object into a dict
insurance_sync_body2_dict = insurance_sync_body2_instance.to_dict()
# create an instance of InsuranceSyncBody2 from a dict
insurance_sync_body2_from_dict = InsuranceSyncBody2.from_dict(insurance_sync_body2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



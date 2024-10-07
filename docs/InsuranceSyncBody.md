# InsuranceSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[Insurance2]**](Insurance2.md) |  | 

## Example

```python
from procore_sdk.models.insurance_sync_body import InsuranceSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of InsuranceSyncBody from a JSON string
insurance_sync_body_instance = InsuranceSyncBody.from_json(json)
# print the JSON string representation of the object
print(InsuranceSyncBody.to_json())

# convert the object into a dict
insurance_sync_body_dict = insurance_sync_body_instance.to_dict()
# create an instance of InsuranceSyncBody from a dict
insurance_sync_body_from_dict = InsuranceSyncBody.from_dict(insurance_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



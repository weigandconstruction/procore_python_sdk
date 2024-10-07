# CostCodeSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[LineItem1]**](LineItem1.md) |  | 

## Example

```python
from procore_sdk.models.cost_code_sync_body import CostCodeSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of CostCodeSyncBody from a JSON string
cost_code_sync_body_instance = CostCodeSyncBody.from_json(json)
# print the JSON string representation of the object
print(CostCodeSyncBody.to_json())

# convert the object into a dict
cost_code_sync_body_dict = cost_code_sync_body_instance.to_dict()
# create an instance of CostCodeSyncBody from a dict
cost_code_sync_body_from_dict = CostCodeSyncBody.from_dict(cost_code_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



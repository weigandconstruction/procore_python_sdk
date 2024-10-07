# StandardCostCodeSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**standard_cost_code_list_id** | **int** | Standard Cost Code list ID | 
**updates** | [**List[StandardCostCodeSyncBodyUpdatesInner]**](StandardCostCodeSyncBodyUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.standard_cost_code_sync_body import StandardCostCodeSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCodeSyncBody from a JSON string
standard_cost_code_sync_body_instance = StandardCostCodeSyncBody.from_json(json)
# print the JSON string representation of the object
print(StandardCostCodeSyncBody.to_json())

# convert the object into a dict
standard_cost_code_sync_body_dict = standard_cost_code_sync_body_instance.to_dict()
# create an instance of StandardCostCodeSyncBody from a dict
standard_cost_code_sync_body_from_dict = StandardCostCodeSyncBody.from_dict(standard_cost_code_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



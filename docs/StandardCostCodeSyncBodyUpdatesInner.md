# StandardCostCodeSyncBodyUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**id** | **int** | The ID of the Standard Cost Code | [optional] 
**code** | **str** | Standard Cost code, including parent prefixes. | [optional] 
**parent_id** | **int** | The ID of the parent Standard Cost Code | [optional] 
**origin_id** | **str** | The Third-party ID of Standard Cost Code | [optional] 
**origin_data** | **str** | Additional Third-party Metadata of the Standard Cost Code (this is a free-form text field) | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code_sync_body_updates_inner import StandardCostCodeSyncBodyUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCodeSyncBodyUpdatesInner from a JSON string
standard_cost_code_sync_body_updates_inner_instance = StandardCostCodeSyncBodyUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(StandardCostCodeSyncBodyUpdatesInner.to_json())

# convert the object into a dict
standard_cost_code_sync_body_updates_inner_dict = standard_cost_code_sync_body_updates_inner_instance.to_dict()
# create an instance of StandardCostCodeSyncBodyUpdatesInner from a dict
standard_cost_code_sync_body_updates_inner_from_dict = StandardCostCodeSyncBodyUpdatesInner.from_dict(standard_cost_code_sync_body_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



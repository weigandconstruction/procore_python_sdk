# Summary

Vendor Summary View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**active_users_count** | **int** |  | [optional] 
**bids_count** | **int** |  | [optional] 
**business_id** | **int** |  | [optional] 
**company_vendor** | **bool** |  | [optional] 
**is_connected** | **bool** |  | [optional] 
**open_bids_count** | **int** |  | [optional] 
**projects_count** | **int** |  | [optional] 
**synced_to_erp** | **bool** | Synced to ERP | [optional] 

## Example

```python
from procore_sdk.models.summary import Summary

# TODO update the JSON string below
json = "{}"
# create an instance of Summary from a JSON string
summary_instance = Summary.from_json(json)
# print the JSON string representation of the object
print(Summary.to_json())

# convert the object into a dict
summary_dict = summary_instance.to_dict()
# create an instance of Summary from a dict
summary_from_dict = Summary.from_dict(summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



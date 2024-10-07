# ObservationItemAssignee1Vendor

Company of User assigned to the Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor ID | [optional] 
**name** | **str** | Vendor Name | [optional] 

## Example

```python
from procore_sdk.models.observation_item_assignee1_vendor import ObservationItemAssignee1Vendor

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemAssignee1Vendor from a JSON string
observation_item_assignee1_vendor_instance = ObservationItemAssignee1Vendor.from_json(json)
# print the JSON string representation of the object
print(ObservationItemAssignee1Vendor.to_json())

# convert the object into a dict
observation_item_assignee1_vendor_dict = observation_item_assignee1_vendor_instance.to_dict()
# create an instance of ObservationItemAssignee1Vendor from a dict
observation_item_assignee1_vendor_from_dict = ObservationItemAssignee1Vendor.from_dict(observation_item_assignee1_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



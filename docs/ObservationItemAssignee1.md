# ObservationItemAssignee1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User&#39;s name | [optional] 
**vendor** | [**ObservationItemAssignee1Vendor**](ObservationItemAssignee1Vendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item_assignee1 import ObservationItemAssignee1

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemAssignee1 from a JSON string
observation_item_assignee1_instance = ObservationItemAssignee1.from_json(json)
# print the JSON string representation of the object
print(ObservationItemAssignee1.to_json())

# convert the object into a dict
observation_item_assignee1_dict = observation_item_assignee1_instance.to_dict()
# create an instance of ObservationItemAssignee1 from a dict
observation_item_assignee1_from_dict = ObservationItemAssignee1.from_dict(observation_item_assignee1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



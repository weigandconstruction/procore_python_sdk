# ObservationItemAssignee

User assigned to the Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**vendor** | [**ObservationItemAssigneeSCompany**](ObservationItemAssigneeSCompany.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item_assignee import ObservationItemAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemAssignee from a JSON string
observation_item_assignee_instance = ObservationItemAssignee.from_json(json)
# print the JSON string representation of the object
print(ObservationItemAssignee.to_json())

# convert the object into a dict
observation_item_assignee_dict = observation_item_assignee_instance.to_dict()
# create an instance of ObservationItemAssignee from a dict
observation_item_assignee_from_dict = ObservationItemAssignee.from_dict(observation_item_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



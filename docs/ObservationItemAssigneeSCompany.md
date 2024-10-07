# ObservationItemAssigneeSCompany

Company of User assigned to the Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor ID | [optional] 
**name** | **str** | Vendor Name | [optional] 

## Example

```python
from procore_sdk.models.observation_item_assignee_s_company import ObservationItemAssigneeSCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemAssigneeSCompany from a JSON string
observation_item_assignee_s_company_instance = ObservationItemAssigneeSCompany.from_json(json)
# print the JSON string representation of the object
print(ObservationItemAssigneeSCompany.to_json())

# convert the object into a dict
observation_item_assignee_s_company_dict = observation_item_assignee_s_company_instance.to_dict()
# create an instance of ObservationItemAssigneeSCompany from a dict
observation_item_assignee_s_company_from_dict = ObservationItemAssigneeSCompany.from_dict(observation_item_assignee_s_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



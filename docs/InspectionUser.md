# InspectionUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | User&#39;s Name | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 
**potential_assignee** | **bool** | Represents whether or not a user can be an Assignee for an Inspection. | [optional] 
**potential_point_of_contact** | **bool** | Represents whether or not a user can be a Point of Contact for an Inspection. | [optional] 
**potential_distribution_member** | **bool** | Represents whether or not a user can be a Distribution Member for an Inspection. | [optional] 
**default_distribution_member** | **bool** | Represents whether or not a user is a Default Distribution Member for Inspections. | [optional] 
**custom_fields** | [**InspectionUserCustomFields**](InspectionUserCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.inspection_user import InspectionUser

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionUser from a JSON string
inspection_user_instance = InspectionUser.from_json(json)
# print the JSON string representation of the object
print(InspectionUser.to_json())

# convert the object into a dict
inspection_user_dict = inspection_user_instance.to_dict()
# create an instance of InspectionUser from a dict
inspection_user_from_dict = InspectionUser.from_dict(inspection_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ChecklistPotentialPointOfContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | Name | [optional] 
**name_with_vendor** | **str** | Name with Vendor | [optional] 
**job_title** | **str** | Job Title | [optional] 
**vendor** | [**ChecklistPotentialPointOfContactVendor**](ChecklistPotentialPointOfContactVendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_potential_point_of_contact import ChecklistPotentialPointOfContact

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistPotentialPointOfContact from a JSON string
checklist_potential_point_of_contact_instance = ChecklistPotentialPointOfContact.from_json(json)
# print the JSON string representation of the object
print(ChecklistPotentialPointOfContact.to_json())

# convert the object into a dict
checklist_potential_point_of_contact_dict = checklist_potential_point_of_contact_instance.to_dict()
# create an instance of ChecklistPotentialPointOfContact from a dict
checklist_potential_point_of_contact_from_dict = ChecklistPotentialPointOfContact.from_dict(checklist_potential_point_of_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



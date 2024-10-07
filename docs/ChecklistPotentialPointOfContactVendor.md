# ChecklistPotentialPointOfContactVendor

Vendor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor ID | [optional] 
**name** | **str** | Vendor Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_potential_point_of_contact_vendor import ChecklistPotentialPointOfContactVendor

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistPotentialPointOfContactVendor from a JSON string
checklist_potential_point_of_contact_vendor_instance = ChecklistPotentialPointOfContactVendor.from_json(json)
# print the JSON string representation of the object
print(ChecklistPotentialPointOfContactVendor.to_json())

# convert the object into a dict
checklist_potential_point_of_contact_vendor_dict = checklist_potential_point_of_contact_vendor_instance.to_dict()
# create an instance of ChecklistPotentialPointOfContactVendor from a dict
checklist_potential_point_of_contact_vendor_from_dict = ChecklistPotentialPointOfContactVendor.from_dict(checklist_potential_point_of_contact_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



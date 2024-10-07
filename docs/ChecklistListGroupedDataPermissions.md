# ChecklistListGroupedDataPermissions

User permissions for the specific Inspection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Flag indicating if the user can edit the specific Inspection | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_grouped_data_permissions import ChecklistListGroupedDataPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListGroupedDataPermissions from a JSON string
checklist_list_grouped_data_permissions_instance = ChecklistListGroupedDataPermissions.from_json(json)
# print the JSON string representation of the object
print(ChecklistListGroupedDataPermissions.to_json())

# convert the object into a dict
checklist_list_grouped_data_permissions_dict = checklist_list_grouped_data_permissions_instance.to_dict()
# create an instance of ChecklistListGroupedDataPermissions from a dict
checklist_list_grouped_data_permissions_from_dict = ChecklistListGroupedDataPermissions.from_dict(checklist_list_grouped_data_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



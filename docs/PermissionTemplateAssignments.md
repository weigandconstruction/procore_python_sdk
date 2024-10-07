# PermissionTemplateAssignments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of the user you wish to update the permission template for | 
**permission_template_id** | **int** | The ID of the permission template you&#39;d like to assign to the user for the project | 

## Example

```python
from procore_sdk.models.permission_template_assignments import PermissionTemplateAssignments

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionTemplateAssignments from a JSON string
permission_template_assignments_instance = PermissionTemplateAssignments.from_json(json)
# print the JSON string representation of the object
print(PermissionTemplateAssignments.to_json())

# convert the object into a dict
permission_template_assignments_dict = permission_template_assignments_instance.to_dict()
# create an instance of PermissionTemplateAssignments from a dict
permission_template_assignments_from_dict = PermissionTemplateAssignments.from_dict(permission_template_assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



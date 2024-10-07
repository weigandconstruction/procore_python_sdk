# ProjectChecklistTemplateSyncedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**list_template_id** | **int** | Company List Template ID that List Template is Synced to | [optional] 

## Example

```python
from procore_sdk.models.project_checklist_template_synced_to import ProjectChecklistTemplateSyncedTo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChecklistTemplateSyncedTo from a JSON string
project_checklist_template_synced_to_instance = ProjectChecklistTemplateSyncedTo.from_json(json)
# print the JSON string representation of the object
print(ProjectChecklistTemplateSyncedTo.to_json())

# convert the object into a dict
project_checklist_template_synced_to_dict = project_checklist_template_synced_to_instance.to_dict()
# create an instance of ProjectChecklistTemplateSyncedTo from a dict
project_checklist_template_synced_to_from_dict = ProjectChecklistTemplateSyncedTo.from_dict(project_checklist_template_synced_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



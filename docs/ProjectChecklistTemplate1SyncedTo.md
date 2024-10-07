# ProjectChecklistTemplate1SyncedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**list_template_id** | **int** | Company List Template ID that List Template is Synced to | [optional] 

## Example

```python
from procore_sdk.models.project_checklist_template1_synced_to import ProjectChecklistTemplate1SyncedTo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChecklistTemplate1SyncedTo from a JSON string
project_checklist_template1_synced_to_instance = ProjectChecklistTemplate1SyncedTo.from_json(json)
# print the JSON string representation of the object
print(ProjectChecklistTemplate1SyncedTo.to_json())

# convert the object into a dict
project_checklist_template1_synced_to_dict = project_checklist_template1_synced_to_instance.to_dict()
# create an instance of ProjectChecklistTemplate1SyncedTo from a dict
project_checklist_template1_synced_to_from_dict = ProjectChecklistTemplate1SyncedTo.from_dict(project_checklist_template1_synced_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ChecklistTemplate1SyncedTo

Checklist Template's synced Company Template information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**list_template_id** | **int** | Company List Template ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_template1_synced_to import ChecklistTemplate1SyncedTo

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate1SyncedTo from a JSON string
checklist_template1_synced_to_instance = ChecklistTemplate1SyncedTo.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate1SyncedTo.to_json())

# convert the object into a dict
checklist_template1_synced_to_dict = checklist_template1_synced_to_instance.to_dict()
# create an instance of ChecklistTemplate1SyncedTo from a dict
checklist_template1_synced_to_from_dict = ChecklistTemplate1SyncedTo.from_dict(checklist_template1_synced_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



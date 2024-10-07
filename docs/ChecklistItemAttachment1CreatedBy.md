# ChecklistItemAttachment1CreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company_name** | **str** | User Company name | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_attachment1_created_by import ChecklistItemAttachment1CreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachment1CreatedBy from a JSON string
checklist_item_attachment1_created_by_instance = ChecklistItemAttachment1CreatedBy.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachment1CreatedBy.to_json())

# convert the object into a dict
checklist_item_attachment1_created_by_dict = checklist_item_attachment1_created_by_instance.to_dict()
# create an instance of ChecklistItemAttachment1CreatedBy from a dict
checklist_item_attachment1_created_by_from_dict = ChecklistItemAttachment1CreatedBy.from_dict(checklist_item_attachment1_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



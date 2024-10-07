# ChecklistItemBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Item belongs to | 
**section_id** | **int** | The ID of the Section the Item belongs to | 
**item** | [**Item**](Item.md) |  | 
**attachments** | **List[str]** | Item&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_body import ChecklistItemBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemBody from a JSON string
checklist_item_body_instance = ChecklistItemBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemBody.to_json())

# convert the object into a dict
checklist_item_body_dict = checklist_item_body_instance.to_dict()
# create an instance of ChecklistItemBody from a dict
checklist_item_body_from_dict = ChecklistItemBody.from_dict(checklist_item_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



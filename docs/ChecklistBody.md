# ChecklistBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project | 
**template_id** | **int** | The ID of the Template to copy from. | 
**list** | [**Checklist2**](Checklist2.md) |  | 
**attachments** | **List[str]** | Checklist&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.checklist_body import ChecklistBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistBody from a JSON string
checklist_body_instance = ChecklistBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistBody.to_json())

# convert the object into a dict
checklist_body_dict = checklist_body_instance.to_dict()
# create an instance of ChecklistBody from a dict
checklist_body_from_dict = ChecklistBody.from_dict(checklist_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



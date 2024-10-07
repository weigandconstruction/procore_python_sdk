# ChecklistBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project | 
**list** | [**Checklist4**](Checklist4.md) |  | 
**attachments** | **List[str]** | Checklist&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.checklist_body1 import ChecklistBody1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistBody1 from a JSON string
checklist_body1_instance = ChecklistBody1.from_json(json)
# print the JSON string representation of the object
print(ChecklistBody1.to_json())

# convert the object into a dict
checklist_body1_dict = checklist_body1_instance.to_dict()
# create an instance of ChecklistBody1 from a dict
checklist_body1_from_dict = ChecklistBody1.from_dict(checklist_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



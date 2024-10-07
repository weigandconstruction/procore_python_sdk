# ChecklistTemplateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_template** | [**ChecklistTemplate**](ChecklistTemplate.md) |  | 
**attachments** | **List[bytearray]** | Checklist Template&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_body import ChecklistTemplateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateBody from a JSON string
checklist_template_body_instance = ChecklistTemplateBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateBody.to_json())

# convert the object into a dict
checklist_template_body_dict = checklist_template_body_instance.to_dict()
# create an instance of ChecklistTemplateBody from a dict
checklist_template_body_from_dict = ChecklistTemplateBody.from_dict(checklist_template_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**alternative_response_set_id** | **int** | Alternative Response Set ID | 

## Example

```python
from procore_sdk.models.rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request import RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest from a JSON string
rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request_instance = RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.to_json())

# convert the object into a dict
rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request_dict = rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request_instance.to_dict()
# create an instance of RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest from a dict
rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request_from_dict = RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.from_dict(rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



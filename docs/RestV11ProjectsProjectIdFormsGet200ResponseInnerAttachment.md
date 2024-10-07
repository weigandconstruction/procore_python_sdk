# RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**name** | **str** | Attachment Name | [optional] 
**url** | **str** | Attachment URL | [optional] 
**filename** | **str** | Attachment Filename | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner_attachment import RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment from a JSON string
rest_v11_projects_project_id_forms_get200_response_inner_attachment_instance = RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment.to_json())

# convert the object into a dict
rest_v11_projects_project_id_forms_get200_response_inner_attachment_dict = rest_v11_projects_project_id_forms_get200_response_inner_attachment_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment from a dict
rest_v11_projects_project_id_forms_get200_response_inner_attachment_from_dict = RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment.from_dict(rest_v11_projects_project_id_forms_get200_response_inner_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV11ProjectsProjectIdFormsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Date created | [optional] 
**description** | **str** | Description | [optional] 
**form_template_id** | **int** | Form Template ID | [optional] 
**form_template_name** | **str** | Form Template Name | [optional] 
**name** | **str** | Name | [optional] 
**private** | **bool** | private | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**updated_at** | **datetime** | Date updated | [optional] 
**fillable_pdf** | [**RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf**](RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.md) |  | [optional] 
**attachments** | [**List[RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf]**](RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.md) |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**viewable** | **bool** | Is Form viewable flag | [optional] 
**viewable_document_id** | **int** | Viewable Document ID | [optional] 
**holder_class** | **str** | Holder class | [optional] 
**download_all_uuid** | **Dict[str, object]** |  | [optional] 
**attachment** | [**RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment**](RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment.md) |  | [optional] 
**permissions** | [**RestV11ProjectsProjectIdFormsGet200ResponseInnerPermissions**](RestV11ProjectsProjectIdFormsGet200ResponseInnerPermissions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_forms_get200_response_inner_instance = RestV11ProjectsProjectIdFormsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdFormsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_forms_get200_response_inner_dict = rest_v11_projects_project_id_forms_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInner from a dict
rest_v11_projects_project_id_forms_get200_response_inner_from_dict = RestV11ProjectsProjectIdFormsGet200ResponseInner.from_dict(rest_v11_projects_project_id_forms_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



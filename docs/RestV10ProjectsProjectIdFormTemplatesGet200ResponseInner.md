# RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**created_at** | **datetime** | Date created | [optional] 
**updated_at** | **datetime** | Date updated | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachment** | [**RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf**](RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.md) |  | [optional] 
**fillable_pdf** | [**RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf**](RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_form_templates_get200_response_inner_instance = RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_form_templates_get200_response_inner_dict = rest_v10_projects_project_id_form_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner from a dict
rest_v10_projects_project_id_form_templates_get200_response_inner_from_dict = RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.from_dict(rest_v10_projects_project_id_form_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner

Project Inspection Template Item Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**template_id** | **int** | ID of the associated Project Inspection Template | [optional] 
**item_id** | **int** | ID of the associated Project Inspection Template Item | [optional] 
**payload** | [**RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayload**](RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayload.md) |  | [optional] 
**type** | **str** | Project Inspection Template Item Reference Type | [optional] 
**created_at** | **str** | Time the Project Inspection Template Item Reference was created | [optional] 
**updated_at** | **str** | Time the Project Inspection Template Item Reference was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner import RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_instance = RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_dict = rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner from a dict
rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_from_dict = RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInner.from_dict(rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response

A work breakdown structure pattern

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | The description of a Pattern | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**is_project_level_ordered** | **bool** | Whether the Pattern has a different Segment order at the project-level. | [optional] 
**segments** | [**List[RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200ResponseSegmentsInner]**](RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200ResponseSegmentsInner.md) | Array of Wbs Segments | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response import RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response from a JSON string
rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response_instance = RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response_dict = rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response from a dict
rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response_from_dict = RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response.from_dict(rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**default_stage** | **bool** | Default Stage | [optional] 
**dependent_projects** | **int** | Dependent Projects count | [optional] 
**formatted_name** | **str** | Formatted Name | [optional] 
**formatted_parent_name** | **str** | Formatted Parent Name | [optional] 
**name** | **str** | Name | [optional] 
**parent_id** | **int** | Construction Volume Stage ID. Returns null if prefix is linked to a project stage that is the parent. | [optional] 
**procore_category** | **bool** | Indicates whether the project stage the prefix is linked to is a Construction Volume default stage. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage import RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage from a JSON string
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage_instance = RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage_dict = rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage from a dict
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage_from_dict = RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage.from_dict(rest_v10_projects_project_id_rfis_get200_response_inner_all_of_project_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



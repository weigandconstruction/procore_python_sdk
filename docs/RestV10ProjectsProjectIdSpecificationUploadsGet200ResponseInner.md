# RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**issued_date** | **str** |  | [optional] 
**received_date** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**spec_format** | **str** |  | [optional] 
**specification_set_id** | **int** |  | [optional] 
**locale** | **str** | Language used for parsing text | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_get200_response_inner import RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_specification_uploads_get200_response_inner_instance = RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_specification_uploads_get200_response_inner_dict = rest_v10_projects_project_id_specification_uploads_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner from a dict
rest_v10_projects_project_id_specification_uploads_get200_response_inner_from_dict = RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner.from_dict(rest_v10_projects_project_id_specification_uploads_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **date** |  | [optional] 
**deleted_at** | **date** |  | [optional] 
**updated_at** | **date** |  | [optional] 
**var_date** | **date** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_get200_response_inner import RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_specification_sets_get200_response_inner_instance = RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_specification_sets_get200_response_inner_dict = rest_v10_projects_project_id_specification_sets_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner from a dict
rest_v10_projects_project_id_specification_sets_get200_response_inner_from_dict = RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.from_dict(rest_v10_projects_project_id_specification_sets_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



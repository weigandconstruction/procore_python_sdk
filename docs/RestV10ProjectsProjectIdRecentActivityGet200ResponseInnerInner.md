# RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**details** | **str** |  | [optional] 
**number** | **float** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**activity_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**due_date** | **date** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recent_activity_get200_response_inner_inner import RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner from a JSON string
rest_v10_projects_project_id_recent_activity_get200_response_inner_inner_instance = RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recent_activity_get200_response_inner_inner_dict = rest_v10_projects_project_id_recent_activity_get200_response_inner_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner from a dict
rest_v10_projects_project_id_recent_activity_get200_response_inner_inner_from_dict = RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner.from_dict(rest_v10_projects_project_id_recent_activity_get200_response_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



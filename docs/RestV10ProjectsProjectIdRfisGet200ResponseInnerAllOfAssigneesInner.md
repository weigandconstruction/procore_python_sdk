# RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Email | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**locale** | **str** | User locale | [optional] 
**response_required** | **bool** | Designate whether or not the assignee is required to respond | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner import RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner from a JSON string
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner_instance = RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner_dict = rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner from a dict
rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner_from_dict = RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner.from_dict(rest_v10_projects_project_id_rfis_get200_response_inner_all_of_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



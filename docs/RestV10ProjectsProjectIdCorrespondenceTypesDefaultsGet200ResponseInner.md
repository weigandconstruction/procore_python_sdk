# RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**correspondence_type_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**due_days** | **int** |  | [optional] 
**distribution_members** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) | Distribution Members | [optional] 
**available_statuses** | **List[str]** |  | [optional] 
**statuses** | [**List[RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInnerStatusesInner]**](RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInnerStatusesInner.md) | Statuses | [optional] 
**private_by_default** | **bool** |  | [optional] 
**workflows_enabled** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner import RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner_instance = RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner_dict = rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner from a dict
rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner_from_dict = RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner.from_dict(rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



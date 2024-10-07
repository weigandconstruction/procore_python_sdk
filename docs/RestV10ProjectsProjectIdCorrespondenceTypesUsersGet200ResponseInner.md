# RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**company** | [**RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInnerCompany**](RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInnerCompany.md) |  | [optional] 
**generic_tools** | [**List[RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInnerGenericToolsInner]**](RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInnerGenericToolsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_correspondence_types_users_get200_response_inner import RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner from a JSON string
rest_v10_projects_project_id_correspondence_types_users_get200_response_inner_instance = RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_correspondence_types_users_get200_response_inner_dict = rest_v10_projects_project_id_correspondence_types_users_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner from a dict
rest_v10_projects_project_id_correspondence_types_users_get200_response_inner_from_dict = RestV10ProjectsProjectIdCorrespondenceTypesUsersGet200ResponseInner.from_dict(rest_v10_projects_project_id_correspondence_types_users_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



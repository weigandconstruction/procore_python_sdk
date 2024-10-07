# RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | access level | [optional] 
**name** | **str** | friendly name for level | [optional] 
**permitted_actions** | **object** | actions supported by access level by tool | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level import RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel from a JSON string
rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level_instance = RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel.to_json())

# convert the object into a dict
rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level_dict = rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel from a dict
rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level_from_dict = RestV10ProjectsProjectIdCorrespondenceTypesPermissionsGet200ResponseInnerUserAccessLevel.from_dict(rest_v10_projects_project_id_correspondence_types_permissions_get200_response_inner_user_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



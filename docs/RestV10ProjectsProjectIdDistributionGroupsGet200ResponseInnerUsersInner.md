# RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID of the User | [optional] 
**name** | **str** |  | [optional] 
**login** | **str** | Email | [optional] 
**image_url** | **str** | User avatar url | [optional] 
**initials** | **str** | User initials | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner import RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner from a JSON string
rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner_instance = RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner_dict = rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner from a dict
rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner_from_dict = RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner.from_dict(rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



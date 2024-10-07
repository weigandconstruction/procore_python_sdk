# RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Email | [optional] 
**id** | **int** | Login Information ID of the User | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_post200_response_users_inner import RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner from a JSON string
rest_v10_projects_project_id_distribution_groups_post200_response_users_inner_instance = RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_distribution_groups_post200_response_users_inner_dict = rest_v10_projects_project_id_distribution_groups_post200_response_users_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner from a dict
rest_v10_projects_project_id_distribution_groups_post200_response_users_inner_from_dict = RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.from_dict(rest_v10_projects_project_id_distribution_groups_post200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



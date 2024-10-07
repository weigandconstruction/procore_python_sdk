# RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner

Distribution Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**users** | [**List[RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner]**](RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner.md) | Only included if the &#39;extended&#39; view is supported | [optional] 
**domain_user_ids** | **List[int]** | List of user IDs that have permissions to view specified domain. Only included if the &#39;extended&#39; view is supported and &#39;with_domain_users&#39; param is sent. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_get200_response_inner import RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_distribution_groups_get200_response_inner_instance = RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_distribution_groups_get200_response_inner_dict = rest_v10_projects_project_id_distribution_groups_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner from a dict
rest_v10_projects_project_id_distribution_groups_get200_response_inner_from_dict = RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner.from_dict(rest_v10_projects_project_id_distribution_groups_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



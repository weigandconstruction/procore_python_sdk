# RestV10ProjectsProjectIdDistributionGroupsPost200Response

Distribution Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**users** | [**List[RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner]**](RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.md) | Only included if the &#39;extended&#39; view is supported | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_post200_response import RestV10ProjectsProjectIdDistributionGroupsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDistributionGroupsPost200Response from a JSON string
rest_v10_projects_project_id_distribution_groups_post200_response_instance = RestV10ProjectsProjectIdDistributionGroupsPost200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDistributionGroupsPost200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_distribution_groups_post200_response_dict = rest_v10_projects_project_id_distribution_groups_post200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDistributionGroupsPost200Response from a dict
rest_v10_projects_project_id_distribution_groups_post200_response_from_dict = RestV10ProjectsProjectIdDistributionGroupsPost200Response.from_dict(rest_v10_projects_project_id_distribution_groups_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



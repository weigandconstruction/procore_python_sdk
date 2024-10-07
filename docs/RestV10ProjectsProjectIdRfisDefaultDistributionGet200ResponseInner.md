# RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the user. | [optional] 
**login** | **str** | The email address of the user that is used to log in. | [optional] 
**name** | **str** | The name of the user. | [optional] 
**company_name** | **str** | User&#39;s Company Name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner import RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner from a JSON string
rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner_instance = RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner_dict = rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner from a dict
rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner_from_dict = RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.from_dict(rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



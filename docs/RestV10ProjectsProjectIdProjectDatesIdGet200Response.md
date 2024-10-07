# RestV10ProjectsProjectIdProjectDatesIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Date Id | [optional] 
**project_membership_id** | **int** | Project Date Membership. The project date membership id associates a project date with an existing project. | [optional] 
**name** | **str** | Project Date Name | [optional] 
**var_date** | **str** | Project Date Date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_project_dates_id_get200_response import RestV10ProjectsProjectIdProjectDatesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProjectDatesIdGet200Response from a JSON string
rest_v10_projects_project_id_project_dates_id_get200_response_instance = RestV10ProjectsProjectIdProjectDatesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProjectDatesIdGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_project_dates_id_get200_response_dict = rest_v10_projects_project_id_project_dates_id_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProjectDatesIdGet200Response from a dict
rest_v10_projects_project_id_project_dates_id_get200_response_from_dict = RestV10ProjectsProjectIdProjectDatesIdGet200Response.from_dict(rest_v10_projects_project_id_project_dates_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



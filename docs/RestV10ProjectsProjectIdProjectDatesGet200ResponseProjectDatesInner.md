# RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Date ID | [optional] 
**project_membership_id** | **int** | Project Date Membership ID. The project date membership id associates a project date with an existing project. | [optional] 
**name** | **str** | Project Date Name | [optional] 
**var_date** | **str** | Project Date Date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner import RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner from a JSON string
rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner_instance = RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner_dict = rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner from a dict
rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner_from_dict = RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner.from_dict(rest_v10_projects_project_id_project_dates_get200_response_project_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



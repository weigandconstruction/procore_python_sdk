# RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key name is the filter field | [optional] 
**value** | **str** | Value is the attribute to filter on | [optional] 
**endpoint** | **str** | Endpoint is the path to the filter options endpoint | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_submittals_filter_options_get200_response_inner import RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_submittals_filter_options_get200_response_inner_instance = RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_submittals_filter_options_get200_response_inner_dict = rest_v10_projects_project_id_submittals_filter_options_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner from a dict
rest_v10_projects_project_id_submittals_filter_options_get200_response_inner_from_dict = RestV10ProjectsProjectIdSubmittalsFilterOptionsGet200ResponseInner.from_dict(rest_v10_projects_project_id_submittals_filter_options_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



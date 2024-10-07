# RestV10ProjectsProjectIdSpecificationSetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of specification set | 
**var_date** | **str** | Creation date of specification set | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_post_request import RestV10ProjectsProjectIdSpecificationSetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSpecificationSetsPostRequest from a JSON string
rest_v10_projects_project_id_specification_sets_post_request_instance = RestV10ProjectsProjectIdSpecificationSetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSpecificationSetsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_specification_sets_post_request_dict = rest_v10_projects_project_id_specification_sets_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSpecificationSetsPostRequest from a dict
rest_v10_projects_project_id_specification_sets_post_request_from_dict = RestV10ProjectsProjectIdSpecificationSetsPostRequest.from_dict(rest_v10_projects_project_id_specification_sets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



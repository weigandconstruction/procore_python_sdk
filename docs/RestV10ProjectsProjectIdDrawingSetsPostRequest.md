# RestV10ProjectsProjectIdDrawingSetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Drawing Set name | 
**var_date** | **date** | Drawing Set date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_drawing_sets_post_request import RestV10ProjectsProjectIdDrawingSetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDrawingSetsPostRequest from a JSON string
rest_v10_projects_project_id_drawing_sets_post_request_instance = RestV10ProjectsProjectIdDrawingSetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDrawingSetsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_drawing_sets_post_request_dict = rest_v10_projects_project_id_drawing_sets_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDrawingSetsPostRequest from a dict
rest_v10_projects_project_id_drawing_sets_post_request_from_dict = RestV10ProjectsProjectIdDrawingSetsPostRequest.from_dict(rest_v10_projects_project_id_drawing_sets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdQuantityLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity_log** | [**RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog**](RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_quantity_logs_post_request import RestV10ProjectsProjectIdQuantityLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdQuantityLogsPostRequest from a JSON string
rest_v10_projects_project_id_quantity_logs_post_request_instance = RestV10ProjectsProjectIdQuantityLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdQuantityLogsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_quantity_logs_post_request_dict = rest_v10_projects_project_id_quantity_logs_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdQuantityLogsPostRequest from a dict
rest_v10_projects_project_id_quantity_logs_post_request_from_dict = RestV10ProjectsProjectIdQuantityLogsPostRequest.from_dict(rest_v10_projects_project_id_quantity_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



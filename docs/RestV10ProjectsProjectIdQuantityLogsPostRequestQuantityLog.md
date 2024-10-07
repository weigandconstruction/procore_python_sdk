# RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**description** | **str** | Description | [optional] 
**quantity** | **int** | Total number of the specified materials placed on the site that day | [optional] 
**unit** | **str** | Units that were delivered | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**location_id** | **int** | The ID of the Location of the Quantity Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_quantity_logs_post_request_quantity_log import RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog from a JSON string
rest_v10_projects_project_id_quantity_logs_post_request_quantity_log_instance = RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_quantity_logs_post_request_quantity_log_dict = rest_v10_projects_project_id_quantity_logs_post_request_quantity_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog from a dict
rest_v10_projects_project_id_quantity_logs_post_request_quantity_log_from_dict = RestV10ProjectsProjectIdQuantityLogsPostRequestQuantityLog.from_dict(rest_v10_projects_project_id_quantity_logs_post_request_quantity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | 
**start_date** | **date** | Start Date, expressed in ISO 8601 date format (YYYY-MM-DD) | 
**end_date** | **date** | End Date, expressed in ISO 8601 date format (YYYY-MM-DD) | 
**unit_of_measure** | **str** | Unit of Measure | 
**unit_cost** | **str** | Unit Cost | 
**utilization** | **str** | Utilization, expressed as a decimal where 1.0 is 100% | 
**budget_line_item_id** | **int** | Budget Line Item ID | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource import RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource from a JSON string
rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource_instance = RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource.to_json())

# convert the object into a dict
rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource_dict = rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource from a dict
rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource_from_dict = RestV10ProjectsProjectIdMonitoringResourcesPostRequestMonitoringResource.from_dict(rest_v10_projects_project_id_monitoring_resources_post_request_monitoring_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



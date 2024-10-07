# RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**start_date** | **date** | Start Date, expressed in ISO 8601 date format (YYYY-MM-DD) | [optional] 
**end_date** | **date** | End Date, expressed in ISO 8601 date format (YYYY-MM-DD) | [optional] 
**unit_of_measure** | **str** | Unit of Measure | [optional] 
**unit_cost** | **str** | Unit Cost | [optional] 
**utilization** | **str** | Utilization, expressed as a decimal where 1.0 is 100% | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource import RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource from a JSON string
rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource_instance = RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource.to_json())

# convert the object into a dict
rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource_dict = rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource from a dict
rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource_from_dict = RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequestMonitoringResource.from_dict(rest_v10_projects_project_id_monitoring_resources_id_patch_request_monitoring_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



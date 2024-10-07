# RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | Description | [optional] 
**start_date** | **str** | Start date, formatted based on the project&#39;s locale | [optional] 
**end_date** | **str** | End date, formatted based on the project&#39;s locale | [optional] 
**unit_of_measure** | **str** | Unit of measure | [optional] 
**unit_cost** | **float** | Unit cost | [optional] 
**units_remaining** | **int** | Units remaining, calculated as of today or as of the provided forecast_start_date parameter | [optional] 
**forecast_to_complete** | **float** | Forecast to complete | [optional] 
**planned_total_cost** | **float** | Planned total cost | [optional] 
**total_units** | **int** | Total units | [optional] 
**utilization** | **float** | Utilization | [optional] 
**budget_line_item_id** | **int** | ID of the associated Budget Line Item | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_get200_response_inner import RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_monitoring_resources_get200_response_inner_instance = RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_monitoring_resources_get200_response_inner_dict = rest_v10_projects_project_id_monitoring_resources_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner from a dict
rest_v10_projects_project_id_monitoring_resources_get200_response_inner_from_dict = RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.from_dict(rest_v10_projects_project_id_monitoring_resources_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



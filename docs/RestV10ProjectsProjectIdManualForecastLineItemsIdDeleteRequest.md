# RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_line_item_id** | **int** | Identifier of the parent budget line item. NOTE - budget line item id or wbs code id is required | [optional] 
**wbs_code_id** | **int** | Wbs code id of the parent budget line item. NOTE - budget line item id or wbs code id is required | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request import RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest from a JSON string
rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request_instance = RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request_dict = rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest from a dict
rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request_from_dict = RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest.from_dict(rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



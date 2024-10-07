# RestV10ProjectsProjectIdManualForecastLineItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_line_item_id** | **int** | Identifier of the parent budget line item. NOTE - budget line item id or wbs code id is required | [optional] 
**wbs_code_id** | **int** | Wbs code id of the parent budget line item. NOTE - budget line item id or wbs code id is required | [optional] 
**description** | **str** | Description | [optional] 
**quantity** | **int** | Quantity | [optional] 
**uom** | **str** | Unit of measure | [optional] 
**unit_cost** | **float** | Unit cost | [optional] 
**amount** | **float** | Total amount | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_post_request import RestV10ProjectsProjectIdManualForecastLineItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsPostRequest from a JSON string
rest_v10_projects_project_id_manual_forecast_line_items_post_request_instance = RestV10ProjectsProjectIdManualForecastLineItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManualForecastLineItemsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manual_forecast_line_items_post_request_dict = rest_v10_projects_project_id_manual_forecast_line_items_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsPostRequest from a dict
rest_v10_projects_project_id_manual_forecast_line_items_post_request_from_dict = RestV10ProjectsProjectIdManualForecastLineItemsPostRequest.from_dict(rest_v10_projects_project_id_manual_forecast_line_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



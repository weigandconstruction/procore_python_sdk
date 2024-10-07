# RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**budget_line_item_id** | **int** | Id of the associated Budget Line Item | [optional] 
**wbs_code_id** | **int** | Wbs code id of the associated Budget Line Item | [optional] 
**budget_forecast_id** | **int** | Id of the associated parent budget forecast | [optional] 
**project_id** | **int** | Id of the associated project | [optional] 
**company_id** | **int** | Id of the associated project | [optional] 
**description** | **str** | Description | [optional] 
**quantity** | **int** | Quantity | [optional] 
**uom** | **str** | Unit of measure | [optional] 
**unit_cost** | **float** | Unit cost | [optional] 
**amount** | **float** | Total amount | [optional] 
**created_at** | **datetime** | Date-time the manual forecast line item was created | [optional] 
**updated_at** | **datetime** | Date-time the manual forecast line item was last updated | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner import RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner_instance = RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner_dict = rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner from a dict
rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner_from_dict = RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner.from_dict(rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



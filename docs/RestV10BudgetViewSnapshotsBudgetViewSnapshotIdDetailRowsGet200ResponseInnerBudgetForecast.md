# RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast

ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**manual_amount** | **float** | Budget forecast manual amount | [optional] 
**automatic_amount** | **float** | Budget forecast automatic amount | [optional] 
**amount** | **float** | Budget forecast amount | [optional] 
**automatically_calculated** | **bool** | Indicates if the amount is the automatic_amount or the manual_amount | [optional] 
**calculation_strategy** | **str** | Indicates how the amount is calculated | [optional] 
**notes** | **str** | Budget forecast notes | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast import RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast from a JSON string
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast_instance = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast_dict = rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast from a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast_from_dict = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast.from_dict(rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_budget_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



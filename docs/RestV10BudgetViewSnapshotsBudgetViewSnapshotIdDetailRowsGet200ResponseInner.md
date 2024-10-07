# RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner

Budget View Detail Row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**deletable** | **bool** | Indicates if the underlying Budget Line Item can be deleted | [optional] 
**company_id** | **int** | Company ID | [optional] 
**company** | **str** | Company name | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**wbs_code_id** | **int** | WBS Code ID or null if WBS information is not available | [optional] 
**biller_id** | **int** | Sub-job or project ID | [optional] 
**root_cost_code_id** | **int** | Division ID | [optional] 
**cost_code_id** | **int** | Cost code ID | [optional] 
**cost_code_origin_id** | **str** | Cost code origin ID | [optional] 
**category_id** | **int** | Category ID | [optional] 
**project** | **str** | Project name | [optional] 
**biller** | **str** | Biller name | [optional] 
**biller_type** | **str** | Biller type | [optional] 
**root_cost_code** | **str** | Division name | [optional] 
**cost_code** | **str** | Cost code name | [optional] 
**category** | **str** | Category | [optional] 
**budget_modifications** | **float** | Budget modifications | [optional] 
**original_budget_amount** | **float** | Original budget amount | [optional] 
**budget_forecast** | [**RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast**](RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInnerBudgetForecast.md) |  | [optional] 
**currency_configuration** | [**RestV10BudgetViewsBudgetViewIdSummaryRowsGet200ResponseInnerCurrencyConfiguration**](RestV10BudgetViewsBudgetViewIdSummaryRowsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**unbudgeted_reason** | **str** | Reason a line does not have a budget_line_item_id | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner import RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner from a JSON string
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_instance = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_dict = rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner from a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_from_dict = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdDetailRowsGet200ResponseInner.from_dict(rest_v10_budget_view_snapshots_budget_view_snapshot_id_detail_rows_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



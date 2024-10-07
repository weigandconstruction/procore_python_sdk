# RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner

Budget View Summary Row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the resource represented by this summary row | [optional] 
**name** | **str** | Name of the resource represented by this summary row | [optional] 
**biller_type** | **str** | Biller type. Populated if group_by is biller. | [optional] 
**budget_line_item_ids** | **List[str]** | List of budget line item ids within this group | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner import RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner from a JSON string
rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner_instance = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner_dict = rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner from a dict
rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner_from_dict = RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner.from_dict(rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



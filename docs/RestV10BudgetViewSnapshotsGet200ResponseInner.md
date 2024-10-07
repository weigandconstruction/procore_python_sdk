# RestV10BudgetViewSnapshotsGet200ResponseInner

Budget View Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**created_at** | **str** | Created At timestamp | [optional] 
**created_by** | [**RestV10BudgetViewsGet200ResponseInnerCreatedBy**](RestV10BudgetViewsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**budget_view** | [**RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView**](RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView.md) |  | [optional] 
**links** | [**RestV10BudgetViewSnapshotsGet200ResponseInnerLinks**](RestV10BudgetViewSnapshotsGet200ResponseInnerLinks.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_get200_response_inner import RestV10BudgetViewSnapshotsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsGet200ResponseInner from a JSON string
rest_v10_budget_view_snapshots_get200_response_inner_instance = RestV10BudgetViewSnapshotsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_get200_response_inner_dict = rest_v10_budget_view_snapshots_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsGet200ResponseInner from a dict
rest_v10_budget_view_snapshots_get200_response_inner_from_dict = RestV10BudgetViewSnapshotsGet200ResponseInner.from_dict(rest_v10_budget_view_snapshots_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



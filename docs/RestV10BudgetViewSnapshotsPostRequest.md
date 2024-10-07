# RestV10BudgetViewSnapshotsPostRequest

Budget Snapshot information Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project identifier | 
**budget_template_id** | **int** | The budget template identifier | 
**name** | **str** | Title of the budget snapshot | 
**description** | **str** | Description of the budget snapshot | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_post_request import RestV10BudgetViewSnapshotsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsPostRequest from a JSON string
rest_v10_budget_view_snapshots_post_request_instance = RestV10BudgetViewSnapshotsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsPostRequest.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_post_request_dict = rest_v10_budget_view_snapshots_post_request_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsPostRequest from a dict
rest_v10_budget_view_snapshots_post_request_from_dict = RestV10BudgetViewSnapshotsPostRequest.from_dict(rest_v10_budget_view_snapshots_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10BudgetViewSnapshotsPost202ResponseData

Budget View Snapshot Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_request_id** | **int** | Snapshot Request ID | [optional] 
**status** | **str** | Status of the snapshot request | [optional] 
**budget_template_id** | **int** | ID of the Budget Template | [optional] 
**project_id** | **int** | ID of the Project | [optional] 
**company_id** | **int** | ID of the Company | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_view_snapshots_post202_response_data import RestV10BudgetViewSnapshotsPost202ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewSnapshotsPost202ResponseData from a JSON string
rest_v10_budget_view_snapshots_post202_response_data_instance = RestV10BudgetViewSnapshotsPost202ResponseData.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewSnapshotsPost202ResponseData.to_json())

# convert the object into a dict
rest_v10_budget_view_snapshots_post202_response_data_dict = rest_v10_budget_view_snapshots_post202_response_data_instance.to_dict()
# create an instance of RestV10BudgetViewSnapshotsPost202ResponseData from a dict
rest_v10_budget_view_snapshots_post202_response_data_from_dict = RestV10BudgetViewSnapshotsPost202ResponseData.from_dict(rest_v10_budget_view_snapshots_post202_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



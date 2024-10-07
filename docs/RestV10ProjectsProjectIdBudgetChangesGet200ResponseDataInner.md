# RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the budget change | [optional] 
**number** | **int** | Number field of the budget change | [optional] 
**status** | **str** | Status of the budget change | [optional] 
**title** | **str** | Title of budget change | [optional] 
**description** | **str** | Description of the budget change in HTML format | [optional] 
**erp_status** | **str** | Displays the state the ERP entity is in. | [optional] 
**prime_contract_id** | **int** | Unique identifier for the prime contract this budget change is associated with | [optional] 
**amount** | **float** | Total amount of adjustments | [optional] 
**change_event_line_item_ids** | **List[int]** | List of change event line item ids | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_get200_response_data_inner import RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner from a JSON string
rest_v10_projects_project_id_budget_changes_get200_response_data_inner_instance = RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_get200_response_data_inner_dict = rest_v10_projects_project_id_budget_changes_get200_response_data_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner from a dict
rest_v10_projects_project_id_budget_changes_get200_response_data_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesGet200ResponseDataInner.from_dict(rest_v10_projects_project_id_budget_changes_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



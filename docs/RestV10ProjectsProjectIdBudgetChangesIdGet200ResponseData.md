# RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the budget change | [optional] 
**number** | **int** | Number field of the budget change | [optional] 
**status** | **str** | Status of the budget change | [optional] 
**title** | **str** | Title of budget change | [optional] 
**description** | **str** | Description of the budget change in HTML format | [optional] 
**erp_status** | **str** | Displays the state the ERP entity is in. | [optional] 
**amount** | **float** | Total amount of the budget change | [optional] 
**prime_contract** | [**RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseDataAllOfPrimeContract**](RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseDataAllOfPrimeContract.md) |  | [optional] 
**attachments** | [**List[RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner]**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner.md) |  | [optional] 
**adjustment_line_items** | [**List[RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner]**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner.md) | todo this key be renamed to line_items in the future | [optional] 
**production_quantities** | [**List[RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner]**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner.md) | List of budget change production quantities | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_id_get200_response_data import RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData from a JSON string
rest_v10_projects_project_id_budget_changes_id_get200_response_data_instance = RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_id_get200_response_data_dict = rest_v10_projects_project_id_budget_changes_id_get200_response_data_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData from a dict
rest_v10_projects_project_id_budget_changes_id_get200_response_data_from_dict = RestV10ProjectsProjectIdBudgetChangesIdGet200ResponseData.from_dict(rest_v10_projects_project_id_budget_changes_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



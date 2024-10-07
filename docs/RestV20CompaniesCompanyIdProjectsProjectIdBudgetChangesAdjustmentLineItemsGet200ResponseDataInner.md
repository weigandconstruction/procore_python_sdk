# RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner

Budget Change Adjustment line item Summarized

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the line item. ID can be combined with the type to uniquely identify an adjustment line item for a project | [optional] 
**adjustment_number** | **int** | The number of the adjustment this line item belongs to | [optional] 
**wbs_code_id** | **str** | The WBS code ID of this line item | [optional] 
**amount** | **float** | The amount of this line item | [optional] 
**uom** | **str** | The unit of measure of this line item | [optional] 
**quantity** | **float** | The quantity of this line item | [optional] 
**description** | **str** | The description of this line item | [optional] 
**type** | **str** | Used to identify type of line item. Type can be combined with the ID to uniquely identify an adjustment line item for a project. Type change_event corresponds to the first line in an adjustment in the UI. The subsequent lines of that adjustment are of type budget_change | [optional] 
**budget_change_number** | **str** | The number of the budget change this line item belongs to | [optional] 
**budget_change_status** | **str** | The status of the budget change | [optional] 
**budget_change_name** | **str** | The name of the budget change | [optional] 
**budget_change_id** | **str** | The ID of the budget change | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner import RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner from a JSON string
rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner_instance = RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner_dict = rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner from a dict
rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200ResponseDataInner.from_dict(rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



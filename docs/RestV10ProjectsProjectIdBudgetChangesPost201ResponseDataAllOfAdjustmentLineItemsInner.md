# RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner

Budget Change Adjustment line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID of this adjustment | [optional] 
**ref** | **str** | Identifier used to map line items in the request to their respective objects or errors in the response | [optional] 
**adjustment_number** | **int** | Number of this adjustment. When creating a line item with type &#39;change_event&#39;, this is optional and it will be auto-assigned an adjustment_number. However, it is required when creating a line item with type &#39;budget_change&#39;. | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**description** | **str** | Description of the adjustment | [optional] 
**comment** | **str** | Comment of the adjustment | [optional] 
**calculation_strategy** | **str** | Cost calculation strategy | [optional] 
**quantity** | **float** | Estimated cost quantity | [optional] 
**type** | **str** | used to identify type of line item. id uniqueness is guaranteed per type | [optional] 
**uom** | **str** | Unit of measure used | [optional] 
**unit_cost** | **float** | Estimated unit cost | [optional] 
**amount** | **float** | Estimated cost amount | [optional] 
**change_event_line_item_id** | **float** | ID of the associated change event line item if it exists (To be deprecated, use change_event_line_item instead) | [optional] 
**change_event_line_item** | [**RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInnerChangeEventLineItem**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInnerChangeEventLineItem.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner import RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner from a JSON string
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner_instance = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner_dict = rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner from a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAdjustmentLineItemsInner.from_dict(rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_adjustment_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



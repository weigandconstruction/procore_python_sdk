# RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner

Budget Change Adjustment line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Identifier used to map line items in the request to their respective objects or errors in the response | [optional] 
**adjustment_number** | **int** | Number of this adjustment | [optional] 
**wbs_code_id** | **int** | Work Breakdown Structure Code ID | [optional] 
**description** | **str** | Description of the adjustment | [optional] 
**comment** | **str** | Comment of the adjustment | [optional] 
**calculation_strategy** | **str** | Cost calculation strategy | [optional] 
**quantity** | **float** | Estimated cost quantity | [optional] 
**type** | **str** | Used to identify type of line item. id uniquess is guaranteed per type.  NOTE: To add an Adjustment Line Item with the type budget_change for an adjustment_number, an Adjustment Line item with the type change_event must be created for the same adjustment_number. | [optional] 
**uom** | **str** | Unit of measure used | [optional] 
**unit_cost** | **float** | Estimated unit cost | [optional] 
**amount** | **float** | Estimated cost amount | [optional] 
**change_event_line_item_id** | **int** | ID for the change event line item associated with the adjustment | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner import RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner from a JSON string
rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner_instance = RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner_dict = rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner from a dict
rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner.from_dict(rest_v10_projects_project_id_budget_changes_post_request_adjustment_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



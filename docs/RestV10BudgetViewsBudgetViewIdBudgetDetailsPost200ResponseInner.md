# RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner

Budget Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerBiller**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerBiller.md) |  | [optional] 
**contract** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract.md) |  | [optional] 
**cost_code** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerCostCode**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerCostCode.md) |  | [optional] 
**cost_type** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerCostType**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerCostType.md) |  | [optional] 
**description** | **str** | Information about the record being returned by the Budget Detail Report | [optional] 
**detail_type** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerDetailType**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerDetailType.md) |  | [optional] 
**id** | **str** | ID of a given budget detail row | [optional] 
**item** | **str** | Information about the budget detail row as it pertains to its source | [optional] 
**link** | **str** | Link to the source in the web app where a detail row can be found | [optional] 
**root_cost_code** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerRootCostCode**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerRootCostCode.md) |  | [optional] 
**vendor** | [**RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerVendor**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerVendor.md) |  | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner import RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner from a JSON string
rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_instance = RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_dict = rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner from a dict
rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_from_dict = RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner.from_dict(rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



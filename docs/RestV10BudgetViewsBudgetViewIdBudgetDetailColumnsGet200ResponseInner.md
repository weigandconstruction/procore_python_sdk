# RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner

Budget Detail Columns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatable** | **bool** | Indicates whether or not a column&#39;s values can be aggregated | [optional] 
**filterable** | **bool** | Indicates whether or not budget details can be filtered by a column&#39;s values | [optional] 
**groupable** | **bool** | Indicates whether or not budget details can be grouped by a column&#39;s values | [optional] 
**id** | **str** | Field used to identify a column&#39;s value in a budget detail row | [optional] 
**name** | **str** | Name of a column used in the Budget Detail Report | [optional] 
**position** | **int** | Indicates order in which columns appear in the Budget Detail Report | [optional] 
**type** | **str** | Describes what type a column is | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner import RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner from a JSON string
rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner_instance = RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner_dict = rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner from a dict
rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner_from_dict = RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner.from_dict(rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



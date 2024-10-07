# BudgetDetailFilterOptions

Budget Detail Filters Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller** | [**List[BudgetDetailFilterOptionsBillerInner]**](BudgetDetailFilterOptionsBillerInner.md) | Sub Job Filter, can pass Sub Job or Project | [optional] 
**cost_code** | **List[int]** | Cost Code Filter | [optional] 
**root_cost_code** | **List[int]** | Division Filter | [optional] 
**cost_type** | **List[int]** | Cost Type Filter | [optional] 
**vendor** | **List[int]** | Vendor Filter | [optional] 
**detail_type** | **List[str]** | Detail Type Filter | [optional] 

## Example

```python
from procore_sdk.models.budget_detail_filter_options import BudgetDetailFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailFilterOptions from a JSON string
budget_detail_filter_options_instance = BudgetDetailFilterOptions.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailFilterOptions.to_json())

# convert the object into a dict
budget_detail_filter_options_dict = budget_detail_filter_options_instance.to_dict()
# create an instance of BudgetDetailFilterOptions from a dict
budget_detail_filter_options_from_dict = BudgetDetailFilterOptions.from_dict(budget_detail_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



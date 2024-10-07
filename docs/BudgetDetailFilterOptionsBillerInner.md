# BudgetDetailFilterOptionsBillerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** | ID of Project or Sub Job | [optional] 
**type** | **str** | Type of Biller | [optional] 
**name** | **str** | Name of Project or Sub Job | [optional] 

## Example

```python
from procore_sdk.models.budget_detail_filter_options_biller_inner import BudgetDetailFilterOptionsBillerInner

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailFilterOptionsBillerInner from a JSON string
budget_detail_filter_options_biller_inner_instance = BudgetDetailFilterOptionsBillerInner.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailFilterOptionsBillerInner.to_json())

# convert the object into a dict
budget_detail_filter_options_biller_inner_dict = budget_detail_filter_options_biller_inner_instance.to_dict()
# create an instance of BudgetDetailFilterOptionsBillerInner from a dict
budget_detail_filter_options_biller_inner_from_dict = BudgetDetailFilterOptionsBillerInner.from_dict(budget_detail_filter_options_biller_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



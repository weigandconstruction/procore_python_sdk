# RestV10BudgetDetailFiltersGet200ResponseInner

Budget Detail Filter Options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Display Value for a filter option | [optional] 
**value** | **List[int]** | Filter values to use for filtering List Budget Details API | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_detail_filters_get200_response_inner import RestV10BudgetDetailFiltersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetDetailFiltersGet200ResponseInner from a JSON string
rest_v10_budget_detail_filters_get200_response_inner_instance = RestV10BudgetDetailFiltersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetDetailFiltersGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_detail_filters_get200_response_inner_dict = rest_v10_budget_detail_filters_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetDetailFiltersGet200ResponseInner from a dict
rest_v10_budget_detail_filters_get200_response_inner_from_dict = RestV10BudgetDetailFiltersGet200ResponseInner.from_dict(rest_v10_budget_detail_filters_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10BudgetViewsGet200ResponseInnerLinks

Links to get budgeting data using this budget view

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_rows** | **str** | URL to the Budget Detail Rows for this budget view | [optional] 
**summary_rows** | **str** | URL to the Budget Summary Rows for this budget view | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_views_get200_response_inner_links import RestV10BudgetViewsGet200ResponseInnerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewsGet200ResponseInnerLinks from a JSON string
rest_v10_budget_views_get200_response_inner_links_instance = RestV10BudgetViewsGet200ResponseInnerLinks.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewsGet200ResponseInnerLinks.to_json())

# convert the object into a dict
rest_v10_budget_views_get200_response_inner_links_dict = rest_v10_budget_views_get200_response_inner_links_instance.to_dict()
# create an instance of RestV10BudgetViewsGet200ResponseInnerLinks from a dict
rest_v10_budget_views_get200_response_inner_links_from_dict = RestV10BudgetViewsGet200ResponseInnerLinks.from_dict(rest_v10_budget_views_get200_response_inner_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



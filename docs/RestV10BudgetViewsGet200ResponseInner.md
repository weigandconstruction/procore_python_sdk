# RestV10BudgetViewsGet200ResponseInner

Budget View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**created_at** | **str** | Created At timestamp | [optional] 
**created_by** | [**RestV10BudgetViewsGet200ResponseInnerCreatedBy**](RestV10BudgetViewsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**updated_at** | **str** | Updated At timestamp | [optional] 
**role** | **str** | Role of the view | [optional] 
**links** | [**RestV10BudgetViewsGet200ResponseInnerLinks**](RestV10BudgetViewsGet200ResponseInnerLinks.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_views_get200_response_inner import RestV10BudgetViewsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetViewsGet200ResponseInner from a JSON string
rest_v10_budget_views_get200_response_inner_instance = RestV10BudgetViewsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetViewsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_budget_views_get200_response_inner_dict = rest_v10_budget_views_get200_response_inner_instance.to_dict()
# create an instance of RestV10BudgetViewsGet200ResponseInner from a dict
rest_v10_budget_views_get200_response_inner_from_dict = RestV10BudgetViewsGet200ResponseInner.from_dict(rest_v10_budget_views_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



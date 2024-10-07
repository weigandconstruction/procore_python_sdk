# RestV10BudgetLineItemsPost422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error** | **str** | Description of the Budget Currency error. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_line_items_post422_response import RestV10BudgetLineItemsPost422Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetLineItemsPost422Response from a JSON string
rest_v10_budget_line_items_post422_response_instance = RestV10BudgetLineItemsPost422Response.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetLineItemsPost422Response.to_json())

# convert the object into a dict
rest_v10_budget_line_items_post422_response_dict = rest_v10_budget_line_items_post422_response_instance.to_dict()
# create an instance of RestV10BudgetLineItemsPost422Response from a dict
rest_v10_budget_line_items_post422_response_from_dict = RestV10BudgetLineItemsPost422Response.from_dict(rest_v10_budget_line_items_post422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



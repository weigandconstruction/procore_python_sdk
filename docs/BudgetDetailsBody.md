# BudgetDetailsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**BudgetDetailFilterOptions**](BudgetDetailFilterOptions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.budget_details_body import BudgetDetailsBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailsBody from a JSON string
budget_details_body_instance = BudgetDetailsBody.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailsBody.to_json())

# convert the object into a dict
budget_details_body_dict = budget_details_body_instance.to_dict()
# create an instance of BudgetDetailsBody from a dict
budget_details_body_from_dict = BudgetDetailsBody.from_dict(budget_details_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



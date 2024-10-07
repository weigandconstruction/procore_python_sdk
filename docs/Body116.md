# Body116


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**budget_line_item** | [**BudgetLineItem**](BudgetLineItem.md) |  | 

## Example

```python
from procore_sdk.models.body116 import Body116

# TODO update the JSON string below
json = "{}"
# create an instance of Body116 from a JSON string
body116_instance = Body116.from_json(json)
# print the JSON string representation of the object
print(Body116.to_json())

# convert the object into a dict
body116_dict = body116_instance.to_dict()
# create an instance of Body116 from a dict
body116_from_dict = Body116.from_dict(body116_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



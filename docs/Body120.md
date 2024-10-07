# Body120


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID | 
**budget_line_items** | [**List[Body120BudgetLineItemsInner]**](Body120BudgetLineItemsInner.md) |  | 

## Example

```python
from procore_sdk.models.body120 import Body120

# TODO update the JSON string below
json = "{}"
# create an instance of Body120 from a JSON string
body120_instance = Body120.from_json(json)
# print the JSON string representation of the object
print(Body120.to_json())

# convert the object into a dict
body120_dict = body120_instance.to_dict()
# create an instance of Body120 from a dict
body120_from_dict = Body120.from_dict(body120_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


